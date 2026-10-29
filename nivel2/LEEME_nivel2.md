# Nivel 2: ¿qué tributario trae el sedimento?

El río Maipo llega a El Manzano con el agua de dos ramas: el Maipo alto (medido en San Alfonso) y el río Colorado.
La pregunta es: ¿cuál de las dos aporta más sedimento? ¿Y qué subcuencas, aunque no tengan medición, deberían aportar más?

Este nivel usa el CSV del nivel 1 y le suma dos archivos:

```python
import pandas as pd
n1 = pd.read_csv("nivel1/nivel1_manzano.csv", parse_dates=["fecha"])
n2 = pd.read_csv("nivel2/nivel2_tributarios.csv", parse_dates=["fecha"])
df = n1.merge(n2, on="fecha")
sub = pd.read_csv("nivel2/subcuencas.csv")
```

## `nivel2_tributarios.csv`: una fila por día, del 2000 al 2026

Se agregan los tributarios para poder repartir entre ellos el agua y el sedimento que llegan a El Manzano.

| Columna | Unidad | Descripción | Por qué se agrega |
|---|---|---|---|
| `fecha` | AAAA-MM-DD | Día | Para unir con el nivel 1 |
| `q_colorado_m3s` | m³/s | Caudal del río Colorado antes de juntarse con el Maipo | Agua que aporta el Colorado |
| `ssc_colorado_mgL` | mg/L | Sedimento medido en el Colorado (2003–2010) | Sedimento que aporta el Colorado |
| `q_san_alfonso_m3s` | m³/s | Caudal del Maipo en San Alfonso (hasta 2017) | Agua que aporta el Maipo alto |
| `ssc_san_alfonso_mgL` | mg/L | Sedimento medido en San Alfonso (2003–2005) | Sedimento que aporta el Maipo alto |
| `q_olivares_m3s` | m³/s | Caudal del río Olivares (rama del Colorado) | Para el ranking, sin sedimento |
| `q_colorado_alto_m3s` | m³/s | Caudal del Colorado antes de juntarse con el Olivares | Para el ranking, sin sedimento |
| `q_volcan_m3s` | m³/s | Caudal del río Volcán (rama del Maipo alto) | Para el ranking, sin sedimento |
| `p_colorado_mm` | mm | Precipitación del día sobre la cuenca del Colorado | Comparar la lluvia de cada rama |
| `p_liq_colorado_mm` | mm | Lluvia líquida sobre la cuenca del Colorado | Igual que `p_liq_mm` del nivel 1 |
| `p_san_alfonso_mm` | mm | Precipitación del día sobre la cuenca de San Alfonso | Comparar la lluvia de cada rama |
| `p_liq_san_alfonso_mm` | mm | Lluvia líquida sobre la cuenca de San Alfonso | Igual que `p_liq_mm` del nivel 1 |

## `subcuencas.csv`: una fila por subcuenca (12)

| Columna | Unidad | Descripción |
|---|---|---|
| `subcuenca_id` | texto | Nombre corto |
| `nombre` | texto | Nombre completo |
| `tipo` | texto | `cuenca`: todo lo que drena a una estación. `residual`: solo el trozo entre estaciones |
| `drena_a` | texto | Subcuenca a la que entrega su agua (la que la contiene) |
| `area_km2` | km² | Área |
| `elev_media_m` | m | Altura media |
| `pend_media_deg` | grados | Pendiente media |
| `pct_glaciar` | % | Parte del área cubierta por glaciares |
| `pct_area_sobre_4000m` | % | Parte del área sobre 4.000 m |
| `geologia` | texto | Roca principal |
| `tiene_ssc` | 0/1 | 1 si tiene sedimento medido desde el 2000 |

Ojo: las subcuencas están unas dentro de otras. El Manzano las contiene a todas.
Para no contar dos veces, usa las que entregan directo a la misma (por ejemplo, las tres con `drena_a = colorado_maipo`).

## Mini guía: ranking de subcuencas

1. Calcula la carga de sedimento de cada estación en toneladas por día: `0.0864 * q * ssc`.
2. Pásala a rendimiento: el promedio diario × 365, dividido por el área. Queda en t/km²/año.
3. Compara el rendimiento con la pendiente, el % glaciar y el % del área sobre 4.000 m.
4. Propón un ranking para las subcuencas sin sedimento medido. Ojo con el caudal por km² de Olivares, Colorado alto y Volcán: hay centrales hidroeléctricas que captan agua antes de esas estaciones, así que miden menos agua de la que produce la cuenca.
5. Discute qué tan seguro es: cuántos días hay y si se usan los mismos días en todas las estaciones.

## Mini guía: primer modelo de ML

1. Une los dos CSV y quédate con los días que tienen `ssc_mgL`.
2. Objetivo: 1 si `ssc_mgL` supera su percentil 95, 0 si no.
3. Separa por tiempo, nunca al azar: entrena con 2000–2012 y prueba con 2013–2018.
4. Variables: caudales, lluvia líquida, `iso0_m`, `t_media_C` y el mes. No uses el sedimento de ningún día como variable.
5. Mide con PR-AUC (`sklearn.metrics.average_precision_score`). Compárala con una regla simple: ordenar los días por `p_liq_48h_mm`.

## Logrado

- Usando solo los días en que hay sedimento medido en El Manzano y en el Colorado, mostrar que el Colorado aporta cerca de la mitad del sedimento con solo un cuarto del agua.
- Calcular el rendimiento de las 3 estaciones con sedimento y mostrar que el del Colorado es el más alto.
- Un ranking de las subcuencas sin sedimento medido, justificado con sus atributos.
- Un modelo simple que, en 2013–2018, supere en PR-AUC a la regla de `p_liq_48h_mm`. Explicar qué variables pesan más y por qué el modelo no funciona igual en verano que en invierno.
