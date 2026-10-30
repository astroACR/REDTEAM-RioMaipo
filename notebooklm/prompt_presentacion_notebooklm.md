# Prompt para NotebookLM — Presentación pitch Hackathon Río Maipo

> **Fuentes que debes cargar en NotebookLM antes de pegar el prompt:**
> `nivel1/LEEME_nivel1.md`, `nivel2/LEEME_nivel2.md`, `nivel3/LEEME_nivel3.md`, `.opencode/command/auditar.md`
> y los tres notebooks **ejecutados** exportados a PDF o HTML (`nivel1.ipynb`, `nivel2.ipynb`, `nivel 3 hackathon.ipynb`), para que NotebookLM vea los gráficos.

---

## PROMPT (copiar desde aquí)

Actúa como diseñador/a de presentaciones científicas y redactor/a de pitch. Crea una presentación en español, de **13 diapositivas**, para el jurado de la **Hackathon Río Maipo**. El tema es la detección temprana y la comprensión física de los eventos de turbiedad (sedimento en suspensión, SSC) del Río Maipo en El Manzano (estación DGA 05710001), que abastece cerca del 70 % del agua potable del Gran Santiago.

### Reglas de contenido (obligatorias)

1. **Solo números de las fuentes.** Usa exclusivamente las cifras de la "Hoja de datos verificados" de abajo, que salen de los outputs ejecutados de los notebooks. No inventes ni redondees de otra forma. Si un texto markdown de un notebook dice otro número que un output, manda el output (y la hoja de datos de abajo).
2. **Una idea por diapositiva.** Título = la conclusión en una frase (por ejemplo, "El Colorado trae la mitad del sedimento con un cuarto del agua"), no el tema ("Resultados Nivel 2").
3. **Cada hallazgo se demuestra con un gráfico del notebook.** Usa solo los gráficos de la lista "Gráficos a usar". Pon un recuadro marcador con el título exacto del gráfico, para insertarlo a mano: `[GRÁFICO: Nivel N — "título exacto"]`. Donde no hay gráfico, usa un KPI grande o una tabla mínima con los números dados.
4. **Explica la física, no solo la métrica.** Cada diapositiva lleva una línea "¿Por qué?" con el mecanismo físico (isoterma 0 °C, lluvia líquida frente a nieve, deshielo, río atmosférico, sedimento glaciar).
5. **Honestidad.** Cuando un hito se cumple con matiz, dilo en la misma diapositiva (marca "✓ con matiz"). Un jurado técnico premia que se reconozcan los límites.
6. **Texto mínimo.** Como máximo 3 bullets por diapositiva y 12 palabras por bullet. El detalle va en las notas del orador (2–4 frases por diapositiva).
7. **Criterios del Auditor Metodológico.** Los modelos se presentan según las 4 Reglas de Oro de `auditar.md`: (1) sin fuga del objetivo (target leakage), (2) partición temporal honesta, (3) PR-AUC con probabilidades continuas, nunca accuracy, (4) comparación con el baseline físico en el mismo conjunto de prueba. Nunca muestres accuracy ni ROC-AUC.

### Estructura del pitch

| # | Diapositiva | Contenido | Evidencia |
|---|---|---|---|
| 1 | **Portada / gancho** | "Cuando el Maipo se enturbia, Santiago se queda sin agua." Nombre del equipo y del reto. | KPI: ~70 % del agua potable de Santiago |
| 2 | **El problema** | Dos causas de turbiedad: tormentas cálidas de invierno y deshielo de verano. Una sola muestra al día, a las 08:00, pierde los picos breves. | Ícono o esquema simple: invierno 🌧 / verano ☀ |
| 3 | **Nuestro enfoque** | Tres niveles: (1) ¿cuándo? → (2) ¿de dónde? → (3) ¿qué tormenta? Física primero, ML después, auditado. | Línea de tiempo de 3 pasos |
| 4 | **N1 · Dos regímenes** | En invierno manda la lluvia, pero en junio solo el 35 % cae líquida. En verano manda el deshielo: caudal y SSC se disparan en dic–ene. | `[GRÁFICO: Nivel 1 — "Ciclo anual en El Manzano (2000–2018)"]` |
| 5 | **N1 · Isoterma y saltos** | Con lluvia, P(SSC>p95) sube con `iso0_m` (en verano). Un salto de caudal sin lluvia da ~3× más días extremos. | `[GRÁFICO: Nivel 1 — "Probabilidad de sedimento extremo según la isoterma 0 °C"]` + `[GRÁFICO: Nivel 1 — "Verano sin lluvia: deshielo con y sin salto de caudal"]` |
| 6 | **N1 · Regla de alerta** | `p_liq_48h_mm ≥ 30 mm` acierta 13 de 16 eventos (meta ≥ 11). Fuera de muestra: 10/16. | KPI grande "13/16" en verde, "10/16 fuera de muestra" en gris |
| 7 | **N2 · El Colorado manda** | 24,8 % del agua → 49,1 % del sedimento. | `[GRÁFICO: Nivel 2 — "Aporte del río Colorado"]` |
| 8 | **N2 · Rendimiento y ranking** | El Colorado tiene el mayor rendimiento (794 t/km²/año). A más área sobre 4.000 m, más sedimento → ranking: Olivares, Colorado alto, Volcán… | `[GRÁFICO: Nivel 2 — "Más área sobre 4.000 m → más sedimento por km²"]` |
| 9 | **N2 · Modelo ML vs regla** | Random Forest: PR-AUC 0,120 frente a 0,035 de la regla (azar 0,041). Gana en verano, pierde en invierno. | `[GRÁFICO: Nivel 2 — "Curva precisión-recall"]` + `[GRÁFICO: Nivel 2 — "Desempeño por temporada"]` |
| 10 | **N2 · ¿Qué aprendió?** | Pesan mes y temperatura (deshielo), no caudal. Desde 2011 el mismo caudal trae mucho más sedimento. | `[GRÁFICO: Nivel 2 — "Importancia de variables (validación dentro de train)"]` |
| 11 | **N3 · Anatomía de la tormenta** | Las 16 crecidas fueron ríos atmosféricos: 16/89 contra 0/226. 7 de las 10 mayores respuestas son eventos documentados. La lluvia líquida de las crecidas se concentra en las zonas bajas (manzano_local 2,10× su área). | Barra simple con 18 % frente a 0 % + `[GRÁFICO: Nivel 3 — "Área de cada zona vs. fracción de lluvia líquida en tormentas con crecida"]` |
| 12 | **Auditoría metodológica** | Semáforo de las 4 Reglas de Oro para N2 y N3 (ver datos). Modelo N3: 0,818 frente a 0,790, IC incluye 0 → "rinde igual que la regla física". | Tabla semáforo |
| 13 | **Cierre / impacto** | 3 mensajes y próximos pasos: alerta por río atmosférico + lluvia líquida en invierno, modelo de deshielo en verano, muestreo de alta frecuencia en tormentas. | KPI resumen + llamada a la acción |

Extra opcional (solo si cabe en la diapositiva 11 o 13, en una línea): los inviernos El Niño muestran más crecidas por invierno (1,33 frente a 0,47 neutros y 0,50 La Niña), pero con solo 3 inviernos El Niño **no es concluyente**.

### Gráficos a usar (y los que se omiten a propósito)

- **Usar:** N1 ciclo anual · N1 isoterma · N1 saltos de caudal · N2 aporte del Colorado · N2 rendimiento vs área sobre 4.000 m · N2 curva PR · N2 desempeño por temporada · N2 importancia de variables · N3 zonas vs lluvia líquida.
- **Omitir:** N1 "Eventos SSC > p95 en días con lluvia" (señal débil, n=33) · N2 "Rendimiento de sedimento por estación" (redundante con el de altura) · N2 "Ranking de subcuencas" en barras (incluido en el de altura) · N2 "Caudal específico" (trampa de captaciones: va solo en notas) · N2 "Riesgo por mes" (las notas del orador lo cubren).

### Hoja de datos verificados (usar tal cual)

**Nivel 1 — El Manzano 2000–2018**
- Junio: 7,12 mm/día de precipitación, solo 2,51 mm/día líquida (35 %). Isoterma mediana de ~3.020–3.030 m en jul–ago y ~4.350 m en enero.
- Caudal mediano: 55–66 m³/s en invierno, 160 m³/s en enero. SSC mediana: 67–128 mg/L en invierno, 873 mg/L en diciembre.
- p95 global de SSC = 1.603 mg/L. En verano, con lluvia, P(SSC>p95) sube de 2,5 % (isoterma 2.500–3.000 m) a 37,5 % (5.000–5.500 m). En invierno la curva es plana: la muestra de las 08:00 pierde los picos.
- Verano seco: un día con salto tiene 29,9 % de días extremos, frente a 10,3 % sin salto (2,9×).
- Regla `p_liq_48h_mm`: 16 episodios documentados (abr–sep 2000–2018). Con 30 mm acierta 13/16, con 35 alarmas. Con el umbral elegido dejando un año fuera, 10/16. Solo 1 de los 16 se ve sobre p95 en la muestra de las 08:00.
- Estado de hitos: ciclo anual ✓ · isoterma ✓ con matiz (solo en verano) · saltos ✓ · regla ≥ 11/16 ✓ con matiz.

**Nivel 2 — Tributarios y ML**
- 1.124 días comunes (2003–2010): el Colorado aporta 24,8 % del agua y 49,1 % del sedimento.
- Rendimiento con todos los días (t/km²/año): Colorado 794, Manzano 391, San Alfonso 256. Con los 356 días comunes: 963 / 622 / 291. El Colorado es el mayor en ambos. % del área sobre 4.000 m: 29,3 / 16,5 / 11,2.
- Ranking sin SSC (7 unidades sin solape, suman el área de El Manzano): 1 Olivares (39,4 % sobre 4.000 m, 14,3 % glaciar), 2 Colorado alto (34,8 %), 3 Volcán (18,6 %), 4 Yeso residual, 5 Melosas, 6 Colorado bajo, 7 Manzano local.
- Modelo: RandomForest (500 árboles, min_samples_leaf=5). Train `anio_hidro ≤ 2012`, test 2013–2018. Umbral p95 calculado solo con train = 1.656 mg/L. 77 eventos de 1.900 días en test.
- PR-AUC test: modelo 0,120 · regla `p_liq_48h_mm` 0,035 · azar 0,041. Diferencia +0,086, IC 95 % por año [+0,022; +0,222]. Sin 2014: 0,093 frente a 0,027.
- Verano: modelo 0,130 · regla 0,069 · azar 0,079 (68 eventos). Invierno: modelo 0,011 · regla 0,017 · azar 0,009 (9 eventos). En invierno gana la regla física.
- Ablación (CV en train): todas 0,183; sin caudales 0,293; sin temperatura/isoterma 0,132. Test sin caudales: 0,140.
- Cambio post-2011: con 100–150 m³/s la SSC mediana pasa de 262 a 752 mg/L y P(>p95) de 2,5 % a 17,5 %.
- Pronóstico con datos de ayer: modelo 0,123 frente a 0,036 de la regla.

**Nivel 3 — Tormentas (abr–sep 2000–2026)**
- 346 tormentas; 334 con etiqueta; 16 crecidas (razón ≥ 3). Los 18 eventos documentados quedan asociados a una tormenta.
- Fracción de crecidas: río atmosférico 16/89 (18 %) frente a 0/226 · convectiva 14/55 (25,5 %) frente a 2/267 · cálida 12/204 (5,9 %) frente a 4/130 (3,1 %).
- Top 10 por respuesta: 7/10 son eventos documentados (meta ≥ 6). Máxima: junio 2023, razón 30,7.
- Lluvia líquida en crecidas frente al área: mayor aporte relativo en manzano_local (2,10×), menor en colorado_alto (0,42×).
- ONI (mayo–sep): 19 neutros, 4 La Niña, 3 El Niño. Crecidas por invierno: 0,47 / 0,50 / 1,33. Isoterma en días de lluvia: 2.965 / 2.686 / 2.927 m. No concluyente.
- Modelo (LogisticRegression en Pipeline con imputador y escalador ajustados por fold, LeaveOneGroupOut por año): PR-AUC 0,818 frente a 0,790 de la regla de lluvia líquida total. Diferencia +0,028, IC 95 % [−0,072; +0,118] → **no se distingue del baseline**. Con umbrales 2, 4 o 5 el modelo pierde.
- Las 8 lluvias zonales son casi la misma variable (correlación mediana 0,96): los coeficientes no se interpretan uno a uno.

**Semáforo de auditoría (diapositiva 12)**

| Regla de Oro | Nivel 2 | Nivel 3 |
|---|---|---|
| 1. Sin fuga del objetivo (target leakage) | 🟢 Ninguna columna `ssc_*` ni `evento_*` en X (assert en el código) | 🟢 Sin caudal, razón de respuesta ni `evento_documentado` en X |
| 2. Partición temporal | 🟢 Por `anio_hidro` (≤2012 / 2013–2018); GroupKFold por año para elegir el modelo | 🟢 LeaveOneGroupOut por año; preprocesamiento dentro del Pipeline |
| 3. PR-AUC con probabilidades | 🟢 `predict_proba` y desglose verano/invierno | 🟢 PR-AUC agrupada + bootstrap por año |
| 4. Contra el baseline físico | 🟢 Gana globalmente / 🔴 pierde en invierno | 🔴 No supera la regla de forma significativa |

### Diseño visual

- **Fondo blanco puro (#FFFFFF)** en todas las diapositivas. Mucho espacio en blanco y márgenes amplios.
- **Texto:** negro grafito (#111827) para títulos y gris (#6B7280) para el texto secundario. Una sola familia sans-serif geométrica moderna (Inter, Manrope o similar): títulos en negrita grande, cuerpo en peso regular.
- **Verde neón (#39FF14)** = lo que funciona: hito cumplido, el modelo gana, el KPI positivo. Úsalo en barras, subrayados, chips, bordes y números grandes, **no para texto pequeño** sobre blanco (contraste bajo). Para texto verde pequeño usa #16A34A.
- **Rojo (#FF2D55)** = riesgo y límites: evento extremo, el modelo pierde, limitación, "no concluyente".
- Los demás elementos van en grises neutros (#E5E7EB para líneas y fondos de tarjeta). Nada de degradados, sombras fuertes ni clipart.
- Cada nivel lleva un pequeño chip de color en la esquina ("NIVEL 1 · ¿Cuándo?", "NIVEL 2 · ¿De dónde?", "NIVEL 3 · ¿Qué tormenta?") para que el jurado se ubique.
- Los gráficos se ven grandes (≥ 60 % de la diapositiva), con la conclusión resaltada en verde o rojo junto al gráfico.
- La retícula y la posición del título son iguales en todas las diapositivas: un diseño armónico y consistente.

### Entrega

Para cada diapositiva entrega: **título-conclusión**, **bullets** (≤ 3), **evidencia** (marcador de gráfico o KPI), **color de highlight** (verde/rojo) y **notas del orador**.
