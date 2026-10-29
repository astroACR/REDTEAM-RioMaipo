# Nivel 3: anatomía de una tormenta

En invierno, algunas tormentas hacen crecer el río Maipo de golpe y otras pasan sin que se note.
La pregunta es: ¿qué tormentas hacen crecer el río, y por qué? ¿Por su tipo, por dónde cae la lluvia o por la altura de la isoterma 0 °C?
Extra: ¿El Niño las empeora?

Este nivel usa los CSV de los niveles 1 y 2 y les suma dos archivos:

```python
import pandas as pd
n1 = pd.read_csv("nivel1/nivel1_manzano.csv", parse_dates=["fecha"])
n2 = pd.read_csv("nivel2/nivel2_tributarios.csv", parse_dates=["fecha"])
n3 = pd.read_csv("nivel3/nivel3_tormentas.csv", parse_dates=["fecha"])
df = n1.merge(n2, on="fecha").merge(n3, on="fecha")
zonas = pd.read_csv("nivel3/zonas.csv")
```

## `nivel3_tormentas.csv`: una fila por día, del 2000 al 2026

| Columna | Unidad | Descripción | Por qué se agrega |
|---|---|---|---|
| `fecha` | AAAA-MM-DD | Día | Para unir con los niveles 1 y 2 |
| `q_hualtatas_m3s` | m³/s | Caudal del Maipo en Las Hualtatas, la parte más alta (falta 2013–2020 y parte de 2021 y 2024) | Ver cómo responde esa zona |
| `pw_mm` | mm | Agua precipitable: todo el vapor que hay en la columna de aire | Reconocer ríos atmosféricos |
| `ivt_mms` | mm·m/s | Transporte de vapor (aproximado): vapor × viento | Reconocer ríos atmosféricos |
| `t_700_C` | °C | Temperatura del aire a unos 3.000 m de altura | Reconocer tormentas cálidas |
| `ki_C` | °C | Índice K: qué tan inestable está el aire | Reconocer tormentas convectivas |
| `oni` | °C | Índice de El Niño del mes: +0,5 o más es El Niño, −0,5 o menos es La Niña | Para el extra |
| `p_<zona>_mm` | mm | Precipitación del día sobre la zona | Ver dónde cayó |
| `p_liq_<zona>_mm` | mm | Lluvia líquida sobre la zona, como `p_liq_mm` del nivel 1 | Ver dónde cayó como lluvia |
| `t_<zona>_C` | °C | Temperatura media del día en la zona | Comparar zonas |

`<zona>` es una de las 8 zonas de `zonas.csv`: `hualtatas`, `melosas_resto`, `volcan`, `yeso`, `colorado_alto`, `olivares`, `colorado_bajo` y `manzano_local`.

`pw_mm`, `ivt_mms`, `t_700_C` y `ki_C` vienen de un globo sonda que se lanza en Santo Domingo, en la costa: es un solo valor por día para toda la cordillera, y hay días sin dato.

## `zonas.csv`: una fila por zona (8)

| Columna | Unidad | Descripción |
|---|---|---|
| `zona` | texto | Nombre corto, el mismo de las columnas |
| `nombre` | texto | Nombre completo |
| `rama` | texto | Rama del nivel 2 a la que pertenece: `san_alfonso`, `colorado` o `local` |
| `caudal_propio` | texto | Columna con el caudal medido a la salida de la zona, si hay |
| `area_km2` | km² | Área |
| `elev_media_m` | m | Altura media |
| `pend_media_deg` | grados | Pendiente media |
| `pct_glaciar` | % | Parte del área cubierta por glaciares |
| `pct_area_sobre_4000m` | % | Parte del área sobre 4.000 m |

Ojo: las 8 zonas no se tocan entre sí y juntas forman la cuenca de El Manzano.
No las sumes con `p_colorado_mm` ni con `p_san_alfonso_mm` del nivel 2: esas ya incluyen varias zonas (mira la columna `rama`) y contarías la lluvia dos veces.

## Mini guía: catálogo de tormentas

Los umbrales son un punto de partida: puedes cambiarlos si explicas por qué.

1. Arma la lista de tormentas: días seguidos de abril a septiembre con `p_mm` de 10 mm o más. Cada racha es una tormenta.
2. Mide la respuesta del río: el caudal máximo desde el primer día de la tormenta hasta 2 días después del último, dividido por la mediana de los 7 días anteriores a la tormenta. Si la respuesta es 3 o más, hubo crecida.
3. Clasifica cada tormenta con el valor máximo de sus días:
   - cálida o fría: cálida si `iso0_m` llega a 3.000 m o más;
   - río atmosférico: mucho vapor, `pw_mm` de 20 o más e `ivt_mms` de 250 o más;
   - convectiva: aire inestable, `ki_C` de 30 o más. Ojo: un `ki_C` alto también marca aire muy húmedo.
4. Mira dónde cayó la lluvia líquida de cada tormenta, zona por zona.
5. Compara las tormentas que hicieron crecer el río con las que no.
6. Extra: agrupa los inviernos según el promedio del `oni` de mayo a septiembre y compara la `iso0_m` de los días de lluvia, la lluvia líquida y las crecidas.

Ten en cuenta:
- Desde 2019 no hay sedimento: la respuesta se mide con el caudal y con `evento_documentado`.
- Hay centrales hidroeléctricas que captan agua antes de las estaciones de Olivares, Colorado alto y Volcán, y el embalse El Yeso frena el agua de la zona `yeso`.
- Son pocos casos: 18 eventos documentados de abril a septiembre y solo 3 inviernos con El Niño.

## Mini guía: modelo simple (destacado)

1. Una fila por tormenta. Objetivo: 1 si hubo crecida, 0 si no.
2. Variables: el tipo de la tormenta y su lluvia líquida por zona. No uses el caudal ni `evento_documentado`.
3. Hay pocas crecidas, así que no separes por tiempo: entrena con todos los años menos uno, prueba con ese año y repite con cada año (`sklearn.model_selection.LeaveOneGroupOut`, con el año como grupo).
4. Mide con PR-AUC (`sklearn.metrics.average_precision_score`). Compárala con una regla simple: ordenar las tormentas por su lluvia líquida total.

## Logrado

- Un catálogo de las tormentas de abril a septiembre de 2000 a 2026, con su tipo, que incluya los 18 eventos documentados.
- Mostrar que las tormentas cálidas y con mucho vapor provocan las mayores crecidas, y que al menos 6 de las 10 tormentas con mayor respuesta son eventos documentados.
- Mostrar en qué zonas cayó la lluvia líquida de las crecidas, comparándola con la parte del área que ocupa cada zona.
- Extra: comparar los inviernos con El Niño, La Niña y neutros, y discutir si la diferencia es concluyente con tan pocos inviernos.
- Destacado: el modelo simple, con su PR-AUC al lado de la de la regla. Explicar si la supera y qué variables pesan más.
