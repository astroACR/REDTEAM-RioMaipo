# Nivel 1: lluvia, calor y sedimento en el río Maipo

`nivel1_manzano.csv` tiene una fila por día, del 2000 al 2026, para el río Maipo en El Manzano.
El río se pone turbio por dos causas: la lluvia cálida de invierno y el deshielo de verano.
La pregunta es: ¿en qué meses actúa cada una y cuándo importa la altura de la isoterma 0 °C?

| Columna | Unidad | Descripción |
|---|---|---|
| `fecha` | AAAA-MM-DD | Día |
| `anio_hidro` | año | Año hidrológico, de abril a marzo |
| `mes` | 1–12 | Mes |
| `q_m3s` | m³/s | Caudal del río |
| `ssc_mgL` | mg/L | Sedimento medido en la muestra del día |
| `ssc_hora_h` | hora | Hora en que se tomó la muestra |
| `p_mm` | mm | Precipitación del día sobre la cuenca |
| `p_acum3d_mm` | mm | Precipitación de los últimos 3 días |
| `t_media_C` | °C | Temperatura media del día sobre la cuenca |
| `iso0_m` | m | Altura donde el aire está a 0 °C |
| `iso0_fuente` | texto | Medida por radiosonda o estimada |
| `frac_bajo_iso0` | 0–1 | Parte de la cuenca donde llueve en vez de nevar |
| `p_liq_mm` | mm | Lluvia líquida: precipitación × `frac_bajo_iso0` | IMPORTANTEEEEE
| `p_liq_48h_mm` | mm | Lluvia líquida de hoy más la de ayer |
| `evento_documentado` | 0/1 | 1 si ese día hubo un evento de turbiedad conocido |
| `evento_causa` | texto | Causa reportada del evento |
| `evento_fuente` | texto | Dónde se documentó: tesis (bustos2011) o prensa |
| `duracion_evento_h` | h | Duración del evento |
| `iso0_reportada_m` | m | Isoterma 0 °C reportada para el evento |
| `ssc_pico_estimado_mgL` | mg/L | Sedimento estimado del evento; no es una medición |

## Mini guía: saltos de caudal en verano

En verano el río puede crecer sin llover, por el deshielo. Para encontrar esos días:

1. Quédate con los meses de octubre a marzo.
2. Descarta los días con lluvia: `p_acum3d_mm` menor a 1 mm.
3. Calcula la mediana del caudal de los 7 días anteriores: `df.q_m3s.shift(1).rolling(7).median()`.
4. Si el caudal de hoy supera 1,2 veces esa mediana, es un salto.
5. Compara qué tan seguido el sedimento es muy alto en días con salto y en días sin salto.

## Logrado

- Graficar el ciclo anual por mes y explicar cuándo dominan la lluvia y el deshielo.
- Mostrar que, en días con lluvia, la probabilidad de sedimento muy alto (sobre el percentil 95 de `ssc_mgL`) sube con `iso0_m`.
- Mostrar que en verano los saltos de caudal sin lluvia traen sedimento alto más seguido.
- Una regla con `p_liq_48h_mm` acierta al menos 11 de los 16 eventos de abril a septiembre de 2000–2018.
