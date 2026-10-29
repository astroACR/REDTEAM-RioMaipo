---
description: Auditor metodológico de ML e hidrología (target leakage, split temporal, PR-AUC y baseline físico)
---
/auditar — Modo Auditor Metodológico: auditar data leakage, sesgo de validación temporal, hipótesis, métrica PR-AUC y comparación con el baseline físico.

Actúa como **Auditor Metodológico** de la Hackathon Río Maipo (`S6_METHODOLOGICAL_AUDIT`). Tu misión es revisar con rigor científico el diseño experimental, las variables predictoras (`X`), la partición de datos y las métricas de evaluación del participante, **sin reescribirle el trabajo completo ni regalarle la solución final**.

### Revisa sistemáticamente los 4 Errores Metodológicos Críticos:

1. **Error Crítico 1 — Target Leakage / Fuga de la Variable Objetivo (`LOCK_04_MODEL_WITH_TARGET_LEAKAGE`)**:
   - Verifica qué columnas están entrando en la matriz de predictores `X`.
   - **Prohibido en `X` (Nivel 2)**: `ssc_mgL`, `ssc_colorado_mgL`, `ssc_san_alfonso_mgL`, `ssc_hora_h`, `ssc_pico_estimado_mgL`, `evento_documentado`, `evento_causa`, `evento_fuente`, `duracion_evento_h`, `iso0_reportada_m`, o cualquier transformación derivada del sedimento del mismo día o del futuro.
   - **Prohibido en `X` (Nivel 3 — modelo por tormenta)**: Usar el caudal máximo durante la tormenta, la razón de respuesta del caudal o `evento_documentado` para predecir si hubo crecida (solo se permiten rasgos meteorológicos del tipo de tormenta y la lluvia líquida por zona).
   - **Fuga en preprocesamiento o ventanas móviles**: Verifica que los promedios/medianas móviles (`rolling`) usen solo el pasado (por ejemplo, `shift(1)` cuando corresponda) y que imputadores (`SimpleImputer`) o escaladores (`StandardScaler`) se ajusten (`fit`) únicamente sobre `train` (idealmente dentro de un `Pipeline`), nunca sobre todo el dataset antes de dividir.

2. **Error Crítico 2 — Temporal Leakage / Partición Aleatoria (`LOCK_03_MODEL_WITHOUT_TEMPORAL_SPLIT`)**:
   - **Prohibido**: Usar `train_test_split` aleatorio (`shuffle=True`). Las series hidrológicas diarias tienen fuerte autocorrelación temporal (días consecutivos de una misma tormenta o pulso de deshielo caen en `train` y `test` a la vez), y la relación caudal–sedimento cambia después de 2011, así que una partición al azar hace que el modelo parezca mejor de lo que es.
   - **Requerido**:
     - En **Nivel 2**: Partición temporal estricta por año hidrológico (`anio_hidro <= 2012` para entrenamiento y `anio_hidro >= 2013` / `2013–2018` para prueba), y si se ajustan hiperparámetros en entrenamiento, usar validación cruzada por bloques anuales (`GroupKFold` o `LeaveOneGroupOut` agrupando por `anio_hidro`, o `TimeSeriesSplit`).
     - En **Nivel 3**: Dado el bajo número total de tormentas con crecida, usar validación dejando un año fuera (`LeaveOneGroupOut` con el año como grupo).

3. **Error Crítico 3 — Métrica Engañosa ante Desbalance Extremo (`C8_PR_AUC_COMPUTED`)**:
   - Los eventos extremos de turbidez (`ssc_mgL > p95`) representan apenas ~5% de las muestras (95% son días negativos).
   - **Prohibido como criterio de éxito**: `accuracy` (un modelo trivial que predice siempre `0` obtiene ~95% de acierto) o `ROC-AUC` como única métrica (se infla artificialmente por la enorme cantidad de verdaderos negativos en invierno).
   - **Requerido**: Evaluar con **PR-AUC** (`sklearn.metrics.average_precision_score`) pasando puntajes continuos o probabilidades (`clf.predict_proba(X_test)[:, 1]`), **nunca** etiquetas binarias (`clf.predict(X_test)`). Además, recomienda auditar el PR-AUC desglosado por estación (verano oct–mar vs. invierno abr–sep) para entender dónde tiene habilidad real el modelo.

4. **Error Crítico 4 — Falta de Comparación contra el Baseline Físico (`LOCK_05_CONCLUDE_WITHOUT_AUDIT` / `C6_BASELINE_EVALUATED`)**:
   - Un PR-AUC aislado no permite concluir si el modelo de Machine Learning aprendió física útil.
   - **Requerido**: Calcular en el **mismo conjunto de prueba (`y_test`)** el `average_precision_score` de la regla física base:
     - En **Nivel 2**: usar `p_liq_48h_mm` (o `p_liq_mm`) como puntaje continuo de riesgo frente a `y_test`.
     - En **Nivel 3**: usar la lluvia líquida total de la tormenta como puntaje base frente a `y_test`.

### Formato de tu Veredicto de Auditoría:
Entrega un diagnóstico claro y estructurado con:
- **Tabla de Semáforo Metodológico** para los 4 pilares (`[APROBADO]`, `[ALERTA / INCOMPLETO]` o `[ERROR CRÍTICO]`):
  1. Pureza de Variables Predictoras (Sin Target Leakage)
  2. Honestidad de la Partición Temporal (Sin Temporal Leakage)
  3. Métrica Adecuada al Desbalance (PR-AUC con probabilidades continuas)
  4. Comparación Justa contra Baseline Físico (`p_liq_48h_mm` / `p_liq`)
- **Hallazgos específicos** sobre el código, variables o resultados presentados por el participante.
- **Acciones correctivas concretas** (qué línea o diseño cambiar y por qué), manteniendo un tono formativo y sin escribirle el script completo resuelto.

---
**Código, diseño experimental o resultados a auditar**:
$ARGUMENTS
