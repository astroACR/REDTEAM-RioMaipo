# Convierte los notebooks a .md + .png (formatos que acepta NotebookLM) en la carpeta notebooklm/
import base64, json, re
from pathlib import Path

SALIDA = Path("notebooklm")
SALIDA.mkdir(exist_ok=True)

for nb_path, nivel in [("nivel1.ipynb", "nivel1"), ("nivel2.ipynb", "nivel2"), ("nivel 3 hackathon.ipynb", "nivel3")]:
    nb = json.loads(Path(nb_path).read_text(encoding="utf-8"))
    md = [f"# {nivel} — exportado de `{nb_path}`\n"]
    for i, celda in enumerate(nb["cells"]):
        src = "".join(celda["source"])
        if celda["cell_type"] == "markdown":
            md.append(src + "\n")
            continue
        md.append(f"```python\n{src}\n```\n")
        for out in celda.get("outputs", []):
            data = out.get("data", {})
            if "image/png" in data:
                titulo = (re.findall(r'suptitle\(\s*f?["\']([^"\']+)', src)  # título general de la figura primero
                          or re.findall(r'(?:set_title\(|title=)\s*f?["\']([^"\']+)', src))
                titulo = titulo[0] if titulo else "grafico"
                nombre = f"{nivel}_celda{i:02d}_{re.sub(r'[^0-9A-Za-zÁÉÍÓÚáéíóúñÑ]+', '_', titulo)[:60].strip('_')}.png"
                (SALIDA / nombre).write_bytes(base64.b64decode(data["image/png"]))
                md.append(f"**[Figura: `{nombre}` — {titulo}]**\n")
            elif out.get("output_type") == "stream":
                md.append("Resultado:\n```\n" + "".join(out["text"]) + "\n```\n")
            elif "text/plain" in data:
                md.append("Resultado:\n```\n" + "".join(data["text/plain"]) + "\n```\n")
            elif out.get("output_type") == "error":
                md.append(f"ERROR: {out.get('ename')}: {out.get('evalue')}\n")
    (SALIDA / f"{nivel}.md").write_text("\n".join(md), encoding="utf-8")

print(*sorted(p.name for p in SALIDA.iterdir()), sep="\n")
