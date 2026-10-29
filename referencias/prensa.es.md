# Eventos de turbiedad en la prensa chilena (2008–2026)

Recopilación del equipo ACC de eventos de turbiedad en los ríos Maipo y Mapocho que afectaron el agua potable de Santiago, con dos fuentes de prensa por evento cuando existen (prensa, Senapred/ONEMI citados en prensa, comunicados de Aguas Andinas, gob.cl). Son 17 eventos entre mayo de 2008 y octubre de 2026. Cada evento trae su ficha y, debajo, extractos textuales de cada noticia citada: solo lo que sirve al proyecto (fechas y horas, turbiedad en UNT, causa meteorológica, alcance y duración del corte, reservas y autonomía). Se omitieron declaraciones políticas, multas, listas de comunas, recomendaciones de consumo y lo ocurrido fuera de Santiago. La ficha, en tabla, está en `data/processed/eventos_prensa.csv`; el método, en `context/bitacora/03-eventos-prensa.md`; el HTML de cada noticia y el texto extraído completo, en `_original/prensa/`.

## Criterios

- Una sección por evento. El tipo es la acción más severa que efectivamente ocurrió: corte de suministro, alerta o pico de turbiedad reportado. Un corte anunciado y luego cancelado cuenta como alerta; los cortes locales parciales van en el detalle.
- Las comunas afectadas solo se informan para cortes ejecutados (cifra inicial del anuncio). Las comunas "en riesgo" van en el detalle.
- La causa sale solo de lo que dice la fuente, sin inferirla por la estación del año. Tormenta cálida: lluvia "donde normalmente nieva", isoterma sobre 3.000 m o río atmosférico. Deshielo: calor en la cordillera. Convectiva: lo dice la fuente. Si la fuente no lo dice, la causa queda como no informada.
- La fecha de fin es el último día con impacto reportado (reposición del servicio o cancelación de la alerta).
- Cuando las fuentes difieren en turbiedad (UNT) o comunas, se usa la cifra de la fuente más cercana a Aguas Andinas o Senapred, y la alternativa va en el detalle.
- Desde 2020 casi todos los eventos son alertas, porque los megaestanques de Pirque evitan los cortes. Para validar contra el sedimento de El Manzano conviene contar alertas y picos reportados como positivos, no solo los cortes.

## Eventos

### Mayo 2008 — corte de suministro, río Maipo

- Fechas: desde el 1 de mayo de 2008 (solo se conoce el mes; el día 1 es convención).
- Tipo: corte de suministro.
- Causa según la fuente: tormenta cálida (lluvia sobre 3.500 m).
- Confianza: baja.
- Detalle: unos 3 días sin agua. Emol (2017) la describe como la primera emergencia de esa magnitud. No hay fuente primaria de la época.

#### Noticia: Turbiedad en el río Maipo: Los nueve cortes masivos de suministro que ha protagonizado Aguas Andinas desde 2008 (Emol, 2017-04-21)

https://www.emol.com/noticias/Nacional/2017/04/21/855108/Turbiedad-del-rio-Maipo-Los-diez-cortes-masivos-de-suministro-que-ha-protagonizado-Aguas-Andinas-en-nueve-anos.html

El río Maipo oscila normalmente entre 40 y 500 UNT y la planta de Las Vizcachas puede potabilizar hasta los 20 mil UNT. Ayer, en algunas horas. alcanzó los 100 mil UNT.

SANTIAGO.- En mayo de 2008 los santiaguinos estuvieron tres días sin el servicio de agua potable en un evento que fue declarado por la Superintendencia de Servicios Sanitarios (SISS) como de "conmoción pública".

Aguas Andinas debió suspender el suministro tras un temporal que tuvo como característica especial que lloviera sobre los 3.500 metros de altura, donde normalmente debiera nevar, provocando así una alta turbiedad en el río Maipo afectando las plantas de agua potable.

Esa fue la primera vez que la sanitaria debió enfrentar una emergencia de tal magnitud por este motivo, situación que se ha repetido en los últimos años.

El verano de 2013 fue el más crítico. El 21 de enero, 9 de febrero y 11 de febrero se registraron situaciones similares a la de 2008. Solo a modo de ejemplo, el corte del 9 de febrero provocó que 1.128.044 hogares -con 4,5 millones de habitantes en total- estuvieron sin servicio luego de que el río Maipo alcanzara los 380 mil UNT (nivel de turbiedad).

La SISS ordenó a la empresas elaborar nuevos estudios de mitigación, y una de las mejores aplicadas fue la construcción de un acueducto de cinco kilómetros que conecta el embalse El Yeso, ubicado a unos 2.500 metros de altura con la planta de tratamiento Las Vizcachas, que además fue complementada con la construcción de nuevos estanques de seguridad.

Posteriormente el 2016 las primeras lluvias de abril hicieron colapsar el servicio y el corte afectó esta vez a 4,2 millones de personas.

En tanto, en lo que va de este año ya son dos los episodios de emergencia: el primero, ocurrió en febrero tras un aluvión en el Cajón del Maipo que dejó 33 comunas de la capital sin agua. Y el segundo es el que afecta hoy y que mantuvo a cerca de un millón de personas sin agua.

#### Noticia: Agua turbia: Los trabajos pendientes de Aguas Andinas para evitar nuevos cortes (The Clinic, 2017-02-27)

https://www.theclinic.cl/2017/02/27/agua-turbia-los-trabajos-pendientes-aguas-andinas-evitar-nuevos-cortes/

Según un reportaje de CIPER, anteriormente, en 2008, hubo lluvias cordilleranas que triplicaron el flujo de agua del Río Maipo y también produjo un corte masivo en Santiago. Esto significó que la SIIS y Aguas Andinas realizaran construcciones preventivas que consistían en 7 pozos subterráneos con 300 litros de agua por segundo, 14 estanques para 225 mil litros cúbicos de agua y un ducto para trasladarla con mayor rapidez a la planta Las Vizcachas, donde se produce el agua potable.

El 22 de enero de ese año [2013], un millón 200 mil personas resultaron afectadas por aluviones en la zona cordillerana que incrementó el caudal del Río Maipo y su turbiedad alcanzó 45 mil Unidades de Turbiedad (UNT), cuando el límite es de 15 mil UNT para ser procesadas. A ello se sumó lo acontecido el 9 y 10 febrero del mismo período, cuando 25 comunas quedaron sin agua potable por la misma razón.

No obstante, esto no tuvo efectos significativos porque en abril del 2016, el Río Maipo se desbordó nuevamente y dejó 29 comunas sin el recurso hídrico entre el 16 y 18 de abril. Este incidente afectó a cuatro millones de santiaguinos y ocurrió porque se produjeron a 3 mil 600 metros de altura sobre el nivel del mar, cuando lo habitual es que a 2 mil 500 metros caiga nieve. En esa oportunidad, el nivel de turbiedad del Río Maipo llegó hasta los 79 mil UNT.

“Nuestra primera fase que se inauguró en el año 2014, ha permitido sortear 10 eventos similares a este, pero no tan importantes y no tuvimos cortes de agua. Si esa primera fase no se hubiese inaugurado, hubiésemos tenido diez cortes más como el que hemos tenido ahora y eso afortunadamente no sucedió” (Eugenio Rodríguez, Aguas Andinas).

“Son seis estanques que se van a situar cerca de nuestra planta Las Vizcachas, donde lo que vamos a hacer ahí es guardar agua afuera del río de manera que cuando el agua venga con turbiedad, nosotros podamos dispondremos de esas aguas para poder seguir produciendo por 32 horas, a diferencia de la autonomía de nueve horas que tenemos hoy día”.

### Enero 2013 — corte de suministro, río Maipo

- Fechas: del 21 al 23 de enero de 2013.
- Tipo: corte de suministro.
- Causa según la fuente: no informada.
- Turbiedad máxima reportada: 45.000 UNT.
- Comunas afectadas por el corte: 19 (otras fuentes dicen 21).
- Confianza: alta.
- Detalle: aluvión en San Alfonso el 21 de enero; corte desde el 22 de enero.

#### Noticia: Febrero de 2013 y abril de 2016: Los otros cortes masivos de Aguas Andinas y las multas que ha debido pagar (Emol, 2017-02-27)

https://www.emol.com/noticias/Nacional/2017/02/27/846968/Febrero-de-2013-y-abril-del-2016-Los-otros-cortes-masivos-de-Aguas-Andinas-y-las-multas-que-ha-debido-pagar.html

El intendente de la Región Metropolitana, Claudio Orrego, explicó que si bien es anómalo ver lluvias a 4.500 metros de altura, ya que cuando en invierno son aproximadamente a mil, esto ya empieza a ser una situación normal que ha ocurrido en otras ocasiones.

El 22 de enero de 2013 se cortó el suministro de agua potable en diversos sectores de 19 comunas de la Región Metropolitana, lo que dejó 1.200.000 personas afectadas.

El corte se produjo por aluviones en la zona cordillera que aumentaron el caudal del Río Maipo y su turbiedad, la que alcanzó 45.000 Unidades de Turbiedad (UNT) cuando el máximo requerido es de 15.000 para poder ser procesada.

Solo días después y por la misma razón, el 9 y 10 de febrero del mismo año, 25 comunas de Santiago quedaron sin agua potable, lo que involucró esta vez a más de un millón de personas.

En 2008 las lluvias cordilleranas triplicaron el caudal del Río Maipo generando un corte masivo en la Región Metropolitana.

Sin embargo, este plan no dio abasto en abril del 2016, cuando volvió a aumentar el caudal y la turbiedad del Río Maipo, dejando a 29 comunas de la capital sin agua potable desde el 16 al 18 de abril. Este corte de suministro afectó a 4 millones de personas.

Las lluvias se produjeron a 3.600 metros de altura sobre el nivel del mar, cuando lo normal es que a 2.500 metros caiga nieve. En esa ocasión la turbiedad del Río Maipo alcanzó los 79.000 UNT.

#### Noticia: Después de tres días, volvió el agua potable a Santiago de Chile (Diario de Cuyo, 2013-01-23)

https://www.diariodecuyo.com.ar/noticias/despues-de-tres-dias-volvio-el-agua-potable-a-santiago-de-chile-716552.html

Chile, 23 de enero.- "Aguas Andinas informa que la totalidad del suministro que se encontraba interrumpido a raíz de la emergencia ha sido repuesto", dijo la compañía en un comunicado publicado en su página web.

La madrugada del martes más de dos millones de personas en Santiago de Chile se vieron afectadas por un corte de emergencia provocado por la contaminación del principal río abastecedor de la ciudad tras un fuerte aluvión de verano.

Según la empresa, el corte se produjo por la contaminación del río Maipo, el principal abastecedor de la capital chilena -de seis millones de habitantes-, tras un inesperado aluvión que se produjo la tarde del lunes en un sector cordillerano.

El barro arrastrado contaminó tres plantas de producción de agua potable, lo que obligó a cortar el suministro.

El alud de barro no dejó víctimas, aunque provocó la evacuación de más de 80 personas que se encontraban en el sector de San Alfonso, en la precordillera de Santiago.

### Febrero 2013 — corte de suministro, ríos Maipo y Mapocho

- Fechas: del 8 al 10 de febrero de 2013.
- Tipo: corte de suministro.
- Causa según la fuente: no informada.
- Comunas afectadas por el corte: 25.
- Confianza: alta.
- Detalle: corte desde la medianoche del 8 al 9 de febrero; en el Mapocho cerraron 16 plantas; servicio 100% repuesto el 10 de febrero. Emol cita 380.000 UNT, cifra dudosa.

#### Noticia: Aguas Andinas reconoce que corte de agua en comunas de Santiago podría extenderse hasta el lunes (El Mostrador, 2013-02-09)

https://www.elmostrador.cl/noticias/pais/2013/02/09/aguas-andinas-reconoce-que-corte-de-agua-en-comunas-de-santiago-podria-extenderse-hasta-el-lunes/

A la turbiedad presentada en el río Maipo se suma la del río Mapocho, lo cual ha significado el cierre de 16 plantas del suministro. A las 07:00 horas de este sábado se han sumado las comunas de Lo Barnechea, Las Condes y Vitacura, lo cual significa que el número de afectados llega al millón de usuarios.

Según las cifras de turbiedad del río Maipo registradas durante la noche del viernes y la madrugada de este sábado, duplican las mostradas hace 21 días.

De acuerdo a lo manifestado por Esquivel y que recoge radio Bío Bío, los nuevos índices de turbiedad retrasaron la entrada en funcionamiento de las plantas de agua, la que originalmente deberían haber iniciado su trabajo durante la madrugada de este sábado.

Esquivel también respondió a las denuncias de cortes anticipados al anuncio de la empresa, afirmando que el cierre de las válvulas comenzó a las 12:00 horas de la noche del viernes.

Los plazos establecidos por el ejecutivo son aleatorios, debido a que dependen de factores naturales ajenos a la empresa. Si las bombas no pueden comenzar a funcionar a las 12:00 de este sábado, o de producirse otro aluvión o nuevas lluvias que arrastren suciedades en la cordillera, significa inmediatamente la demora en la reposición de servicios, que podrían aplazar la operatividad completa para el día lunes.

Por su parte, la intendenta (S) Caterina Klein dijo a radio Cooperativa que son casi 4 millones de personas las afectadas por el corte del suministro en la Región Metropolitana, lo cual se traduce en 1.060.000 clientes.

«Como informamos durante la semana nos encontramos con alerta temprana preventiva debido a que las condiciones climáticas eran similares a las de la semana pasada. Esto no ocurría hace cinco años, que es una mezcla de causales, ya que estamos en sequía, el material de arriba en los cerros es seco, lluvias intensas en esta localidad en época de hielo», explicó.

#### Noticia: Aguas Andinas afirma que el servicio se ha restablecido en un 100% (El Dínamo, 2013-02-10)

https://www.eldinamo.cl/pais/2013/02/10/aguas-andinas-afirma-que-el-servicio-se-ha-restablecido-en-un-100/

La empresa Aguas Andinas afirmó que este domingo a las 19 horas se restableció el suministro de agua por completo, luego de cerca de 1 millón de clientes pasaran más de 24 horas sin el servicio.

“La empresa ya está haciendo trabajos de tres tipos: inversiones en pozos profundos, un estanque de abastecimiento adicional y un ducto que viene desde el embalse El Yeso hacia la planta Las Vizcachas. Esas tres obras ya están curso, algunas de ellas concluidas, y tendrán que finalizar en su totalidad en diciembre de 2013, según el cronograma” (Lucas Palacios, ministro de Obras Públicas subrogante).

### Diciembre 2015 — pico de turbiedad reportado, río Maipo

- Fechas: 30 de diciembre de 2015.
- Tipo: pico de turbiedad reportado (sin corte).
- Causa según la fuente: no informada.
- Confianza: media.
- Detalle: una remoción en masa en el río Colorado elevó la turbiedad; no hubo corte.

#### Noticia: Turbiedad en el río Maipo: Los nueve cortes masivos de suministro que ha protagonizado Aguas Andinas desde 2008 (Emol, 2017-04-21)

https://www.emol.com/noticias/Nacional/2017/04/21/855108/Turbiedad-del-rio-Maipo-Los-diez-cortes-masivos-de-suministro-que-ha-protagonizado-Aguas-Andinas-en-nueve-anos.html

Esas obras permitieron mantener la continuidad del suministro en casos de emergencia, como el ocurrido el 30 de diciembre del 2015, cuando un derrumbe en el río Colorado aumentó los niveles de turbiedad.

### Abril 2016 — corte de suministro, ríos Maipo y Mapocho

- Fechas: del 16 al 18 de abril de 2016.
- Tipo: corte de suministro.
- Causa según la fuente: tormenta cálida.
- Turbiedad máxima reportada: 65.000 UNT (Aguas Andinas vía T13; Emol reporta 79.000 UNT).
- Comunas afectadas por el corte: 27 (Emol dice 29).
- Confianza: alta.
- Detalle: corte desde las 12:00 del 16 de abril.

#### Noticia: Corte de agua potable afecta a 27 comunas de la Región Metropolitana (T13, 2016-04-16)

https://www.t13.cl/noticia/nacional/corte-emergencia-region-metropolitana

Esta mañana, la empresa de Aguas Andinas informó apartir de las 12:00 horas del día, se realizará un corte de agua no programado en 27 comunas de la Región Metropolitana, debido a la turbiedad que han presentado los ríos Mapocho y Maipo causa de las lluvias que afectan a la zona.

El horario de reposición del servicio será comunicado tan pronto como las condiciones del río permitan que las plantas de producción vuelvan a operar, aunque el gerente corportativo de Aguas Andinas, informó a través de radio Bío Bío que el corte podría durar al menos 24 horas.

Según la empresa, cerca de 800 mil clientes se verán afectadas con la suspensión del servicio.

En tanto, las comunas de la periferia del sector poniente no deberían tener problemas con el suministro, debido a que el servicio de agua potable de estas zonas no está relacionado con la producción proveniente del agua de los ríos, sino de napas subterráneas.

Aguas Andinas detalló que producto de las fuertes lluvias en la zona cordillerana, la turbiedades de los ríos Mapocho y Maipo alcanzaron niveles extremos, los que superaron a las 8:00 hrs. de hoy las 65.000 UNT (unidad de medición de turbiedad).

Ante esto la empresa procedió a cerrar sus plantas de producció.

#### Noticia: Casi todo Santiago se queda sin agua potable por al menos 24 horas (The Clinic, 2016-04-16)

https://www.theclinic.cl/2016/04/16/530400/

Aguas Andinas informó que debido a la turbiedad de los ríos Mapocho y Maipo se suspende el suministro de este inapreciable bien desde el mediodía de este sábado. Son 27 las comunas las afectadas, lo que implica un universo total de unos 800 mil clientes.

Según Aguas Andinas el nivel de turbiedad de los ríos Mapocho y Maipo alcanzaron máximos extremos, algo así como 65.000 UNT (unidad de medición de turbiedad).

### Febrero 2017 — corte de suministro, río Maipo

- Fechas: del 25 de febrero al 1 de marzo de 2017.
- Tipo: corte de suministro.
- Causa según la fuente: tormenta cálida.
- Turbiedad máxima reportada: 175.000 UNT, el 27 de febrero a la 01:30.
- Comunas afectadas por el corte: 30 (según Aguas Andinas y ONEMI; hay versiones de 33 y 38).
- Confianza: alta.
- Detalle: aluviones el 25 de febrero; corte desde el 26 de febrero; servicio 100% repuesto el 1 de marzo.

#### Noticia: [Minuto a Minuto] Aún hay problemas con la reposición del agua (Cooperativa, 2017-02-25)

https://www.cooperativa.cl/noticias/pais/tiempo/las-consecuencias-de-las-fuertes-lluvias-en-el-pais/2017-02-25/213827.html

Entradas del minuto a minuto, de la más antigua a la más reciente:

- Aguas Andinas: Frente meteorológico en alta cordillera aumentó intensidad de turbiedades
- Orrego: El nivel de turbiedad del río Maipo aumentó significativamente estas últimas dos horas
- Aguas Andinas: Sigue lloviendo en la alta cordillera, no podemos confirmar hora de reposición
- Onemi: Aguas Andinas mantiene el corte de agua en 30 comunas de la Región Metropolitana
- Aguas Andinas paralizó sus plantas de agua potable por altas turbiedades en el Río Maipo
- Confirmado: Se mantiene corte de agua para Santiago este lunes por turbiedad del río Maipo
- Aguas Andinas confirma que reinició "parcialmente" la producción de agua potable
- "Las turbiedades marcaron un peak de 175.000 UNT a la 01:30 y aún se mantienen altas, de manera que la capacidad de producción no está al 100 por ciento", informó la empresa.
- La Superintendencia confirmó que va mejorando la condición del Río Maipo y hay menos turbiedad.
- Corte de agua en la comuna de San Antonio afecta a 47 mil clientes, además se registran cortes en Cartagena
- Aguas Andinas: El proceso de reposición ha avanzado de forma más lenta que la prevista
- Superintendente de Servicios Sanitarios: Corte de agua obedece a un efecto climático
- Intendente Orrego: Hay 970 mil clientes de Aguas Andinas sin suministro de agua
- "Reposición servicio gradual hasta las 08:00 horas del martes", indicó intendente Orrego
- Aguas Andinas comenzó llenado de la red para iniciar la reposición masiva del suministro
- Corte en San Antonio y Cartagena se debe a la alta turbiedad de río Maipo
- Según el último reporte de Aguas Andinas, el 97 por ciento de los clientes de Santiago ya cuentan con agua potable
- Transcurridas 72 horas del corte, el suministro de agua potable aún no se normaliza del todo en la Región Metropolitana.
- [Radio en vivo] Superintendente de Servicios Sanitarios: Aguas Andinas informó a las 04:00 que se restablecía el 100%

#### Noticia: Aguas Andinas: reposición del agua potable dependerá de la turbiedad del Río Maipo (El Dínamo, 2017-02-26)

https://www.eldinamo.cl/pais/2017/02/26/aguas-andinas-reposicion-del-agua-potable-dependera-de-la-turbiedad-del-rio-maipo/

La turbiedad del Río Maipo producto de los aluviones que han afectado a la zona pre cordillerana de la Región Metropolitana provocó que Aguas Andinas suspendiera el suministro en 30 comunas, afectando a un millón y medio de clientes.

“El tiempo lo determina el río”, dijo Rodríguez, asegurando que una vez que baje la turbiedad la empresa retomará inmediatamente el proceso para iniciar la reposición del servicio. Sin embargo, advirtió que una vez que ello ocurra “necesitamos de una cantidad de al menos ocho horas para rellenar los estanques y la red”, consignó La Tercera.

### Abril 2017 — corte de suministro, río Maipo

- Fechas: del 20 al 21 de abril de 2017.
- Tipo: corte de suministro.
- Causa según la fuente: no informada.
- Turbiedad máxima reportada: 100.000 UNT (pie de foto de Emol).
- Comunas afectadas por el corte: 27.
- Confianza: alta.
- Detalle: corte el 21 de abril, de 02:00 a 23:57.

#### Noticia: MAPA | Orrego y Aguas Andinas anuncian corte de suministro en 27 comunas de Región Metropolitana (El Dínamo, 2017-04-20)

https://www.eldinamo.cl/pais/2017/04/20/orrego-y-aguas-andinas-anuncian-corte-de-suministro-en-27-comunas-de-region-metropolitana/

El intendente Claudio Orrego y la empresa Aguas Andinas confirmaron que a partir de las 02:00 horas de este viernes se cortará el suministro en 27 comunas de la Región Metropolitana.

Según explicaron los involucrados, el nivel de turbiedad del río Maipo, provocado por las lluvias en el sector cordillerano, harán que se paralicen las plantas de agua potable de la compañía.

A través de un comunicado, Aguas Andinas justificó la medida señalando que “la turbiedad en el Río Maipo alcanzó a niveles extremos, por que se tuvo que paralizar su producción y comenzó a utilizar sus reservas de agua para mantener el servicio”.

#### Noticia: [Minuto a Minuto] Aguas Andinas informa que el 100% de los clientes afectados por el corte ya cuentan con agua (Meganoticias, 2017-04-21)

https://www.meganoticias.cl/nacional/195170-minuto-a-minuto-lluvias-afectan-a-la-zona-central-del-pais.html

Entradas del minuto a minuto, de la más antigua a la más reciente (20 y 21 de abril):

- 19:15 Aguas Andinas se declara en "estado de pre emergencia" ante aumento en la turbiedad del río Maipo. Además, recomendaron a los usuarios juntar agua en caso de un próximo corte del suministro en la Región Metropolitana.
- 19:43 Bruna: Los estanques de emergencia de Aguas Andinas están en un 100% y los que abastecen a Santiago en un 90%.
- 21:29 Orrego: la turbiedad del agua subió considerablemente.
- 21:31 El superintendente de Servicios Sanitarios, Ronaldo Bruna anuncia que el corte empezar{a entre 2 a 3 de la mañana.
- 21:33 Aguas Andinas confirma corte de agua en 27 comunas de Santiago
- 01:49 La Onemi decretó Alerta Roja para las 27 comunas que sufrieron el corte de agua en la Región Metropolitana.
- 07:38 Aguas Andinas informa que reinició parcialmente la producción de agua potable.
- 11:30 "Aquí no hay falla de planta, lo que hay es un río que no entrega agua en calidad necesaria (...) cada vez que el río Maipo traiga las condiciones que trae hoy día, será necesario hacer un corte de agua potable (...) la respuesta la tiene la condición del agua del río Maipo", dijo [el representante de Aguas Andinas].
- 15:10: Aguas Andinas informa que se reestableció el servicio de agua potable a otros 175.000 hogares.
- 17:06 El intendente de la región Metropolitana, Claudio Orrego, informó que continúan bajando los niveles de turbiedad en cauces cordilleranos y ya el 76% hogares afectados cuentan con agua.

### Febrero 2018 — alerta, río Maipo

- Fechas: del 6 al 8 de febrero de 2018.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: deshielo.
- Confianza: media.
- Detalle: Alerta Temprana Preventiva (ATP) de Aguas Andinas por deshielo. El comunicado del 8 de febrero dice que la alerta regía "desde el viernes", es decir, desde el 2 de febrero de 2018 (la tabla `eventos_prensa.csv` todavía dice 6 de febrero).

#### Noticia: Aguas Andinas mantiene alerta temprana preventiva mientras no se disipen efectos de lluvias en la cordillera (Mediabanco, comunicado de Aguas Andinas, 2018-02-06)

https://www.mediabanco.com/?p=70043

Santiago, 6 de febrero 2018, 9.00 horas. Aguas Andinas informó que se mantendrá en estado de Alerta Temprana Preventiva mientras no se disipen los efectos sobre el río Maipo de las recientes lluvias en la alta cordillera y persistan los pronósticos de altas temperaturas.

La empresa enfatizó que, si bien aumentaron los niveles de turbiedad en el río Maipo, el abastecimiento de agua potable a los clientes funciona con absoluta normalidad, sin embargo, se mantiene monitoreando la situación en caso de que la turbiedad aumente.

#### Noticia: Aguas Andinas cancela alerta temprana preventiva por efectos de deshielos en la alta cordillera (Mediabanco, comunicado de Aguas Andinas, 2018-02-08)

https://www.mediabanco.com/aguas-andinas-cancela-alerta-temprana-preventiva-por-efectos-de-deshielos-en-la-alta-cordillera/

Santiago, 8 de febrero de 2018, 10.30 horas. Aguas Andinas informó que se cancela el estado de Alerta Temprana Preventiva en el que se encontraba desde el viernes, debido a una mejora de los efectos que tuvieron las altas temperaturas en la Cordillera de la Región Metropolitana.

Durante los días en que se ha mantenido el estado de alerta, la empresa ha realizado un arduo trabajo para evitar que la producción de las plantas de agua potable se vea afectada, sobre todo por las altas cantidades de lodo que han sido extraídos del cauce del río Maipo. En sólo cinco días, se han sacado alrededor de 450.000 m3 de lodo, lo que equivale a un volumen que permitiría llenar 180 piscinas olímpicas.

### Enero 2020 — alerta, río Maipo

- Fechas: desde el 3 de enero de 2020 (fin no verificado).
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: deshielo.
- Confianza: media.
- Detalle: ATP por altas temperaturas en la cordillera; suministro normal.

#### Noticia: Aguas Andinas decreta alerta temprana preventiva por altas temperaturas en la cordillera (Diario Financiero, 2020-01-03)

https://www.df.cl/empresas/medio-ambiente/aguas-andinas-decreta-alerta-temprana-preventiva-por-altas-temperaturas

Aguas Andinas informó esta tarde que se declaró en Alerta Temprana Preventiva como consecuencia de las elevadas temperaturas que se han registrado en la alta Cordillera de la Región Metropolitana y que se mantendrían durante los próximos dos días. Esto ha llevado al río Maipo a experimentar turbiedad en su caudal, debido a los deshielos.

La compañía agregó que en estos momentos el abastecimiento de agua potable se mantiene operando bajo total normalidad.

### Enero 2021 — alerta, ríos Maipo y Mapocho

- Fechas: del 30 de enero al 2 de febrero de 2021.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: tormenta cálida (río atmosférico).
- Turbiedad máxima reportada: 153.000 UNT en el Mapocho; más de 61.000 UNT en el Maipo.
- Confianza: alta.
- Detalle: no hubo corte masivo, solo uno parcial de unos 4.000 hogares en Lo Barnechea (Mapocho). Las cifras de UNT vienen de un comunicado de Aguas Andinas del 4 de febrero de 2021 reproducido en Mediabanco, visto solo en extractos del buscador.

#### Noticia: Informan turbiedad del Río Maipo: Intendente dice que sin estanques de Pirque "en estos momentos no tendríamos agua" (Emol, 2021-01-30)

https://www.emol.com/noticias/Nacional/2021/01/30/1010831/Aguas-Andinas-alerta-rio-atmosferico.html

Aguas Andinas informó esta mañana que adhirió a la Alerta Temprana Preventiva decretada por la autoridad para la Región Metropolitana. Ello, como consecuencia de las lluvias que se han registrado en la Cordillera con motivo del inusual fenómeno denominado "río atmosférico" y las altas turbiedades experimentadas en el río Maipo.

Esto, ocurrió debido a que "la isoterma, el límite de donde parte la nieve y comienza el agua fue muy alto, sobre los 3 mil metros anoche. Donde cae nueve, anoche cayó agua y lavó el cerro. Ese lodo cayó al curso del agua y provocó turbiedad, lo que impide sacarla del río y entregarla" (Felipe Guevara, intendente de la RM).

Para poner en perspectiva la situación, explicó que "la ciudad de Santiago se abastece en un 80% de agua potable del río Maipo". Por eso, y frente a las lluvias que se pronostican para las 18.00 horas, "eso podría aumentar la turbiedad del río".

"La producción de agua continúa, pero por los estanques de Pirque. La producción continúa igual por las próximas 34 horas desde las 8 de la mañana. El origen no es el río, sino los estanques que se han llenado para emergencias como esta (...) están rindiendo sus frutos y permiten autonomía de 34 horas agua potable", agregó.

En ese sentido, Guevara reconoció que "si no tuviéramos los estanques no tendríamos agua en estos momentos, habría dejado de producirse ya que no es posible captar agua del río Maipo".

El Plan de Resiliencia, ha sido desarrollado la compañía para enfrentar los efectos del cambio climático, reforzando la continuidad del suministro en la zona abastecida principalmente por el río Maipo. Esto ha permitido pasar de 4 horas en 2011 a las 34 horas de autonomía actualmente.

La primera fase entró en operación en 2013, con una inversión de $47 mil millones y la construcción de 7 nuevos pozos y 14 estanques de almacenamiento de agua potable. Esta fase permitió pasar de 4 a 9 las horas de respaldo en la ciudad.

La segunda etapa inició su operación en 2018 y consideró una inversión total de $ 15 mil millones. Esto permitió pasar de 9 a 11 las horas de autonomía de Santiago.

Finalmente, en febrero de 2020 se iniciaron las operaciones en los Mega Estanques de Pirque con una inversión por $ 77,5 mil millones, que permitió pasar de 11 a 34 las horas de autonomía de Santiago frente a emergencias climáticas.

La última fase del plan de resiliencia avanza para llegar a las 48 horas de autonomía de suministro, entre los cuales se encuentran Lo Pozos de Cerro Negro-Lo Mena y el proyecto Pirque-El Manzano.

#### Noticia: [Minuto a Minuto] Sigue el riesgo de un corte masivo de agua en Santiago (Cooperativa, 2021-02-01)

https://www.cooperativa.cl/noticias/pais/tiempo/sigue-el-riesgo-de-un-corte-masivo-de-agua-en-santiago/2021-02-01/155145.html

Entradas del minuto a minuto, de la más antigua a la más reciente:

- Director de gestión de servicios de Aguas Andinas, Eugenio Rodríguez: De las 38 comunas que anunciamos ayer que podrían verse afectadas por un corte, 37 se liberan de esa restricción hasta mañana a las 08:00
- Aguas Andinas: Si en las próximas tres o cuatro horas podemos recuperar la planta San Enrique, no va a ser necesario el corte en el sector El Huinganal, en Lo Barnechea, lo que vamos a informar a las 20:00 horas
- Director de Gestión de Servicio de Aguas Andinas, Eugenio Rodríguez: Los niveles de turbiedad que hemos visto en los ríos Mapocho y Maipo son inéditos
- Director de Gestión de Servicio de Aguas Andinas, Eugenio Rodríguez: Miramos muchas décadas atrás y no hay registros de que hayan caído 90 mm de agua en el embalse El Yeso
- Director de Gestión de Servicio de Aguas Andinas, Eugenio Rodríguez: Al río Maipo lo vemos mucho más robusto que el Mapocho, que ha estado muy inestable y es el que no ha querido reaccionar como quisiéramos
- Unos 4.000 hogares de la comuna de Lo Barnechea se encuentran sin suministro de agua potable a partir de las 21:00 horas de hoy y por un período no superior a 24 horas.
- Aguas Andinas descartó suspensiones del suministro "debido a la mejora en las condiciones del río Maipo", aunque se mantiene la alerta amarilla en la Región Metropolitana
- [En vivo] Aguas Andinas: Turbiedad del Río Maipo puede generar agua potable, pero no es posible llenar los mega estanques

### Diciembre 2021 — alerta, río Maipo

- Fechas: del 24 al 28 de diciembre de 2021.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: deshielo.
- Confianza: alta.
- Detalle: ATP por calor en la cordillera; Aguas Andinas usó los megaestanques de Pirque; no hubo corte.

#### Noticia: Aguas Andinas en Alerta Temprana Preventiva por turbiedad en caudal del río Maipo ocasionado por el calor (Meganoticias, 2021-12-24)

https://www.meganoticias.cl/nacional/362636-aguas-andinas-alerta-temprana-preventiva-turbiedad-rio-maipo-24-12-2021.html

La empresa Aguas Andinas se declaró en Alerta Temprana Preventiva en la Región Metropolitana, como consecuencia de las altas temperaturas registradas en la Cordillera de Los Andes, ocasionando turbiedades en el caudal del río Maipo, desde el cual se abastece gran parte de la población.

A través de un comunicado de prensa, la compañía informó que el suministro de agua potable hacia los hogares se encuentra operando con normalidad y que ha activado su plan de continuidad operacional, recurriendo a la infraestructura de respaldo que ha desplegado a través de su plan de resiliencia en los últimos años.

El ejecutivo detalló que "en los últimos días, y también se espera para los próximos, hemos tenido altas temperaturas en la cordillera, lo que ha hecho que el río Maipo haya aumentado su nivel de turbiedad" (Eugenio Rodríguez, Aguas Andinas).

#### Noticia: Aguas Andinas se declara en alerta temprana preventiva por altas temperaturas que han generado turbiedad (Radio Agricultura, 2021-12-24)

https://www.radioagricultura.cl/noticias/nacional/aguas-andinas-se-declara-en-alerta-temprana-preventiva-por-altas-temperaturas-que-han-generado-turbiedad_20211224/

Aguas Andinas informó este viernes que se declaró en Alerta Temprana Preventiva en la Región Metropolitana como consecuencia de las altas temperaturas que se han registrado en la cordillera, ocasionando turbiedades en el caudal del rio Maipo desde el cual se abastece parte importante de la ciudad.

### Enero 2022 — alerta, ríos Maipo y Mapocho

- Fechas: del 9 al 18 de enero de 2022.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: deshielo.
- Turbiedad máxima reportada: más de 10.000 UNT en el Maipo.
- Confianza: alta.
- Detalle: ATP de ONEMI el 11 de enero; superada el 18 de enero.

#### Noticia: Alerta Temprana en la RM por turbiedad en ríos: Aguas Andinas ya utiliza reservas de agua potable (BioBioChile, 2022-01-11)

https://www.biobiochile.cl/noticias/nacional/region-metropolitana/2022/01/11/alerta-temprana-en-la-rm-por-turbiedad-en-rios-aguas-andinas-ya-utiliza-reservas-de-agua-potable.shtml

Según informó la sanitaria Aguas Andinas, durante los últimos días ha habido turbiedad en los caudales de los ríos Maipo y Mapocho. A ello se suma a que se pronostican lluvias convectivas en la cordillera para las próximas horas.

En específico, Onemi reportó que en el río Maipo “se ha producido turbiedad alta desde el 9 de enero, con un promedio de 24 horas móviles por sobre 4.000 unidades nefelométricas de turbidez (UNT) y peak por sobre las 10.000 UNT, lo que afecta los procesos de producción habituales de agua potable de la empresa sanitaria”.

Aguas Andinas agregó que el suministro hacia los hogares opera en forma normal ya que que se comenzó a utilizar el agua de los megaestanques de Pirque. Se trata de reservas del recurso líquido que permiten dar una autonomía de 34 horas de funcionamiento en caso de que no se pueda producir agua.

#### Noticia: Aguas Andinas da por superado evento de turbiedad para la Región Metropolitana (T13, 2022-01-18)

https://www.t13.cl/noticia/nacional/aguas-andinas-turbiedad-region-metropolitana-18-01-2022

La empresa Aguas Andinas informó este martes que dio por superado el evento de turbiedad extrema que se registró en los ríos hace una semana debido a las altas temperaturas en la cordillera, en la región Metropolitana.

Específicamente, el hecho afectó a los caudales de los ríos Maipo y Mapocho, los dos principales efluentes desde los cuales se abastece la ciudad.

"Informamos del paso a normalidad para el evento de turbiedad y que se encuentran recuperadas las reservas de agua para abastecer a la Región Metropolitana", señaló Aguas Andinas a través de Twitter.

### Enero 2023 — alerta, ríos Maipo y Mapocho

- Fechas: del 7 al 11 de enero de 2023.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: convectiva.
- Turbiedad máxima reportada: 90.000 UNT el 9 de enero (Senapred).
- Confianza: alta.
- Detalle: ATP de Senapred; corte parcial en Chicureo el 10 de enero. La Tercera ubica el inicio de la alerta de Aguas Andinas el sábado 7 de enero, y Pauta el 9 de enero.

#### Noticia: Turbiedad en río que abastece a la RM: Senapred aclara que "no ha sido necesario efectuar cortes de suministro" (Meganoticias, 2023-01-09)

https://www.meganoticias.cl/nacional/401885-senapred-cortes-de-agua-potable-region-metropolitana-turbiedad-rio-09-01-2023.html

Durante la jornada de este lunes, el Servicio Nacional de Prevención y Respuestas ante Desastres (Senapred) declaró Alerta Temprana Preventiva regional por la turbiedad del Río Maipo, el cual abastece de agua potable a la capital.

La entidad precisó que "se ha producido una alta turbiedad en las aguas de la cuenca del Río Maipo, llegando a 90.000 UNT el día 09 de enero, debido a las precipitaciones ocurridas en cordillera generando la activación de quebradas que depositaron sedimentos en los ríos Maipo y Mapocho".

Eso sí, esto aún no afecta el abastecimiento del "vital elemento" a la zona, pues el Senapred remarcó que "se procedió a utilizar las reservas de agua de los estanques de seguridad de Pirque, para asegurar la correcta distribución de agua potable a la población".

#### Noticia: ¿Por qué aumentó la turbiedad en el río Mapocho? (La Tercera, 2023-01-11)

https://www.latercera.com/nacional/noticia/por-que-aumento-la-turbiedad-en-el-rio-mapocho/NTP67TMYABGABOTSZVZV3GOLVQ/

Desde el pasado sábado 7 de enero, Aguas Andinas se declaró en Alerta Temprana Preventiva por la persistencia en la turbiedad de los ríos Mapocho y Maipo, pausando la producción de agua potable al ser los principales proveedores de las plantas de procesamiento.

El río Mapocho es el principal abastecedor de agua potable para las comunas de Las Condes, Vitacura y lo Barnechea.

Desde Aguas Andinas se explicó que la causa se debió a los deslizamientos de tierra causados por las fuertes lluvias que azotaron a la zona precordillerana: ello fue lo que gatilló que las aguas de estos ríos presentaran un aumento alarmante en su turbiedad, obligando a decretar la alerta temprana preventiva y paralizando el funcionamiento de sus plantas.

### Junio 2023 — alerta, ríos Maipo y Mapocho

- Fechas: del 22 de junio al 1 de julio de 2023.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: tormenta cálida.
- Confianza: alta.
- Detalle: no fue corte. Hubo alerta roja y un corte anunciado para 34 comunas, que se canceló el 24 de junio (gob.cl, Chocale y CNN). La alerta amarilla se canceló el 1 de julio.

#### Noticia: Estas son las 34 comunas que tendrían corte de agua informadas por Aguas Andinas (gob.cl)

https://www.gob.cl/noticias/comunas-corte-agua-intenso-sistema-frontal-historico-lluvias-rios-alta-turbiedad/

El intenso sistema frontal por el que atraviesan diferentes regiones de la zona centro sur de nuestro país ha llevado a Aguas Andinas a tomar la decisión de evaluar un corte de agua para 34 comunas de la Región Metropolitana,

La suspensión temporal del suministro se debe a las condiciones de turbiedad del agua del río Maipo y río Mapocho por las históricas lluvias que han precipitado en el embalse El Yeso.

Sin embargo, esta noche el Presidente anunció la suspensión del corte de agua.

Si bien, en un inicio, el corte de agua se llevaría a cabo este sábado 24 de junio a las 14 horas, de acuerdo a la información proporcionada por la compañía Aguas Andinas, las autoridades han informado su postergación para las 20 horas del mismo día.

#### Noticia: Cancelan corte de agua potable en la Región Metropolitana (Chócale, 2023-06-25)

https://chocale.cl/2023/06/cancelan-corte-de-agua-potable-en-la-region-metropolitana/

Aguas Andinas y el Ministerio de Obras Públicas (MOP) cancelaron el corte del suministro de agua, previsto para las 20:00 horas de este sábado, en 34 comunas de la Región Metropolitana.

Eugenio Rodríguez, director de Clientes de la compañía, explicó: "Considerando la evolución sostenida en las condiciones del río durante las últimas 5 horas, lo que permitió retomar la producción de agua potable directamente desde el río Maipo, estamos en condiciones de descartar la suspensión del servicio programado para las 20 horas de hoy".

No obstante, se mantiene la Alerta Roja. Aguas Andinas subraya la necesidad de continuar con el consumo responsable hasta recuperar el 25% de sus reservas de agua y subsanar algunos daños ocasionados en su captación por la crecida de los ríos durante el frente climático extremo.

Aseguró que el corte de agua potable pudo evitarse "principalmente debido al consumo responsable de la población y al mejoramiento de las condiciones climáticas que permitieron disminuir los niveles de turbiedad del Río Maipo" (Jessica López, ministra de Obras Públicas).

### Agosto 2023 — alerta, ríos Maipo y Mapocho

- Fechas: desde el 23 de agosto de 2023 (fin no verificado).
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: no informada.
- Confianza: alta.
- Detalle: ATP de Senapred y Aguas Andinas; más de 100 mm en 24 horas en la cordillera.

#### Noticia: Sistema frontal en la RM: Declaran Alerta Temprana Preventiva por turbidez en la cuenca del río Maipo (T13, 2023-08-23)

https://www.t13.cl/noticia/nacional/sistema-frontal-rm-alerta-temprana-preventiva-turbidez-rio-maipo-23-8-2023

A través de un reporte oficial, señalaron que "de acuerdo con la información proporcionada por la Dirección Regional Metropolitana de Senapred y la empresa de servicios sanitarios Aguas Andinas, se registra un peak de turbidez en la cuenca del Río Maipo, que ha hecho necesario la descarga de los estanques de seguridad de Pirque para mezcla en la producción de agua potable".

De igual forma, y conforme a lo validado por el organismo junto con la Superintendencia de Servicios Sanitarios (SISS), de momento "no se requiere efectuar cortes del suministro de agua potable hacia la población".

#### Noticia: "Hemos comenzado a utilizar nuestras reservas": Aguas Andinas emite Alerta Temprana Preventiva por turbiedad en ríos Maipo y Mapocho (The Clinic, 2023-08-23)

https://www.theclinic.cl/2023/08/23/aguas-andinas-alerta-region-metropolitana-agua-potable-turbiedad-rio-maipo-mapocho/

Sobre esto además detallaron que debido a las precipitaciones durante las últimas 12 horas han caído más de 40 milímetros de agua en la capital.

Sin embargo, advirtieron que debido a “los efectos derivados del evento climático, ha activado su plan de continuidad operacional para reforzar la producción de agua potable y ha recurrido desde horas de la madrugada a la infraestructura de reserva que ha desplegado en los últimos años en el marco de su plan de resiliencia, entre ellos, los Mega Estanques de Pirque, con lo que ha comenzado a hacer uso de las 37 horas de autonomía hídrica”.

### Noviembre 2023 — alerta, ríos Maipo y Mapocho

- Fechas: del 10 al 11 de noviembre de 2023.
- Tipo: alerta (sin corte masivo).
- Causa según la fuente: tormenta cálida (isoterma sobre 3.000 m).
- Confianza: alta.
- Detalle: ATP de Aguas Andinas, cancelada el 11 de noviembre. Aguas Andinas dijo entonces que era la "duodécima vez" que usaba los megaestanques de Pirque desde 2020.

#### Noticia: Aguas Andinas declara Alerta Temprana Preventiva en la RM por turbiedad en los cauces de ríos Maipo y Mapocho (24 Horas, 2023-11-10)

https://www.24horas.cl/actualidad/nacional/lluvia-en-santiago-aguas-andinas-declara-alerta-temprana-preventiva-por

Aguas Andinas informó recientemente la declaración de Alerta Temprana Preventiva en la Región Metropolitana debido a episodios de turbiedades registrados en los cauces de los ríos Maipo y Mapocho por las lluvias registradas este viernes.

En un comunicado explicó que la medida se tomó "como consecuencia del fenómeno climático que se ha dado tanto en la cordillera como en la ciudad, con intensas precipitaciones, acompañadas de una isoterma cero superior a los 3.000 metros en la montaña".

"Sin embargo, con la información disponible en este momento, estimamos que el suministro no se vería impactado en la ciudad, gracias al uso de su infraestructura de respaldo, como los mega estanques de Pirque y Pozos de Cerro Negro-Lo Mena que entregan una autonomía hídrica de 37 horas", agregó.

#### Noticia: Aguas Andinas cancela Alerta Temprana Preventiva tras disminución de turbiedad (Radio Agricultura, 2023-11-11)

https://www.radioagricultura.cl/nacional/2023/11/11/aguas-andinas-cancela-alerta-temprana-preventiva-tras-disminucion-de-turbiedad/

Luego de inusuales lluvias registradas en las últimas horas, y que llevaron a Aguas Andinas a utilizar parte de sus reservas, la compañía anunció que da por superada la situación, al registrarse disminuciones en las turbiedades de los ríos Maipo y Mapocho y retomar la normal producción de agua potable en sus plantas.

La compañía por duodécima vez desde su inauguración en 2020 recurrió al uso de los Megaestanques de Pirque, infraestructura que dispone de 1.500 millones de litros y que junto a los Pozos de Cerro Negro – Lo Mena entregan 37 horas de autonomía a la Región Metropolitana. Con todo lo anterior, Aguas Andinas, da por superado este último evento climático, el cual trajo un volumen de lluvias en noviembre, que no se veían hace más de una década en la Región Metropolitana.

### Octubre 2026 — pico de turbiedad reportado, río Mapocho

- Fechas: desde el 8 de octubre de 2026 (fin no informado).
- Tipo: pico de turbiedad reportado (sin corte).
- Causa según la fuente: tormenta cálida ("isoterma muy alta", según The Clinic del 8 de octubre de 2026 sobre el aluvión de San Carlos).
- Confianza: media.
- Detalle: cierre de la compuerta del Mapocho y uso de reservas; no hubo corte.

#### Noticia: Gobierno pidió a santiaguinos "uso responsable del agua", aunque no debería haber corte (Cooperativa, 2026-10-08)

https://www.cooperativa.cl/noticias/pais/desastres-naturales/inundaciones/gobierno-pidio-a-santiaguinos-uso-responsable-del-agua-aunque-no/2026-10-08/210833.html

El delegado presidencial metropolitano, Germán Codina, pidió hacer "uso responsable del agua" en Santiago, debido a la turbiedad del Río Mapocho causada por las intensas lluvias de esta semana, aunque descartó -por ahora- que se vaya a producir un corte en la capital.

"Hasta el momento, no debiera haber corte de suministro de agua potable. Sin embargo, la empresa (Aguas Andinas) sí ha informado que la turbiedad del Río Mapocho ha motivado el cierre de la compuerta de ingreso de agua, para efectos de potabilizar. Por lo tanto, en este minuto están comenzando a utilizar los estanques de reserva", explicó durante un punto de prensa en la comuna de Las Condes este jueves.

#### Noticia: Gobierno pidió a santiaguinos "uso responsable del agua", aunque no debería haber corte (Radio La Señal, 2026-10-09)

https://radiolasenal.cl/gobierno-pidio-a-santiaguinos-uso-responsable-del-agua-aunque-no-deberia-haber-corte/

Reproduce la misma nota de Cooperativa; no es una fuente independiente.

## Vacíos y eventos excluidos

- 1990–2007: no hay prensa digital indexada. Bustos (2011) registra los eventos de 1997 a 2008.
- 2019, 2024 y 2025 quedaron sin eventos. No se encontró ninguno, lo que no prueba que no los haya. Entre 2020 y 2023 hay unos 7 eventos, pero Aguas Andinas habló de 12 usos de los megaestanques en ese período, así que faltan unos 5 eventos menores (alertas sin prensa). Además, Aguas Andinas dijo en 2017 que la primera fase de obras (2014) le permitió sortear "10 eventos similares" sin corte, que tampoco están en la prensa.
- Se excluyeron las alertas preventivas sin turbiedad observada: la ATP del 9 de mayo de 2017 (emitida ante un pronóstico) y la de julio de 2026 (Aguas Andinas descartó turbiedad).
