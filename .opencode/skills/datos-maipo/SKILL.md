---
name: datos-maipo
description: Cómo cargar y unir los CSV de la Hackathon Río Maipo, qué años cubre cada columna y qué trampas de los datos evitar. Úsala antes de escribir código que lea estos CSV, al comparar estaciones o zonas, o cuando un resultado se vea raro.
---

# Datos de la Hackathon Río Maipo

Las columnas de cada CSV están descritas en `nivelN/LEEME_nivelN.md`. Aquí va lo que no está ahí. Las reglas de método (fuga de datos, partición, PR-AUC) están en `AGENTS.md`.

## Cargar y unir (desde la raíz del kit)

```python
import pandas as pd
n1 = pd.read_csv("nivel1/nivel1_manzano.csv", parse_dates=["fecha"])
n2 = pd.read_csv("nivel2/nivel2_tributarios.csv", parse_dates=["fecha"])
n3 = pd.read_csv("nivel3/nivel3_tormentas.csv", parse_dates=["fecha"])
df = n1.merge(n2, on="fecha").merge(n3, on="fecha")   # 9.709 días × 61 columnas
sub = pd.read_csv("nivel2/subcuencas.csv")            # 12 subcuencas
zonas = pd.read_csv("nivel3/zonas.csv")               # 8 zonas
```

Los tres diarios van del 2000-01-01 al 2026-07-31, una fila por día.

## Cobertura: hay muchos huecos

| Columna | Años con dato | Días con dato |
|---|---|---|
| `ssc_mgL` (El Manzano) | 2000–2018 | 5.258 |
| `ssc_colorado_mgL` | 2003–2010 | 1.598 |
| `ssc_san_alfonso_mgL` | 2003–2005 | 624 |
| `q_san_alfonso_m3s` | 2000–2017 | 5.995 |
| `q_hualtatas_m3s` | 2000–2026; falta 2013–2020 y parte de 2021 y 2024 | 6.226 |
| `pw_mm`, `ivt_mms`, `t_700_C`, `ki_C` | 2000–2026, con días sin dato | ~8.300 |
| `iso0_m`, `oni`, precipitación y temperatura | completas | 9.709 |

- Desde 2019 no hay sedimento: después de esa fecha la respuesta del río se mide con el caudal y con `evento_documentado`.
- `iso0_m` viene de la radiosonda (`iso0_fuente = igra`) o, en 333 días, es estimada (`cr2met_ajustado`).
- `evento_documentado` marca 87 días. `evento_causa`, `evento_fuente`, `duracion_evento_h`, `iso0_reportada_m` y `ssc_pico_estimado_mgL` solo tienen valor esos días.

## Trampas

1. **Comparar con los mismos días.** Al comparar estaciones, quédate con los días en que todas tienen dato (`dropna(subset=[...])`). Si no, comparas años distintos.
2. **Subcuencas anidadas (nivel 2).** `manzano` contiene a todas. Para repartir sin contar dos veces, usa las que tienen el mismo `drena_a`: `san_alfonso`, `colorado_maipo` y `manzano_local_residuo` drenan a `manzano`; `colorado_alto`, `olivares` y `colorado_bajo_residuo` drenan a `colorado_maipo`.
3. **Zonas (nivel 3).** Las 8 zonas no se tocan entre sí. No las sumes con `p_colorado_mm` ni con `p_san_alfonso_mm`: esas ya agrupan varias zonas (mira la columna `rama`).
4. **Caudales intervenidos.** Hay centrales hidroeléctricas que captan agua antes de Olivares, Colorado alto y Volcán, y el embalse El Yeso frena la zona `yeso`. Su caudal por km² sale más bajo que el que produce la cuenca.
5. **Año hidrológico.** `anio_hidro` va de abril a marzo: úsalo para agrupar inviernos y veranos sin cortar la temporada.
6. **Una sola radiosonda.** `pw_mm`, `ivt_mms`, `t_700_C` y `ki_C` vienen de un globo lanzado en Santo Domingo, en la costa: un valor por día para toda la cordillera.
7. **Muestra de las 08:00.** Desde el 2000 casi todo el sedimento se midió a las 08:00 (`ssc_hora_h`): un pico breve que pase entre dos muestras no queda registrado. Por eso las crecidas de invierno se validan también con `evento_documentado` y con la respuesta del caudal.

## Referencias

`referencias/` trae la tesis de Bustos (2011) y `prensa.es.md`, con los eventos de turbiedad de 2008–2026. Son largas: búscalas con grep por fecha o palabra, no las leas enteras.
