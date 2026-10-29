# Guía Rápida del Participante — Hackathon Río Maipo

¡Bienvenido/a a la **Hackathon Río Maipo**! El desafío consiste en explorar, explicar físicamente y predecir los eventos extremos de turbidez / sedimento en suspensión (`SSC`) en el **Río Maipo en El Manzano**, que abastece cerca del **70% del agua potable de Santiago**.

---

## 1. Configuración (`OpenCode`)

> **¿No quieres instalar nada?** Usa Google Colab: mira la sección 1b. Si la instalación se complica más de 10 minutos, pásate a Colab y sigue trabajando.

### Qué necesitas instalar (solo la primera vez)

| Programa | Para qué | Dónde se descarga |
|---|---|---|
| **Python 3** | Correr el código de los niveles | https://www.python.org/downloads/ (en Windows, marca **"Add python.exe to PATH"** al instalar) |
| **Node.js LTS** | Instalar OpenCode con `npm` (solo Windows) | https://nodejs.org/es |
| **OpenCode** | El asistente | Paso 1, más abajo (guía oficial: https://opencode.ai/docs) |
| **Windows Terminal** | Una terminal moderna (solo Windows 10; Windows 11 ya la trae) | https://aka.ms/terminal |

### Paso 1: Instala OpenCode

**Windows (PowerShell):**
```powershell
npm install -g opencode-ai
```
- Si `npm` no se reconoce, instala Node.js LTS (tabla de arriba), cierra la terminal y abre otra.
- Si aparece *"la ejecución de scripts está deshabilitada en este sistema"*, ejecuta `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.
- Otras formas: `scoop install opencode` (https://scoop.sh) o `choco install opencode` (https://chocolatey.org/install).

**macOS / Linux:**
```bash
curl -fsSL https://opencode.ai/install | bash
export PATH="$HOME/.opencode/bin:$PATH"
```
- La segunda línea hace que esta terminal encuentre `opencode` sin tener que abrir otra.
- **No uses `brew install opencode`:** instala OpenCode 2, cuya configuración no es compatible con este kit.

**Comprueba:** `opencode --version` debe mostrar una versión que empiece con **1.**

### Paso 2: Descomprime el kit

- **Windows:** clic derecho en `maipo-starter-kit.zip` → **Extraer todo**. Windows deja una carpeta dentro de otra (`maipo-starter-kit\maipo-starter-kit\`): trabaja en **la de adentro**, la que muestra `AGENTS.md` y `opencode.json`.
- **macOS:** doble clic en el zip.

### Paso 3: Abre una terminal en esa carpeta

- **Windows 11:** clic derecho en un espacio vacío de la carpeta → **Abrir en Terminal**.
- **Windows 10:** escribe `powershell` en la barra de direcciones del Explorador y presiona Enter.
- **macOS:** abre la Terminal, escribe `cd ` (con un espacio al final), arrastra la carpeta a la ventana y presiona Enter.

**Comprueba:** `dir` (Windows) o `ls` (macOS) debe mostrar `AGENTS.md` y `opencode.json`.

> Si abres OpenCode en otra carpeta, no verá `/explorar` ni `/auditar` ni se conectará al asistente de la hackathon, **y no te avisará**.

### Paso 4: Instala las librerías de Python

- **Windows:** `py -m pip install -r requirements.txt` (si `py` no se reconoce, usa `python -m pip install -r requirements.txt`).
- **macOS / Linux:** `python3 -m pip install -r requirements.txt`. Si aparece `externally-managed-environment`, primero crea un entorno con `python3 -m venv .venv && source .venv/bin/activate` y repite.

### Paso 5: Pon la llave de tu equipo (cada vez que abras una terminal)

- **Windows (PowerShell):** `$env:MAIPO_API_KEY="sk-maipo-TU_LLAVE_AQUI"`
- **macOS / Linux:** `export MAIPO_API_KEY="sk-maipo-TU_LLAVE_AQUI"`

La llave vale solo en esa ventana: si abres otra, repite este paso.

> La llave es solo de tu equipo: no la escribas en notebooks, en el código ni en un repositorio.

### Paso 6: Abre OpenCode

```
opencode
```

**Comprueba:** al escribir `/` deben aparecer `explorar` y `auditar`. Si no aparecen, la terminal no está en la carpeta del kit (vuelve al paso 3).

## 1b. Sin instalar nada: Google Colab

1. Abre `inicio.ipynb` en Colab.
2. Corre la celda 1: trae el kit (si te lo pide, sube `maipo-starter-kit.zip`).
3. Corre la celda 2: te pide la llave en un campo oculto y muestra el saldo de tu equipo.
4. Conversa desde cualquier celda con `explorar("...")`, `preguntar("...")` y `auditar("...")`: es el mismo asistente y los mismos comandos que en OpenCode, pero no ejecuta código; copia lo que te proponga en una celda.

## 1c. Material de apoyo

- `referencias/`: tesis de Bustos (2011), eventos de turbiedad en la prensa (2008–2026) y enlaces a los papers de Vergara.
- Saldo de tu llave:
  - **Windows (PowerShell):** `curl.exe -s -H "Authorization: Bearer $env:MAIPO_API_KEY" https://maipo-router-1095563500960.southamerica-west1.run.app/v1/budget`
  - **macOS / Linux:** `curl -s -H "Authorization: Bearer $MAIPO_API_KEY" https://maipo-router-1095563500960.southamerica-west1.run.app/v1/budget`
  - **Colab:** `saldo()`

---

## 2. Los 3 Niveles del Desafío

Avanza en orden. Cada carpeta contiene un archivo `LEEME_nivelN.md` con la pregunta, la tabla de columnas, una mini guía paso a paso y los criterios de **Logrado**:

| Nivel | Carpeta y Archivos | Objetivo Principal |
|---|---|---|
| **Nivel 1 (Básico)** | `nivel1/LEEME_nivel1.md`<br>`nivel1/nivel1_manzano.csv` | Entender el ciclo anual en El Manzano: lluvia líquida bajo la isoterma 0 °C (`iso0_m`, `p_liq_48h_mm`) en invierno vs. saltos de caudal por deshielo sin lluvia en verano. |
| **Nivel 2 (Intermedio)** | `nivel2/LEEME_nivel2.md`<br>`nivel2/nivel2_tributarios.csv`<br>`nivel2/subcuencas.csv` | Demostrar qué tributario aporta más sedimento (Río Colorado vs. San Alfonso), armar un ranking de subcuencas sin medición de `SSC` y entrenar tu primer modelo de ML que supere a la regla física en **PR-AUC**. |
| **Nivel 3 (Legendario)** | `nivel3/LEEME_nivel3.md`<br>`nivel3/nivel3_tormentas.csv`<br>`nivel3/zonas.csv` | Anatomía de las tormentas de invierno: ríos atmosféricos (`pw_mm`, `ivt_mms`), tormentas cálidas, distribución espacial en las 8 zonas cordilleranas, efecto de El Niño (`oni`) y modelo por tormenta. |

---

## 3. Tus Dos Comandos Especiales en OpenCode (`/explorar` y `/auditar`)

Dentro de `opencode`, además de pedir código en Python con `pandas` y `scikit-learn`, tienes dos comandos diseñados para ayudarte a ganar:

- **`/explorar <tu pregunta o hipótesis>`** *(Mentor Hidrometeorológico)*:
  Úsalo para entender la física de la cuenca antes de programar: cómo actúa la isoterma 0 °C, por qué el deshielo de verano domina los picos de las 08:00 h, por qué el Río Colorado arrastra tanto sedimento o cómo formular hipótesis verificables en `pandas`.
  - *Ejemplo*: `/explorar ¿por qué la muestra de las 08:00 h ve los eventos de deshielo de verano pero casi no ve las tormentas de invierno?`

- **`/auditar <tu código o resultados>`** *(Auditor Metodológico)*:
  Úsalo cuando tengas listo tu modelo de Machine Learning para verificar que no tengas errores que invaliden tu puntaje ante el jurado:
  1. **Sin Target Leakage**: No usar columnas de sedimento (`ssc_*`) ni de eventos (`evento_documentado`, `evento_causa`) dentro de `X`.
  2. **Partición Temporal Honesta**: Separar por año hidrológico (`2000–2012` entrenamiento, `2013–2018` prueba en Nivel 2, o `LeaveOneGroupOut` en Nivel 3); nunca usar `train_test_split` aleatorio.
  3. **Métrica PR-AUC**: Evaluar con `average_precision_score` usando probabilidades continuas (`predict_proba`), no `accuracy` ni `ROC-AUC`.
  4. **Comparación con el Baseline Físico**: Comparar siempre el PR-AUC de tu modelo contra la regla base de lluvia líquida (`p_liq_48h_mm`).
  - *Ejemplo*: `/auditar revisa nuestro script de entrenamiento del nivel 2 y dinos si cumplimos las 4 reglas metodológicas`
