"""Asistente de la Hackathon Río Maipo para Colab o Jupyter, sin instalar nada.

Conversa con el mismo router que usa OpenCode, con los mismos /explorar y /auditar:

    from asistente import preguntar, explorar, auditar, nueva, saldo
    explorar("¿por qué el río se enturbia en verano sin llover?")
    preguntar("¿cómo grafico el caudal mediano por mes?", df)   # df opcional: envía un resumen, no la tabla
    auditar('''X = df[["q_m3s", "p_liq_48h_mm"]] ...''')
    nueva()    # empieza una conversación nueva
    saldo()    # cuánto presupuesto le queda al equipo
"""

from __future__ import annotations

import getpass
import json
import os
import ssl
import urllib.error
import urllib.request
import uuid
from pathlib import Path

AQUI = Path(__file__).resolve().parent
URL = json.loads((AQUI / "opencode.json").read_text(encoding="utf-8"))["provider"]["maipo-router"]["options"]["baseURL"]
MODO_CHAT = (
    "Estás en modo chat dentro de un notebook: no puedes ejecutar código ni leer archivos. "
    "Da código corto para que el equipo lo corra en su celda y pídele que te pegue el resultado.\n\n"
)
SISTEMA = {"role": "system", "content": MODO_CHAT + (AQUI / "AGENTS.md").read_text(encoding="utf-8")}

try:  # el Python de python.org en macOS no trae certificados raíz; certifi sí (viene con jupyter y requests)
    import certifi

    _SSL = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL = ssl.create_default_context()

_historial: list[dict[str, str]] = []
_sesion = uuid.uuid4().hex
_llave: str | None = None


def _llave_api() -> str:
    """Busca la llave en la variable de entorno, luego en los Secretos de Colab y, si no está, la pide."""
    global _llave
    if not _llave:
        _llave = os.environ.get("MAIPO_API_KEY")
    if not _llave:
        try:
            from google.colab import userdata

            _llave = userdata.get("MAIPO_API_KEY")
        except Exception:  # fuera de Colab, o sin el secreto creado
            pass
    if not _llave:
        _llave = getpass.getpass("Llave del equipo (sk-maipo-...): ").strip()
    return _llave


def _pedir(metodo: str, ruta: str, cuerpo: dict | None = None) -> dict:
    global _llave
    req = urllib.request.Request(
        f"{URL}{ruta}",
        method=metodo,
        data=json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None,
        headers={
            "Authorization": f"Bearer {_llave_api()}",
            "X-Session-Id": _sesion,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180, context=_SSL) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            _llave = None  # la próxima llamada la vuelve a pedir
            raise RuntimeError(f"Llave rechazada ({e.code}). Revisa la llave y vuelve a intentarlo.") from None
        raise RuntimeError(f"El router respondió {e.code}: {e.read().decode('utf-8', 'replace')[:300]}") from None


def _comando(nombre: str, texto: str) -> str:
    """Arma el mensaje igual que OpenCode: cuerpo del comando sin frontmatter y $ARGUMENTS reemplazado."""
    cuerpo = (AQUI / ".opencode" / "command" / f"{nombre}.md").read_text(encoding="utf-8")
    if cuerpo.startswith("---\n"):
        cuerpo = cuerpo.split("---\n", 2)[2].lstrip("\n")
    return cuerpo.replace("$ARGUMENTS", texto)


def _resumen(df) -> str:
    if df is None:
        return ""
    return f"\n\nResumen de mis datos ({df.shape[0]} filas × {df.shape[1]} columnas):\n{df.describe(include='all').T.to_string()}"


def _mostrar(texto: str) -> None:
    try:
        from IPython.display import Markdown, display

        display(Markdown(texto))
    except ImportError:
        print(texto)


def _enviar(texto: str) -> None:
    mensajes = [SISTEMA, *_historial, {"role": "user", "content": texto}]
    datos = _pedir("POST", "/chat/completions", {"model": "maipo-auto", "messages": mensajes})
    respuesta = datos["choices"][0]["message"].get("content") or ""
    _historial.extend([{"role": "user", "content": texto}, {"role": "assistant", "content": respuesta}])
    _mostrar(respuesta)


def preguntar(texto: str, df=None) -> None:
    """Pregunta libre: código, gráficos, errores. `df` adjunta un resumen de la tabla."""
    _enviar(texto + _resumen(df))


def explorar(texto: str = "", df=None) -> None:
    """Mentor de física: hipótesis antes de programar."""
    _enviar(_comando("explorar", texto) + _resumen(df))


def auditar(texto: str = "") -> None:
    """Auditor de método: pega tu código o tus resultados."""
    _enviar(_comando("auditar", texto))


def nueva() -> None:
    """Olvida la conversación y empieza una sesión nueva (más barato si cambias de tema)."""
    global _sesion
    _historial.clear()
    _sesion = uuid.uuid4().hex
    print("Conversación nueva.")


def saldo() -> None:
    """Muestra el presupuesto del equipo. También sirve para comprobar que la llave funciona."""
    b = _pedir("GET", "/budget")
    print(f"Equipo {b['team_name']}: quedan US$ {b['remaining_usd']:.2f} de {b['budget_usd']:.2f}.")
