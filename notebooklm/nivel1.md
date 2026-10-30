# nivel1 — exportado de `nivel1.ipynb`

# Hackathon Río Maipo — inicio

Nivel 1 ordenado según los criterios de logrado de `nivel1/LEEME_nivel1.md`. Corre todo en orden (**Run All**) desde la carpeta del kit: varias celdas reusan `n1`, `p95`, `AZUL`, `NARANJO` y `np`.

### Cómo usar el asistente

| Escribe | Para |
|---|---|
| `explorar("¿por qué...?")` | Pensar la física y las hipótesis antes de programar |
| `preguntar("¿cómo grafico...?", df)` | Código, gráficos, errores. `df` es opcional: manda un resumen, no la tabla |
| `auditar('''tu código o resultados''')` | Revisar el método: fuga de datos, partición, PR-AUC, regla base |
| `nueva()` | Empezar una conversación nueva al cambiar de tema (gasta menos) |
| `saldo()` | Ver cuánto presupuesto le queda al equipo |

El asistente no ve tus variables ni corre código: copia el código que te dé en una celda y, si algo falla, pégale el error con `preguntar(...)`.

## 0. Datos: carga e inspección

Antes de graficar: tipos, rango de fechas, faltantes y, sobre todo, **cuándo hay sedimento** (`ssc_mgL` solo 2000–2018) y **a qué hora se mide** (casi siempre 08:00).

```python
# 3. Primeros datos: nivel 1
import pandas as pd
import matplotlib.pyplot as plt

n1 = pd.read_csv("nivel1/nivel1_manzano.csv", parse_dates=["fecha"])
n1.head()
```

Resultado:
```
       fecha  anio_hidro  mes  q_m3s  ssc_mgL  ssc_hora_h  p_mm  p_acum3d_mm  \
0 2000-01-01        1999    1  161.0      NaN         NaN  0.01         0.01   
1 2000-01-02        1999    1  163.0      NaN         NaN  0.00         0.01   
2 2000-01-03        1999    1  160.0      NaN         NaN  0.42         0.43   
3 2000-01-04        1999    1  141.0      NaN         NaN  0.04         0.46   
4 2000-01-05        1999    1  146.0      NaN         NaN  0.00         0.46   

   t_media_C  iso0_m iso0_fuente  frac_bajo_iso0  p_liq_mm  p_liq_48h_mm  \
0       9.44  4325.0        igra          0.9082      0.01          0.01   
1       9.82  4168.0        igra          0.8773      0.00          0.01   
2       7.95  4007.0        igra          0.8366      0.35          0.35   
3       8.99  4053.0        igra          0.8494      0.04          0.39   
4       9.47  4278.0        igra          0.8997      0.00          0.04   

   evento_documentado evento_causa evento_fuente  duracion_evento_h  \
0                   0          NaN           NaN                NaN   
1                   0          NaN           NaN                NaN   
2                   0          NaN           NaN                NaN   
3                   0          NaN           NaN                NaN   
4                   0          NaN           NaN                NaN   

   iso0_reportada_m  ssc_pico_estimado_mgL  
0               NaN                    NaN  
1               NaN                    NaN  
2               NaN                    NaN  
3               NaN                    NaN  
4               NaN                    NaN  
```

```python
# Inspección antes de transformar: tipos, rangos, faltantes y cobertura del sedimento
import numpy as np

n1.info()
print("\nRango de fechas:", n1["fecha"].min().date(), "→", n1["fecha"].max().date())
print("\nFaltantes por columna (%):")
print((n1.isna().mean() * 100).round(1).sort_values(ascending=False).head(10))
con_ssc = n1.dropna(subset=["ssc_mgL"])
print(f"\nssc_mgL: {len(con_ssc)} días con dato, {con_ssc['fecha'].dt.year.min()}–{con_ssc['fecha'].dt.year.max()}")
print("Hora de la muestra (ssc_hora_h):", n1["ssc_hora_h"].value_counts().to_dict())
p95 = n1["ssc_mgL"].quantile(0.95)
ev = n1["ssc_mgL"] > p95
print(f"p95 global = {p95:.0f} mg/L | días sobre p95: invierno (abr–sep) {(ev & n1['mes'].between(4, 9)).sum()}, "
      f"verano (oct–mar) {(ev & ~n1['mes'].between(4, 9)).sum()}")
n1[["q_m3s", "ssc_mgL", "p_mm", "p_liq_mm", "p_liq_48h_mm", "iso0_m", "frac_bajo_iso0"]].describe().round(1)
```

Resultado:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9709 entries, 0 to 9708
Data columns (total 20 columns):
 #   Column                 Non-Null Count  Dtype         
---  ------                 --------------  -----         
 0   fecha                  9709 non-null   datetime64[ns]
 1   anio_hidro             9709 non-null   int64         
 2   mes                    9709 non-null   int64         
 3   q_m3s                  9653 non-null   float64       
 4   ssc_mgL                5258 non-null   float64       
 5   ssc_hora_h             5140 non-null   float64       
 6   p_mm                   9709 non-null   float64       
 7   p_acum3d_mm            9709 non-null   float64       
 8   t_media_C              9678 non-null   float64       
 9   iso0_m                 9709 non-null   float64       
 10  iso0_fuente            9709 non-null   object        
 11  frac_bajo_iso0         9709 non-null   float64       
 12  p_liq_mm               9709 non-null   float64       
 13  p_liq_48h_mm           9709 non-null   float64       
 14  evento_documentado     9709 non-null   int64         
 15  evento_causa           87 non-null     object        
 16  evento_fuente          87 non-null     object        
 17  duracion_evento_h      29 non-null     float64       
 18  iso0_reportada_m       28 non-null     float64       
 19  ssc_pico_estimado_mgL  25 non-null     float64       
dtypes: datetime64[ns](1), float64(13), int64(3), object(3)
memory usage: 1.5+ MB

Rango de fechas: 2000-01-01 → 2026-07-31

Faltantes por columna (%):
ssc_pico_estimado_mgL    99.7
iso0_reportada_m         99.7
duracion_evento_h        99.7
evento_fuente            99.1
evento_causa             99.1
ssc_hora_h               47.1
ssc_mgL                  45.8
q_m3s                     0.6
t_media_C                 0.3
p_liq_mm                  0.0
dtype: float64

ssc_mgL: 5258 días con dato, 2000–2018
Hora de la muestra (ssc_hora_h): {8.0: 5128, 18.0: 12}
p95 global = 1603 mg/L | días sobre p95: invierno (abr–sep) 9, verano (oct–mar) 254

```

Resultado:
```
        q_m3s  ssc_mgL    p_mm  p_liq_mm  p_liq_48h_mm  iso0_m  frac_bajo_iso0
count  9653.0   5258.0  9709.0    9709.0        9709.0  9709.0          9709.0
mean     93.0    420.5     2.7       1.1           2.2  3645.7             0.7
std      69.9    629.0     8.5       3.6           6.0   786.1             0.3
min      10.6      1.6     0.0       0.0           0.0   867.0             0.0
25%      51.8     65.7     0.0       0.0           0.0  3154.0             0.5
50%      70.9    181.7     0.0       0.0           0.0  3766.0             0.8
75%     110.0    523.0     0.7       0.3           1.6  4213.0             0.9
max     768.0   9770.0   117.2      52.6          83.4  5480.0             1.0
```

```python
# Separar por temporada: verano = oct–mar (deshielo), invierno = abr–sep (tormentas)
verano = n1[n1["mes"].isin([10, 11, 12, 1, 2, 3])]
invierno = n1[n1["mes"].isin([4, 5, 6, 7, 8, 9])]
print(f"Verano: {len(verano)} días | Invierno: {len(invierno)} días")
```

Resultado:
```
Verano: 4829 días | Invierno: 4880 días

```

## Criterio 1 — Ciclo fluvial verano–invierno: ¿cuándo dominan la lluvia y el deshielo?

```python
# Ciclo anual en orden hidrológico (abr→mar): invierno a la izquierda, deshielo a la derecha
orden = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
etiquetas = ["Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar"]
desde = "2000-01-01"
hasta = "2018-12-31"
g = n1[(n1["fecha"] >= desde) & (n1["fecha"] <= hasta)].groupby("mes")
x = range(12)
AZUL, NARANJO = "#2a78d6", "#eb6834"

fig, ax = plt.subplots(4, 1, sharex=True, figsize=(9, 11))

# 1. Precipitación total vs líquida (la diferencia es nieve que se guarda para el verano)
p = g[["p_mm", "p_liq_mm"]].mean().loc[orden]
ax[0].bar([i - 0.2 for i in x], p["p_mm"], width=0.4, color=AZUL, label="Precipitación total (p_mm)")
ax[0].bar([i + 0.2 for i in x], p["p_liq_mm"], width=0.4, color=NARANJO, label="Lluvia líquida (p_liq_mm)")
ax[0].set_ylabel("mm/día (promedio)")
ax[0].legend(frameon=False)
ax[0].set_title("Lluvia: cuánta cae y cuánta es líquida")

# 2. Isoterma 0 °C: qué tan alto llega el calor
ax[1].plot(x, g["iso0_m"].median().loc[orden], color=AZUL, lw=2, marker="o", ms=5)
ax[1].set_ylabel("iso0_m (mediana, m)")
ax[1].set_title("Isoterma 0 °C: sube en verano → derrite nieve")

# 3. Caudal: mediana + rango intercuartil
q = g["q_m3s"].quantile([0.25, 0.5, 0.75]).unstack().loc[orden]
ax[2].fill_between(x, q[0.25], q[0.75], color=AZUL, alpha=0.2, lw=0, label="P25–P75")
ax[2].plot(x, q[0.5], color=AZUL, lw=2, marker="o", ms=5, label="Mediana")
ax[2].set_ylabel("q_m3s (m³/s)")
ax[2].legend(frameon=False)
ax[2].set_title("Caudal")

# 4. Sedimento: mediana (mes típico) y P95 (extremos), escala log porque SSC es muy asimétrico
s = g["ssc_mgL"].quantile([0.5, 0.9]).unstack().loc[orden]
ax[3].plot(x, s[0.5], color=AZUL, lw=2, marker="o", ms=5, label="Mediana")
p95_mes = g["ssc_mgL"].quantile(0.95).loc[orden]  # no pisar `p95` (umbral global que usan otras celdas)
ax[3].plot(x, p95_mes, color=NARANJO, lw=2, marker="o", ms=5, ls="--", label="P95")
ax[3].set_yscale("log")
ax[3].set_ylabel("ssc_mgL (mg/L, log)")
ax[3].legend(frameon=False)
ax[3].set_title("Sedimento en suspensión")

for a in ax:
    a.grid(axis="y", color="#e0dfda", lw=0.8)
    a.spines[["top", "right"]].set_visible(False)
    a.axvspan(-0.5, 5.5, color="#f0efec", zorder=0)  # abr–sep: régimen de tormentas
ax[3].set_xticks(list(x), etiquetas)
ax[3].set_xlim(-0.5, 11.5)
fig.suptitle("Ciclo anual en El Manzano (2000–2018) — fondo gris: invierno abr–sep", y=0.995)
fig.tight_layout()
```

**[Figura: `nivel1_celda07_Ciclo_anual_en_El_Manzano_2000_2018_fondo_gris_invierno_abr.png` — Ciclo anual en El Manzano (2000–2018) — fondo gris: invierno abr–sep]**


Ciclo anual en El Manzano: cuándo domina la lluvia y cuándo el deshielo
Invierno (abril–septiembre): manda la lluvia, pero el río casi no responde en el día a día.
La precipitación se concentra en estos meses y llega a su máximo en junio, con 7,12 mm/día en promedio. Pero solo 2,51 mm/día de esa precipitación caen como lluvia líquida (35 %). El resto cae como nieve, porque la isoterma 0 °C está baja: su mediana es de ~3.030 m en agosto. Esa nieve no escurre, se queda acumulada en la cordillera. Por eso el caudal se mantiene plano, entre 55 y 66 m³/s, y la mediana de sedimento queda entre 67 y 128 mg/L. Aun así, el percentil 95 del sedimento llega a ser hasta 12 veces la mediana (928 contra 80 mg/L en abril). Eso indica eventos breves e intensos: tormentas cálidas en que la isoterma sube y llueve sobre una parte mayor de la cuenca.

Verano (octubre–marzo): manda el deshielo.
Casi no llueve: menos de 0,9 mm/día entre diciembre y marzo. Sin embargo, la isoterma sube a ~4.350 m en enero y la nieve acumulada en invierno se derrite. El caudal se triplica, hasta una mediana de 160 m³/s en enero. El sedimento lo sigue, hasta 873 mg/L en diciembre, unas 10 veces la mediana de invierno. En estos meses el sedimento alto es sostenido y no depende de la lluvia: el percentil 95 es solo ~3 veces la mediana.

Conclusión. El agua que precipita en invierno llega al río meses después. El sedimento responde a dos mecanismos distintos:

Deshielo de verano: controlado por la temperatura y la isoterma. Produce turbiedad alta, prolongada y predecible.

Lluvia líquida de invierno: controlada por la lluvia que cae bajo la isoterma. Produce pulsos raros y cortos.

Limitación. El sedimento se muestrea una vez al día, a las 08:00 (ssc_hora_h). Ese muestreo capta bien los pulsos largos del deshielo, pero puede perder los picos de pocas horas de las tormentas invernales. Por eso el riesgo de invierno probablemente está subestimado en estos gráficos.

## Criterio 2 — En días con lluvia, P(SSC > p95) sube con `iso0_m`

```python
# P(SSC > p95 global) según la altura de la isoterma 0 °C, solo días con precipitación
import numpy as np

d = n1.dropna(subset=["ssc_mgL", "iso0_m"]).copy()
p95 = d["ssc_mgL"].quantile(0.95)  # umbral global: calculado con TODOS los días, antes de filtrar
d = d[d["p_mm"] > 0].copy()
d["evento"] = d["ssc_mgL"] > p95
d["temporada"] = np.where(d["mes"].isin([4, 5, 6, 7, 8, 9]), "Invierno (abr–sep)", "Verano (oct–mar)")
d["tramo"] = pd.cut(d["iso0_m"], range(1500, 5501, 500))

tabla = d.groupby(["temporada", "tramo"], observed=True)["evento"].agg(["mean", "sum", "size"])
tabla = tabla[tabla["size"] >= 10]  # tramos con menos de 10 días no dicen nada
print(f"p95 global = {p95:.0f} mg/L | días con p_mm > 0: {len(d)}")
print(tabla.round(3))

# Intervalo de Wilson al 95 %: cuánto podría variar la proporción solo por azar con n días
z = 1.96
n, k = tabla["size"], tabla["sum"]
centro = (k + z**2 / 2) / (n + z**2)
radio = z * np.sqrt(k * (n - k) / n + z**2 / 4) / (n + z**2)
tabla["lo"], tabla["hi"] = centro - radio, centro + radio

fig, ax = plt.subplots(figsize=(9, 5))
for (temp, t), color, dy in zip(tabla.groupby(level="temporada"), [AZUL, NARANJO], [-14, 8]):
    xc = [iv.mid for iv in t.index.get_level_values("tramo")]
    ax.fill_between(xc, t["lo"] * 100, t["hi"] * 100, color=color, alpha=0.15, lw=0)
    ax.plot(xc, t["mean"] * 100, color=color, lw=2, marker="o", ms=6, label=temp)
    for xi, yi, ni in zip(xc, t["mean"] * 100, t["size"]):
        ax.annotate(f"n={ni}", (xi, yi), textcoords="offset points", xytext=(0, dy),
                    ha="center", fontsize=8, color="#52514e")

ax.set_xlabel("Isoterma 0 °C, iso0_m (m) — centro del tramo de 500 m")
ax.set_ylabel(f"% de días con SSC > p95 ({p95:.0f} mg/L)")
ax.set_title("Probabilidad de sedimento extremo según la isoterma 0 °C (días con p_mm > 0)")
ax.set_ylim(-5, None)
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="y", color="#e0dfda", lw=0.8)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
```

Resultado:
```
p95 global = 1603 mg/L | días con p_mm > 0: 2150
                                  mean  sum  size
temporada          tramo                         
Invierno (abr–sep) (1500, 2000]  0.000    0    94
                   (2000, 2500]  0.000    0   183
                   (2500, 3000]  0.000    0   284
                   (3000, 3500]  0.000    0   319
                   (3500, 4000]  0.015    3   200
                   (4000, 4500]  0.000    0    38
Verano (oct–mar)   (1500, 2000]  0.000    0    12
                   (2000, 2500]  0.000    0    34
                   (2500, 3000]  0.025    2    80
                   (3000, 3500]  0.042    7   166
                   (3500, 4000]  0.070   21   298
                   (4000, 4500]  0.108   31   288
                   (4500, 5000]  0.208   21   101
                   (5000, 5500]  0.375    9    24

```

**[Figura: `nivel1_celda10_Probabilidad_de_sedimento_extremo_según_la_isoterma_0_C_días.png` — Probabilidad de sedimento extremo según la isoterma 0 °C (días con p_mm > 0)]**

**Lectura y cuidado:** en verano la probabilidad sube claramente con la isoterma, pero el **p95 global lo fija el deshielo** (casi todos los días sobre p95 son de oct–mar) y `p_mm > 0` incluye lloviznas. Con isoterma alta en verano también hay más deshielo: la subida mezcla calor y lluvia (el criterio 3 muestra que el sedimento alto de verano viene con saltos de caudal sin lluvia). La celda siguiente repite la curva **solo en invierno**, con su propio p95 y lluvia relevante.

```python
# Control de honestidad: misma curva, solo invierno, con su propio p95 y lluvia relevante en 48 h
# (>= 10 mm hoy o ayer: el piso de "tormenta" del Nivel 3; iso0_m máxima de 48 h por el desfase lluvia → muestra 08:00)
s = n1.sort_values("fecha").copy()
s["iso0_48h"] = s["iso0_m"].rolling(2).max()
s["lluvia_48h"] = s["p_mm"].rolling(2).max() >= 10
inv = s[s["mes"].between(4, 9) & s["ssc_mgL"].notna()]
p95_inv = inv["ssc_mgL"].quantile(0.95)
inv = inv[inv["lluvia_48h"]].copy()
inv["evento"] = inv["ssc_mgL"] > p95_inv
inv["tramo"] = pd.cut(inv["iso0_48h"], range(1500, 5001, 500))
ti = inv.groupby("tramo", observed=True)["evento"].agg(["mean", "sum", "size"])
print(f"p95 de invierno = {p95_inv:.0f} mg/L | días de invierno con lluvia >= 10 mm en 48 h: {len(inv)}")
print(ti[ti["size"] >= 10].round(3))
print("Mediana de p_mm en días de invierno con lluvia, por tramo de iso0_m (¿llueve fuerte con isoterma muy alta?):")
w0 = n1[n1["mes"].between(4, 9) & (n1["p_mm"] > 0)]
print(w0.groupby(pd.cut(w0["iso0_m"], range(1500, 5001, 500)), observed=True)["p_mm"].median().round(1))
```

Resultado:
```
p95 de invierno = 595 mg/L | días de invierno con lluvia >= 10 mm en 48 h: 581
               mean  sum  size
tramo                         
(1500, 2000]  0.059    1    17
(2000, 2500]  0.051    4    78
(2500, 3000]  0.028    4   141
(3000, 3500]  0.062   12   194
(3500, 4000]  0.071    9   127
(4000, 4500]  0.043    1    23
Mediana de p_mm en días de invierno con lluvia, por tramo de iso0_m (¿llueve fuerte con isoterma muy alta?):
iso0_m
(1500, 2000]    4.1
(2000, 2500]    7.1
(2500, 3000]    6.6
(3000, 3500]    5.5
(3500, 4000]    3.6
(4000, 4500]    1.8
(4500, 5000]    1.1
Name: p_mm, dtype: float64

```

**Lectura:** en invierno la curva queda plana y ruidosa aun con lluvia ≥ 10 mm. Dos razones físicas: (1) con isoterma > 4.000 m en invierno casi solo llovizna (ver medianas de `p_mm`), y (2) la muestra de las 08:00 pierde los picos breves de las tormentas. Con `ssc_mgL` el efecto de la isoterma se ve en verano (mezclado con deshielo); en invierno hay que validar contra `evento_documentado` (criterio 4), donde `p_liq_48h_mm = p_mm × frac_bajo_iso0` ya combina lámina de lluvia e isoterma.

La celda siguiente complementa: los días extremos **con lluvia**, ¿ocurren con la isoterma más alta de lo normal para un día lluvioso de esa época?

```python
# Eventos SSC > p95 en días con lluvia, sobre el año hidrológico (abr→mar, 2000–2018 superpuestos)
# x = día del año hidrológico, y = isoterma 0 °C del día del evento, color = año
# Fondo gris: isoterma "normal" para esa época del año → ¿los eventos ocurren con isoterma más alta de lo normal?
import numpy as np

d = n1[n1["anio_hidro"].between(2000, 2018)].copy()               # filtro: entero, sin .dt
inicio = pd.to_datetime(d["anio_hidro"].astype(str) + "-04-01")   # 1 de abril de su año hidrológico
d["dia_hidro"] = (d["fecha"] - inicio).dt.days                    # la resta se hace con la fecha

p95 = n1["ssc_mgL"].quantile(0.95)  # umbral global, antes de filtrar por lluvia
ev = d[(d["ssc_mgL"] > p95) & (d["p_mm"] >= 1)].dropna(subset=["iso0_m"])  # el filtro de lluvia va solo aquí

# Isoterma "normal" de los días con lluvia (un día lluvioso es más frío que uno despejado de la misma fecha)
# Hay pocos días con lluvia por fecha, así que se suaviza con una ventana de 31 días
lluviosos = d[d["p_mm"] >= 1]
clim = lluviosos.groupby("dia_hidro")["iso0_m"].quantile([0.25, 0.5, 0.75]).unstack().reindex(range(366))
clim = clim.rolling(31, center=True, min_periods=1).mean()

# ¿Qué fracción de eventos ocurre con la isoterma sobre la mediana de su época?
sobre = ev["iso0_m"] > clim.loc[ev["dia_hidro"], 0.5].values
print(f"p95 global = {p95:.0f} mg/L | eventos con p_mm >= 1: {len(ev)} | con isoterma sobre lo normal: {sobre.mean():.0%}")

fig, ax = plt.subplots(figsize=(12, 6))
ax.fill_between(clim.index, clim[0.25], clim[0.75], color="#e0dfda", lw=0, label="Isoterma normal en días con lluvia (P25–P75)")
ax.plot(clim.index, clim[0.5], color="#8a8984", lw=1.5, label="Isoterma mediana")

sc = ax.scatter(ev["dia_hidro"], ev["iso0_m"], c=ev["fecha"].dt.year, cmap="turbo", vmin=2000, vmax=2018,
                s=50, edgecolors="white", linewidths=0.5, label="Evento con lluvia (p_mm ≥ 1)")
fig.colorbar(sc, ax=ax, label="Año del evento")

meses = ["Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar"]
ax.set_xticks([0, 30, 61, 91, 122, 153, 183, 214, 244, 275, 306, 334], meses)
ax.set_xlim(0, 365)
ax.set_ylabel("Isoterma 0 °C, iso0_m (m)")
ax.set_title(f"Eventos SSC > p95 ({p95:.0f} mg/L) en días con lluvia, El Manzano 2000–2018")
ax.axhline(3500, color="#52514e", ls="--", lw=1, label="Isoterma 3.500 m")
ax.axhline(4500, color="#52514e", ls="--", lw=1, label="Isoterma 4.500 m")
ax.legend(frameon=False, loc="lower right", fontsize=9)  # después de axhline, para que entren en la leyenda
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()

```

Resultado:
```
p95 global = 1603 mg/L | eventos con p_mm >= 1: 33 | con isoterma sobre lo normal: 64%

```

**[Figura: `nivel1_celda14_Eventos_SSC_p95_p95_0f_mg_L_en_días_con_lluvia_El_Manzano_20.png` — Eventos SSC > p95 ({p95:.0f} mg/L) en días con lluvia, El Manzano 2000–2018]**

**Lectura:** son pocos días (33 extremos con `p_mm ≥ 1`), y ~2 de cada 3 (64 %) ocurren con isoterma sobre la mediana de los días lluviosos de su época. Es una señal débil: con n pequeño, no concluir más que eso.

## Criterio 3 — En verano, los saltos de caudal sin lluvia traen sedimento alto más seguido

```python
# Verano: ¿los saltos de caudal sin lluvia traen sedimento alto más seguido?
# Mini guía del LEEME: oct–mar, sin lluvia (p_acum3d_mm < 1), salto si q > 1,2 × mediana de los 7 días ANTERIORES
import numpy as np

v = n1.sort_values("fecha").copy()
v["q_med7_prev"] = v["q_m3s"].shift(1).rolling(7).median()  # shift(1): solo el pasado, sin mirar hoy
v["salto"] = v["q_m3s"] > 1.2 * v["q_med7_prev"]
p95 = n1["ssc_mgL"].quantile(0.95)
v = v[v["mes"].isin([10, 11, 12, 1, 2, 3]) & (v["p_acum3d_mm"] < 1)].dropna(subset=["ssc_mgL", "q_med7_prev"])
v["extremo"] = v["ssc_mgL"] > p95

tabla = v.groupby("salto")["extremo"].agg(dias="size", extremos="sum", pct="mean")
tabla = tabla.reindex([False, True]).rename(index={False: "Sin salto", True: "Con salto"})
print(f"Verano seco (p_acum3d_mm < 1) | p95 global = {p95:.0f} mg/L")
print(tabla.round(3))
print(f"Un día con salto tiene {tabla.loc['Con salto', 'pct'] / tabla.loc['Sin salto', 'pct']:.1f}× más probabilidad de SSC > p95")

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(tabla.index, tabla["pct"] * 100, color=[AZUL, NARANJO], width=0.5)
for i, (pct, n) in enumerate(zip(tabla["pct"], tabla["dias"])):
    ax.annotate(f"{pct:.0%}\nn={n}", (i, pct * 100), textcoords="offset points", xytext=(0, 4), ha="center", fontsize=9)
ax.set_ylabel(f"% días con SSC > p95 ({p95:.0f} mg/L)")
ax.set_title("Verano sin lluvia: deshielo con y sin salto de caudal")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
```

Resultado:
```
Verano seco (p_acum3d_mm < 1) | p95 global = 1603 mg/L
           dias  extremos    pct
salto                           
Sin salto  1332       137  0.103
Con salto   187        56  0.299
Un día con salto tiene 2.9× más probabilidad de SSC > p95

```

**[Figura: `nivel1_celda17_Verano_sin_lluvia_deshielo_con_y_sin_salto_de_caudal.png` — Verano sin lluvia: deshielo con y sin salto de caudal]**

**Lectura:** en verano seco, un día con salto de caudal (onda de calor → deshielo brusco) tiene ~3× más probabilidad de SSC > p95 que uno sin salto. El salto arrastra sedimento fino glaciar y de morrenas sin que caiga una gota.

## Criterio 4 — Regla `p_liq_48h_mm` contra los 16 eventos de abr–sep 2000–2018

```python
# Invierno: regla p_liq_48h_mm >= umbral contra los 16 eventos documentados (abr–sep 2000–2018)
# La muestra de las 08:00 no ve los picos breves de las tormentas → se valida contra evento_documentado, no contra ssc_mgL
w = n1[n1["mes"].between(4, 9) & n1["fecha"].dt.year.between(2000, 2018)].sort_values("fecha")

# Días documentados → episodios (un temporal marca varios días seguidos; tolera 1 día sin marca)
doc = w[w["evento_documentado"] == 1].copy()
doc["episodio"] = (doc["fecha"].diff().dt.days > 2).cumsum()
ep = doc.groupby("episodio").agg(inicio=("fecha", "min"), anio_hidro=("anio_hidro", "first"),
                                 ssc_max_08h=("ssc_mgL", "max"), p_liq48_max=("p_liq_48h_mm", "max"))
print(f"{len(doc)} días documentados → {len(ep)} episodios | con SSC 08:00 > p95: {(ep['ssc_max_08h'] > p95).sum()}")

def alarmas(u):
    """Episodios de alarma (rachas con p_liq_48h_mm >= u) y cuántos no coinciden con ningún evento documentado."""
    a = w[w["p_liq_48h_mm"] >= u].copy()
    a["ep"] = (a["fecha"].diff().dt.days > 2).cumsum()
    con_evento = a.groupby("ep")["evento_documentado"].max() == 1
    return len(con_evento), int((~con_evento).sum())

filas = []
for u in [10, 20, 30, 40]:
    tot, falsas = alarmas(u)
    filas.append({"umbral_mm": u, "aciertos": int((ep["p_liq48_max"] >= u).sum()), "alarmas": tot, "sin_evento": falsas})
print(pd.DataFrame(filas).to_string(index=False))

# Honestidad: elegir el umbral sin mirar el año que se evalúa (dejando un anio_hidro fuera)
grid = np.arange(5, 81, 5)
aciertos_fuera = 0
for anio in ep["anio_hidro"].unique():
    train, test = ep[ep["anio_hidro"] != anio], ep[ep["anio_hidro"] == anio]
    u_sel = max(u for u in grid if (train["p_liq48_max"] >= u).mean() >= 11 / 16)
    aciertos_fuera += int((test["p_liq48_max"] >= u_sel).sum())
print(f"Umbral elegido dejando un año fuera → aciertos fuera de muestra: {aciertos_fuera}/{len(ep)}")

```

Resultado:
```
34 días documentados → 16 episodios | con SSC 08:00 > p95: 1
 umbral_mm  aciertos  alarmas  sin_evento
        10        16      158         142
        20        14       79          65
        30        13       35          22
        40         9       21          12
Umbral elegido dejando un año fuera → aciertos fuera de muestra: 10/16

```

**Lectura:**
- Los días documentados se agrupan en **16 episodios**; casi ninguno se ve sobre p95 en la muestra de las 08:00 → validar contra `ssc_mgL` habría hecho fallar cualquier regla.
- Con umbral **30 mm** la regla acierta **13/16** (cumple ≥ 11), con 35 episodios de alarma de los que 22 no tienen evento documentado (falsas alarmas o eventos no registrados).
- **Honestidad:** ese umbral se eligió mirando los mismos 16 eventos. Eligiéndolo dejando cada año fuera, acierta **10/16**. Reportamos ambos.

## Resumen de criterios de logrado

| Criterio | Estado | Evidencia |
|---|---|---|
| 1. Ciclo anual y regímenes | ✅ | Lluvia abr–sep (mayormente nieve), deshielo oct–mar con máximo de caudal y SSC en dic–ene |
| 2. P(SSC > p95) sube con `iso0_m` en días con lluvia | ✅ con matiz | Sube en verano (mezclado con deshielo); en invierno no se ve en `ssc_mgL` por la muestra de 08:00 |
| 3. Saltos de caudal en verano | ✅ | ~3× más días extremos con salto |
| 4. Regla `p_liq_48h_mm` ≥ 11/16 | ✅ con matiz | 13/16 con 30 mm; 10/16 fuera de muestra |

**Limitaciones:** muestra única a las 08:00 (aliasing de picos invernales), `evento_documentado` puede estar sesgado a las tormentas más grandes, sin sedimento desde 2019.
