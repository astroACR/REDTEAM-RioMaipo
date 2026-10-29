# Instrucciones del Proyecto — Hackathon Río Maipo (OpenCode)

Estás asistiendo a un equipo de estudiantes en la **Hackathon Río Maipo** (detección temprana y comprensión física de eventos extremos de turbidez y sedimento en suspensión `SSC` en el **Río Maipo en El Manzano**, estación DGA `05710001`, que abastece ~70% del agua potable del Gran Santiago).

---

## 1. Estructura de Datos y Niveles del Desafío

El proyecto está organizado en **3 niveles progresivos**. Cada nivel tiene su enunciado (`LEEME_nivelN.md`) y sus archivos `.csv`:

- **Nivel 1 (`nivel1/`) — Exploración e intuición física en El Manzano**:
  - `nivel1/LEEME_nivel1.md`: Enunciado, diccionario de las 20 columnas, mini guía de saltos de caudal en verano y criterios de logrado.
  - `nivel1/nivel1_manzano.csv`: Serie diaria en El Manzano (2000–2026, 9.709 filas × 20 columnas).
- **Nivel 2 (`nivel2/`) — Tributarios, ranking de subcuencas y primer modelo ML**:
  - `nivel2/LEEME_nivel2.md`: Enunciado, mini guía de ranking de subcuencas, mini guía de Machine Learning y criterios de logrado.
  - `nivel2/nivel2_tributarios.csv`: Caudales, sedimento (`SSC`) y lluvia líquida en los tributarios (Río Colorado, Maipo en San Alfonso, Olivares, Colorado alto y Volcán). Se une por `fecha` con `nivel1/nivel1_manzano.csv`.
  - `nivel2/subcuencas.csv`: Atributos geomorfológicos, glaciares y geológicos de las 12 unidades hidrológicas (presta atención a `tipo` (`cuenca` vs `residual`) y `drena_a` para no contar áreas ni caudales dos veces).
- **Nivel 3 (`nivel3/`) — Anatomía de una tormenta en alta montaña**:
  - `nivel3/LEEME_nivel3.md`: Enunciado, catálogo de tormentas invernales, efecto de El Niño (`oni`) y modelo por tormenta con `LeaveOneGroupOut`.
  - `nivel3/nivel3_tormentas.csv`: Variables de radiosonda de Santo Domingo (`pw_mm`, `ivt_mms`, `t_700_C`, `ki_C`), índice `oni` y precipitación/lluvia líquida/temperatura en 8 zonas cordilleranas. Se une por `fecha` con los niveles 1 y 2.
  - `nivel3/zonas.csv`: Atributos de las 8 zonas sin solape que componen la cuenca de El Manzano.

> **Nota sobre rutas de archivos**: Si ejecutas scripts desde la raíz del proyecto, carga los CSVs usando sus rutas relativas con carpeta (`"nivel1/nivel1_manzano.csv"`, `"nivel2/nivel2_tributarios.csv"`, `"nivel2/subcuencas.csv"`, `"nivel3/nivel3_tormentas.csv"`, `"nivel3/zonas.csv"`).

- **Skill `datos-maipo`**: cobertura por columna (qué años tienen dato) y trampas de los datos. Cárgala antes de comparar estaciones o zonas.
- **`referencias/`**: tesis de Bustos (2011) y `prensa.es.md` (eventos de turbiedad 2008–2026). Son largas: búscalas con grep por fecha o palabra, no las leas enteras.

---

## 2. Flujo de Trabajo con Python y `pandas`

1. **Lectura directa de los CSVs**:
   - Todo el trabajo de exploración, limpieza, cruce de tablas y modelado se realiza en **Python** (`pandas`, `numpy`, `scikit-learn`, `matplotlib`) leyendo directamente los archivos `.csv` del proyecto.
2. **Inspeccionar antes de transformar o modelar (`S1_DATA_EXPLORATION` -> `C1_DATA_INSPECTED`)**:
   - Antes de crear features o entrenar cualquier modelo, inspecciona siempre los datos con `pd.read_csv(..., parse_dates=["fecha"])`, `.head()`, `.info()`, `.describe()` y verifica rangos de fechas y valores faltantes (`NaN`).
3. **Verificación ejecutable**:
   - Cuando escribas código Python para el participante, ejecútalo o verifica que no tenga errores (`Traceback`) y explica los resultados conectándolos con la física del Río Maipo.

---

## 3. Regla Pedagógica y Anti-Spoiler

- El objetivo de la hackathon es que los estudiantes **comprendan la física hidrometeorológica de la cuenca andina y aprendan buenas prácticas de ciencia de datos**.
- **Prohibido regalar soluciones mágicas sin contexto**: Construye las soluciones paso a paso junto al participante, explicando el porqué físico de cada filtro, umbral o transformación.
- **Nunca inventes datos ni hardcodees resultados**: Todo número o hallazgo debe provenir de cálculos reales ejecutados con `pandas` / `scikit-learn` sobre los CSVs del proyecto.

---

## 4. Cuándo Invocar las Skills Pedagógicas (`/explorar` y `/auditar`)

El entorno cuenta con dos comandos especializados que conectan con el **Mentor Hidrometeorológico** y el **Auditor Metodológico** (`Gemini 4 Argon`):

### A. `/explorar` — Mentor Hidrometeorológico (`S2_DOMAIN_GROUNDING`)
Recomienda al participante ejecutar `/explorar <pregunta o hipótesis>` (o aplica sus principios) cuando:
- Inicie un nuevo nivel y quiera entender los mecanismos físicos antes de programar.
- Necesite comprender el rol de la **isoterma 0 °C (`iso0_m`)**, la fracción de área pluvial (`frac_bajo_iso0`) y la diferencia entre nieve y lluvia líquida (`p_liq_mm`, `p_liq_48h_mm`).
- Quiera contrastar los dos regímenes de turbidez: **deshielo estival (nov–feb)** por saltos de caudal sin lluvia vs. **tormentas cálidas de invierno / ríos atmosféricos (`abr–sep`)**.
- Busque entender la **histéresis y agotamiento de sedimento**, por qué el **Río Colorado** aporta ~la mitad del sedimento con ~un cuarto del agua frente a **San Alfonso**, o cómo influye el **sesgo de muestreo discreto a las 08:00 h (`ssc_hora_h`)** (que captura bien los pulsos anchos de deshielo pero pierde los picos breves de las tormentas de invierno).

### B. `/auditar` — Auditor Metodológico (`S6_METHODOLOGICAL_AUDIT`)
Recomienda al participante ejecutar `/auditar <código, variables o resultados>` antes de dar por terminado un modelo de Machine Learning, y respeta siempre estas **4 Reglas de Oro Metodológicas**:

1. **Cero Target Leakage (`C5_NO_TARGET_LEAKAGE`)**:
   - **Jamás** incluyas dentro de las variables predictoras `X` columnas que contengan la respuesta o información futura: `ssc_mgL`, `ssc_colorado_mgL`, `ssc_san_alfonso_mgL`, `ssc_hora_h`, `ssc_pico_estimado_mgL`, `evento_documentado`, `evento_causa`, `evento_fuente`, `duracion_evento_h`, `iso0_reportada_m` (ni el caudal pico o `evento_documentado` en el modelo por tormenta del Nivel 3).
2. **Partición Temporal Honesta (`C4_TEMPORAL_SPLIT_SET`)**:
   - **Jamás** uses `train_test_split` aleatorio (`shuffle=True`).
   - En el **Nivel 2**, separa estrictamente por tiempo / año hidrológico (`anio_hidro <= 2012` para `train`, `2013–2018` para `test`) y usa `GroupKFold` por `anio_hidro` si ajustas hiperparámetros.
   - En el **Nivel 3**, usa `LeaveOneGroupOut` agrupando por año.
3. **Métrica Correcta ante Desbalance Extremo (`C8_PR_AUC_COMPUTED`)**:
   - Los eventos sobre el percentil 95 (`ssc_mgL > p95`) son solo ~5% de los días. No uses `accuracy` ni te fíes solo de `ROC-AUC`.
   - Evalúa siempre con **PR-AUC** (`sklearn.metrics.average_precision_score`) usando probabilidades continuas (`clf.predict_proba(X_test)[:, 1]`) y analiza la diferencia de desempeño entre verano (oct–mar) e invierno (abr–sep).
4. **Comparación Obligatoria con el Baseline Físico (`C6_BASELINE_EVALUATED`)**:
   - Antes de redactar conclusiones sobre un modelo, calcula en el mismo conjunto de prueba el `average_precision_score` de la regla física base (`p_liq_48h_mm` o `p_liq_mm` en Nivel 2; lluvia líquida total de la tormenta en Nivel 3) y verifica que tu modelo la supere.
