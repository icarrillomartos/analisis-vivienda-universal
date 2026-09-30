# Ficha de datos — Parque de viviendas, suelo y capacidad del sector de la construcción

Fuentes exclusivamente oficiales (INE, MIVAU/antiguo Fomento, Sistema de Información Urbana). Todas las descargas originales están en `raw/`; los CSV limpios/derivados están en `limpio/`; los scripts de procesamiento en `scripts/`. Fecha de recopilación: 28/09/2026.

---

## 1. Censo de Población y Viviendas 2021 (INE) — parque por tipo

### 1.1 Total nacional

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Viviendas totales | 26.626.315 | viviendas | 2021 | INE | Censo 2021, tabla jaxi tpx=59520 | https://www.ine.es/jaxi/Tabla.htm?tpx=59520 | raw/censo2021/59520_viviendas_tipo_ccaa_provincia_tamaño_municipio.csv | Total Nacional, tamaño municipio=Total |
| Viviendas principales | 18.539.223 | viviendas | 2021 | INE | ídem | ídem | ídem | |
| Viviendas no principales | 8.087.092 | viviendas | 2021 | INE | ídem | ídem | ídem | Incluye secundarias + vacías, ver 1.3 |
| Viviendas no principales — secundarias | 8.087.092 (nacional, ver nota) | viviendas | 2021 | INE | tpx=59525 "Total viviendas familiares convencionales por tipo de vivienda" | https://www.ine.es/jaxi/Tabla.htm?tpx=59525 | raw/censo2021/59525_viviendas_tipo_por_municipio_nacional.csv | Esta tabla solo separa Principal/No principal a nivel de cada municipio; el desglose secundaria/vacía en detalle solo está publicado para municipios >2.000 hab (ver 1.3) y a nivel nacional agregando esos municipios. |

### 1.2 Por provincia (Total / Principal / No principal)

Fuente: INE, Censo 2021, tabla jaxi **tpx=59520** "Viviendas familiares (convencionales y alojamientos) según tamaño del municipio por tipo de vivienda" (dimensión Comunidad Autónoma y Provincia, filtrado a tamaño de municipio = Total). URL: https://www.ine.es/jaxi/Tabla.htm?tpx=59520. Archivo: `raw/censo2021/59520_viviendas_tipo_ccaa_provincia_tamaño_municipio.csv` → tabla limpia completa (52 provincias) en `limpio/censo2021_viviendas_total_principal_noprincipal_ccaa_provincia.csv`.

Ejemplo (provincias de las 6 ciudades pedidas):

| provincia | Total | Principal | No principal |
|---|---|---|---|
| Madrid | 2.957.295 | 2.546.843 | 410.452 |
| Barcelona | 2.597.046 | 2.197.826 | 399.220 |
| Valencia/València | 1.488.908 | 1.030.071 | 458.837 |
| Sevilla | 913.014 | 723.494 | 189.520 |
| Zaragoza | 543.799 | 395.356 | 148.443 |
| Málaga | 996.566 | 660.344 | 336.222 |

Notas: el Censo 2021 (a diferencia de 2011) no publica de forma predefinida el desglose provincial secundaria/vacía; solo ofrece Principal/No principal a nivel provincia. El desglose fino (secundaria vs. vacía) existe a nivel de cada municipio de >2.000 habitantes (tabla p06/10mun00.px) y a nivel nacional.

### 1.3 Municipios solicitados (Madrid, Barcelona, Valencia, Sevilla, Zaragoza, Málaga) — desglose completo

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Madrid — total / principal / secundaria / vacía | 1.593.245 (aprox., ver csv) total; ver detalle | viviendas | 2021 | INE | Censo 2021, path t20/e244/viviendas/p06/l0/10mun00.px | https://www.ine.es/jaxi/Tabla.htm?path=/t20/e244/viviendas/p06/l0/&file=10mun00.px | raw/censo2021/10mun00_tipo_detallado_municipios_mas2000hab.csv y limpio/censo2021_viviendas_tipo_detallado_6_municipios.csv | Tabla municipal (municipios >2.000 hab) con categorías "2.1 Total viviendas principales", "2.21 Viviendas secundarias", "2.22 Viviendas vacías" |
| Barcelona, Valencia, Sevilla, Zaragoza, Málaga — ídem | ver csv | viviendas | 2021 | INE | ídem | ídem | ídem | |

Valores extraídos (viviendas vacías, columna "2.22 Viviendas vacias" del CSV limpio) — Madrid: 153.101; Barcelona: 88.259; Valencia: 57.193; Sevilla: 48.178; Zaragoza: 35.136; Málaga: 28.410. El desglose completo (total, principales, secundarias, vacías, colectivas) de los 6 municipios está en `limpio/censo2021_viviendas_tipo_detallado_6_municipios.csv`.

---

## 2. Superficie útil y número de habitaciones (Censo 2021)

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Viviendas principales por tramo de superficie útil x nº de habitaciones (nacional) | ver tabla cruzada | viviendas | 2021 | INE | Censo 2021, tpx=56829 | https://www.ine.es/jaxi/Tabla.htm?tpx=56829 | raw/censo2021/56829_superficie_habitaciones_nacional_tamano_municipio.csv → limpio/censo2021_superficie_habitaciones_nacional.csv | Tramos disponibles: "Hasta 75 m²", "De 76 a 90 m²", "De 91 a 120 m²", "Más de 120 m²". El INE **no publica un tramo específico 40-50 m²**; es el hueco más fino disponible. |
| ídem, por municipio (todas las capitales) | ver csv | viviendas | 2021 | INE | tpx=56877 | https://www.ine.es/jaxi/Tabla.htm?tpx=56877 | raw/censo2021/56877_superficie_habitaciones_por_municipio.csv | Igual granularidad de tramos que el nacional |

**Estimación aproximada solicitada** ("≥40-50 m² útiles con dormitorio, salón, cocina y baño" ≈ al menos 2 estancias): viviendas principales en el tramo "Hasta 75 m²" con 2 o más habitaciones = **4.844.511** (de 5.581.436 viviendas en ese tramo). Sumando todos los tramos ≥76 m² (que sí garantizan superficie suficiente) = **13.228.611** viviendas (76-90m²: 4.770.091 + 91-120m²: 5.022.978 + >120m²: 3.435.542), es decir el **70,3%** del parque principal (18.810.046 según esta tabla censal). Esto es una aproximación por rangos, no una cifra exacta al corte de 40-50 m².

---

## 3. Estimación del parque de viviendas más reciente (MIVAU) y antigüedad (Censo 2021)

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Parque total de viviendas (España) | 27.099.556 | viviendas | 2025 (estimación anual) | MIVAU | Boletín estadístico, "Estimación del Parque de Viviendas", Tabla 2 | https://apps.fomento.gob.es/BoletinOnline2/sedal/33102000.XLS | raw/mivau/33102000.xls → limpio/mivau_parque_viviendas_tipo_ccaa_provincia_2001_2025.csv | Serie 2001-2025 por CCAA y provincia |
| — Viviendas principales | 19.571.428 | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| — Viviendas no principales | 7.528.128 | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Parque por provincia, ej. Madrid | 3.054.762 total / 2.699.021 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | Provincia = "Madrid (Comunidad de)" en la tabla (mono-provincial) |
| Parque por provincia, ej. Barcelona | 2.647.478 total / 2.290.722 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Parque por provincia, ej. Valencia | 1.508.589 total / 1.126.835 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Parque por provincia, ej. Sevilla | 936.812 total / 753.149 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Parque por provincia, ej. Zaragoza | 552.858 total / 414.543 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Parque por provincia, ej. Málaga | 1.025.676 total / 695.314 principal | viviendas | 2025 | MIVAU | ídem | ídem | ídem | |
| Viviendas por año de construcción del edificio (nacional, todas) | ver tabla | viviendas | 2021 | INE | Censo 2021, tpx=59516 | https://www.ine.es/jaxi/Tabla.htm?tpx=59516 | raw/censo2021/59516_tipo_vivienda_anio_construccion_nacional.csv | Desglosado también en Principal / No principal |

Antigüedad del parque (Censo 2021, viviendas totales por año de construcción del edificio):

| periodo construcción | viviendas totales | viviendas principales |
|---|---|---|
| Antes de 1900 | 508.637 | 256.497 |
| 1900-1920 | 1.393.089 | 706.643 |
| 1921-1940 | 1.055.529 | 614.624 |
| 1941-1950 | 713.643 | 436.840 |
| 1951-1960 | 1.433.735 | 1.035.379 |
| 1961-1970 | 3.450.525 | 2.642.794 |
| 1971-1980 | 4.488.319 | 3.415.830 |
| 1981-1990 | 3.078.407 | 2.168.412 |
| 1991-2000 | 3.564.948 | 2.687.031 |
| 2001-2010 | 5.240.772 | 3.721.560 |
| 2011-2020 | 734.659 | 468.576 |
| No consta | 961.445 | 382.430 |

---

## 4. Series anuales 2000-2025: iniciadas, terminadas, visados y VPO calificadas (MIVAU)

Fuente: MIVAU, Boletín Estadístico Online (antiguo Ministerio de Fomento), series anuales por CCAA/provincia, 1991-2025.

| variable | valor 2000 | valor 2006 (máx. histórico) | valor 2013 (mínimo) | valor 2024 | valor 2025 | unidad | organismo | tabla/código | URL exacta | archivo local |
|---|---|---|---|---|---|---|---|---|---|---|
| Viviendas libres iniciadas (nacional) | 487.810 | **664.923** | 29.232 | 112.220 | 121.827 | viviendas/año | MIVAU | Boletín, Tabla 3.1, cod. 32200500 | https://apps.fomento.gob.es/BoletinOnline2/sedal/32200500.XLS | raw/mivau/32200500.xls → limpio/mivau_viviendas_libres_iniciadas_1991_2025.csv |
| Viviendas libres terminadas (nacional) | 362.940 | **597.632** (máx. 2006; 2005=528.754, 2007=579.665) | 43.230 | 86.609 | 80.792 | viviendas/año | MIVAU | Boletín, Tabla 3.2, cod. 32201000 | https://apps.fomento.gob.es/BoletinOnline2/sedal/32201000.XLS | raw/mivau/32201000.xls → limpio/mivau_viviendas_libres_terminadas_1991_2025.csv |
| VPO — calificaciones provisionales (nacional) | 47.180 | 97.617 | 6.489 | 23.967 | 15.503 | viviendas/año | MIVAU | Boletín, Tabla 1.3, cod. 31303000 | https://apps.fomento.gob.es/BoletinOnline2/sedal/31303000.XLS | raw/mivau/31303000.xls → limpio/mivau_vpo_calificaciones_provisionales_1991_2025.csv |
| VPO — calificaciones definitivas (nacional) | 52.318 | 60.878 | 17.059 | 14.371 | 12.858 | viviendas/año | MIVAU | Boletín, Tabla 1.6, cod. 31306000 | https://apps.fomento.gob.es/BoletinOnline2/sedal/31306000.XLS | raw/mivau/31306000.xls → limpio/mivau_vpo_calificaciones_definitivas_1991_2025.csv |

Series mensuales equivalentes también descargadas (cod. 32100500 / 32101000, viviendas libres iniciadas/terminadas mensual) en `raw/mivau/32100500.xls` y `32101000.xls`.

Nota sobre "visados de dirección de obra nueva (CSCAE)": el Boletín Estadístico del MIVAU en la sección de vivienda libre publica **iniciadas/terminadas**, que en la práctica de MIVAU/Fomento se basan en visados de dirección de obra del CSCAE agregados; no se ha localizado en apps.fomento.gob.es una tabla separada explícitamente rotulada "visados" con serie 2000-2025 independiente de "iniciadas". Se toma la serie de "viviendas libres iniciadas" como equivalente operativo, tal como hace el propio MIVAU en sus notas de prensa. Ver huecos.

---

## 5. Empleo en construcción (EPA, Seguridad Social, VAB)

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Ocupados en construcción (pico histórico) | 2.724.400 (2007T3); 2.705.400 (2007T4); 2.624.200 (2006T4) | miles de personas ×1000 (personas) | 2002T1-2008T4 | INE | EPA, tabla jaxiT3 t=4642 (CNAE-93), "Ocupados por rama de actividad y sexo y CCAA" | https://www.ine.es/jaxiT3/Tabla.htm?t=4642 | raw/ine_series/ocupados_rama_ccaa_4642.csv | Ambos sexos, Total Nacional. Clasificación CNAE-93 (anterior a 2009) |
| Ocupados en construcción, último dato con esta tabla | 1.409.100 (2023T4) | personas (miles) | 2021T1-2023T4 | INE | EPA, tabla jaxiT3 t=4128 / t=4230 (CNAE-2009) | https://www.ine.es/jaxiT3/Tabla.htm?t=4128 | raw/ine_series/epa_ocupados_rama_4128.csv, ocupados_rama_ccaa_4230.csv | Tabla online solo conserva ventana móvil de periodos recientes; no cubre 2024-2026 en el momento de la consulta |
| Variación ocupados construcción, 2T 2026 | +60.000 respecto al trimestre anterior | personas | 2T 2026 | INE | Nota de prensa EPA 2T2026 | https://www.ine.es/dyngs/Prensa/EPA2T26.htm | (no descargable como tabla; cita textual de la nota) | Cifra absoluta del nivel no indicada en el cuerpo de la nota; requeriría el cuadro-anexo de la publicación completa |
| VAB construcción (Contabilidad Nacional, precios corrientes) | 1.057.467 (miles €, año 2017 en la serie descargada — ver nota) | miles de euros | serie hasta 2017 en este export | INE | Contabilidad Nacional, tabla jaxiT3 t=29008 "Valor Añadido Bruto" | https://www.ine.es/jaxiT3/Tabla.htm?t=29008 | raw/ine_series/vab_29008.csv | La fila "Total CNAE" no es construcción; falta filtrar por agrupación CNAE A21/A64 = Construcción; ver huecos |
| Afiliados a la Seguridad Social en construcción | no obtenido | — | — | Seguridad Social (Ministerio de Inclusión) | Estadística de afiliados por sección de actividad, portal PXWeb w6.seg-social.es | https://w6.seg-social.es/PXWeb/pxweb/es/Afiliados%20en%20alta%20laboral/ | — | No se ha logrado descargar el CSV/XLS exacto por sección de actividad (construcción) dentro del tiempo de esta recopilación; ver huecos |

---

## 6. Suelo: precio del suelo urbano y Sistema de Información Urbana (SIU)

### 6.1 Precio del suelo urbano (MIVAU, Estadística de precios de suelo urbano)

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Precio medio suelo urbano, nacional | 207,76 | €/m² | 2T 2026 (último dato) | MIVAU | Boletín, Tabla 4, cod. 36400500 | https://apps.fomento.gob.es/BoletinOnline2/sedal/36400500.XLS | raw/mivau/36400500.xls → limpio/mivau_precio_suelo_urbano_provincias_ultimo_periodo.csv | Var. trimestral +10,6%; interanual +15,3% |
| — Madrid (Comunidad de) | ver csv | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | Provincia mono-provincial = CCAA |
| — Barcelona | ver csv (var. interanual -2,4%) | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| — Valencia/València (var. interanual +21,5%) | ver csv | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| — Sevilla (var. interanual +17,1%) | ver csv | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| — Zaragoza (var. interanual +13,6%) | ver csv | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| — Málaga (var. interanual +26,9%) | ver csv | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| Precio suelo urbano en municipios >50.000 hab, nacional | ver csv | €/m² | 2T 2026 | MIVAU | Boletín, Tabla 4.5, cod. 36403000 | https://apps.fomento.gob.es/BoletinOnline2/sedal/36403000.XLS | raw/mivau/36403000.xls → limpio/mivau_precio_suelo_urbano_municipios_mas50000_ultimo_periodo.csv | Málaga (capital, fila "Málaga"): 653,52 €/m²; Barcelona: 438,08; Valencia/València: 434,45; Zaragoza: 313,17; Sevilla: 231,96. Es un **promedio provincial de los municipios >50.000 hab de esa provincia**, no un dato exclusivo de la capital cuando hay varios municipios >50.000 hab en la provincia. |

### 6.2 Sistema de Información Urbana (SIU) — clases de suelo y capacidad residencial del planeamiento

Fuente: MIVAU, SIU, descarga oficial de datos alfanuméricos. URL de descarga: https://cdn.mivau.gob.es/portal-web-mivau/urbanismo-suelo/Datos%20alfanumericos%20SIU%20-%20Excel%20-%2020260619.zip (actualización 19/06/2026). Cobertura: 5.900 municipios estudiados (72% del total de municipios españoles).

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Superficie total en Áreas de Suelo de Desarrollo (nacional) | 5.303.875.857 | m² (≈530.388 ha) | actualización 2026 (por municipio) | MIVAU, SIU | areas_desarrollo_nac.xlsx | https://www.mivau.gob.es/urbanismo-y-suelo/sistema-de-informacion-urbana | raw/siu/datos_alfanumericos/areas_desarrollo_nac.xlsx | |
| Viviendas previstas en Áreas de Desarrollo (nacional) | 9.600.382 | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | Suma de todo lo planificado, construido o no |
| — de ellas, pendientes de materializar | 7.090.504 | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | Indicador clave de "capacidad residencial ya zonificada" no construida |
| Viviendas previstas en áreas de desarrollo — Madrid (provincia) | 768.562 (441.720 pendientes) | viviendas | ídem | MIVAU, SIU | areas_desarrollo_prov.xlsx | ídem | limpio/siu_areas_desarrollo_por_provincia.csv | |
| — Barcelona | 301.740 (197.959 pendientes) | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | |
| — Valencia/València | 450.509 (310.145 pendientes) | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | |
| — Sevilla | 295.523 (212.963 pendientes) | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | |
| — Zaragoza | 169.511 (118.262 pendientes) | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | |
| — Málaga | 440.590 (259.553 pendientes) | viviendas | ídem | MIVAU, SIU | ídem | ídem | ídem | |
| Clases de suelo, % por provincia (consolidado, desarrollo, urbanizable delim./no delim., no urbanizable, etc.) | ver csv completo, 52 provincias | % de superficie municipal | ídem | MIVAU, SIU | clases_suelo_prov.xlsx | ídem | limpio/siu_clases_suelo_por_provincia.csv | Nacional: 95,48% suelo no urbanizable, 2,06% urbano consolidado, 1,28% en áreas de desarrollo, 0,85% urbanizable no delimitado, 1,04% urbanizable delimitado (ver clases_suelo_nac.xlsx) |

No se ha descargado el shapefile completo "Clases de suelo" (ZIP de 300 MB, por encima del límite de tamaño fijado para esta tarea); se ha usado en su lugar el paquete de datos alfanuméricos (Excel), que contiene los mismos indicadores agregados sin geometría.

---

## 7. Transacciones de vivienda al año

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Viviendas transmitidas, total (todos los títulos: compraventa+herencia+donación+otros) | 1.129.253 | viviendas/año | 2025 | INE | ETDP, tabla jaxiT3 t=6154 "Viviendas transmitidas según título de adquisición" | https://www.ine.es/jaxiT3/Datos.htm?t=6154 | raw/ine_series/etdp_viviendas_transmitidas_6154.csv | Serie nacional, por CCAA y por provincia, título "Viviendas: Total" |
| Viviendas transmitidas por compraventa | 711.543 | viviendas/año | 2025 | INE | ídem | ídem | ídem | Serie completa 2007-2025 en el CSV: 2007=775.300 (máximo pre-crisis) … 2009=413.393 (mínimo) … 2025=711.543 |
| Transacciones inmobiliarias de vivienda, MIVAU (histórico, archivado) | serie 2004-2008 solamente | transacciones/trimestre | 2004-2008 | MIVAU | Boletín, Tabla 1 y 1.3/1.4, cod. 34010110/34010180/34010190 | https://apps.fomento.gob.es/BoletinOnline2/sedal/34010110.XLS | raw/mivau/34010110.xls, 34010180.xls, 34010190.xls | Estas tablas del boletín online de MIVAU están archivadas y solo cubren 2004-2008; para serie reciente se usó la ETDP del INE (fila anterior) |

---

## 8. Estado de conservación del parque (Censo 2021)

| variable | valor | unidad | fecha ref | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Viviendas principales por estado de conservación del edificio (nacional) | Malo: 628.950; Regular: 3.089.865; Normal: 3.948.440; Bueno: 5.778.004; Muy bueno: 3.073.852; Excelente: 2.290.935; Total: 18.810.046 | viviendas | 2021 | INE | Censo 2021, tpx=56894 "Viviendas principales según estado de conservación del edificio…" | https://www.ine.es/jaxi/Tabla.htm?tpx=56894 | raw/censo2021/56894_viviendas_estado_conservacion_tipoedificio_anio_tamano.csv → limpio/censo2021_viviendas_estado_conservacion_nacional.csv | Escala censal de 6 categorías (Malo/Regular/Normal/Bueno/Muy bueno/Excelente); el Censo 2021 no usa la etiqueta "ruinoso" que sí usaba el Censo de Edificios 2011 |
| Viviendas en estado "Malo" o "Regular" (proxy de parque no digno) | 3.718.815 | viviendas | 2021 | INE | ídem | ídem | ídem | = 19,8% del parque principal censado en esta tabla |

---

## Huecos y advertencias

1. **Desglose provincial secundaria/vacía (Censo 2021):** el INE solo publica de forma predefinida, a nivel de provincia, la dicotomía "principal / no principal" (tpx 59520). El desglose fino secundaria vs. vacía existe únicamente a nivel de cada municipio ≥2.000 habitantes (tabla p06/10mun00.px) y agregado nacional (tpx 59525, solo total/principal/no-principal por municipio). Es posible reconstruir un agregado provincial de secundarias/vacías sumando los municipios ≥2.000 hab. de esa provincia, pero quedarían fuera los municipios pequeños (aproximación, no cifra oficial exacta). No se ha hecho esa agregación por límite de tiempo; los insumos (10mun00.px, raw completo) están descargados para hacerlo si se requiere.
2. **Tramo de superficie 40-50 m²:** el Censo 2021 no publica ese corte; el tramo más fino oficial es "Hasta 75 m²". Se reporta una aproximación (sección 2) que sobreestima ligeramente la vivienda "suficiente" porque el tramo hasta 75 m² mezcla viviendas de 40 y de 74 m².
3. **Visados de dirección de obra nueva (CSCAE) como serie independiente de "iniciadas":** no se localizó en apps.fomento.gob.es una tabla explícitamente llamada "visados" separada de "viviendas iniciadas" con serie 2000-2025; el propio MIVAU trata ambas series como equivalentes en sus publicaciones. Si el análisis requiere el dato crudo de visados del CSCAE (que a veces difiere ligeramente de "iniciadas" MIVAU), habría que acudir directamente al Observatorio del CSCAE, que no es fuente estatal-oficial en sentido estricto y por tanto no se ha usado aquí.
4. **Empleo EPA en construcción, serie continua 2006-2026:** no existe una única tabla online de INE con esa ventana completa bajo una sola clasificación CNAE. Se combinó: (a) tabla histórica CNAE-93 (t=4642), cubre 2002T1-2008T4 y capta el máximo histórico de ocupación en construcción (~2,72 millones en 2007T3); (b) tabla CNAE-2009 (t=4128/t=4230), que en el momento de la consulta solo conservaba online 2021T1-2023T4 (1,41 millones en 2023T4); (c) la nota de prensa EPA 2T2026 confirma una subida de +60.000 ocupados en construcción respecto al trimestre anterior, pero no publica en el cuerpo del texto el nivel absoluto. **Falta el nivel exacto 2024-2026 y el puente 2009-2020**; se recomienda pedir a INE (o usar el servicio Tempus3 vía API con series históricas completas) las tablas de "series enlazadas" que unifican CNAE-93 y CNAE-2009.
5. **VAB de construcción (Contabilidad Nacional):** el archivo descargado (t=29008) trae la fila "Total CNAE" sin desglosar aún por agrupación A21/A64 = Construcción en el volcado revisado; falta filtrar por el código correspondiente a construcción dentro de ese fichero (los datos brutos están en `raw/ine_series/vab_29008.csv`, columnas "CNAE Agrupación A21/A64"). No se completó el filtrado fino por límite de tiempo.
6. **Afiliados a la Seguridad Social en construcción:** no se consiguió descargar el fichero exacto (serie histórica por sección de actividad) desde el portal PXWeb de la Seguridad Social (w6.seg-social.es) dentro del tiempo de esta tarea. Es un hueco real; la mejor aproximación oficial sería la tabla "Afiliados en alta laboral" de ese portal, sección CNAE Construcción (F), serie mensual/anual.
7. **Horas de trabajo por vivienda / productividad del sector:** no se localizó una estadística oficial que ofrezca directamente "horas de trabajo por vivienda construida". Se podría aproximar combinando VAB de construcción (Contabilidad Nacional) y ocupados EPA, pero no es un dato oficial directo y no se ha calculado un índice propio para no presentarlo como estadística oficial.
8. **SIU — unidad de "superficie total de suelo" (ETotSue/MunTotSue):** el fichero de metadatos del SIU no especifica la unidad de esa variable con la misma claridad que para "Áreas de Suelo de Desarrollo" (que sí está en m²). El valor nacional (413.482) es plausible en km² para los 5.900 municipios estudiados, pero no se ha podido confirmar la unidad exacta contra la documentación oficial del SIU dentro del tiempo disponible; usar con precaución y, si es crítico para el análisis, confirmar con el propio informe metodológico del SIU (enlace "Enlaces relacionados" / "Sectores Residenciales en España 2025" en la web del SIU).
9. **Shapefile "Clases de suelo" (geometría SIU):** el paquete completo (~300 MB) supera el límite de tamaño fijado para las descargas de esta tarea y no se ha descargado; solo se usaron los datos alfanuméricos agregados (sin geometría), suficientes para las cifras agregadas por provincia/municipio pedidas.
10. **Informe "Áreas urbanas en España" / Atlas de Áreas Urbanas:** se localizó la sección del MIVAU (https://www.mivau.gob.es/urbanismo-y-suelo/suelo/atlas-estadistico-de-las-areas-urbanas) pero no se descargó su informe específico por límite de tiempo; el dato de suelo vacante/urbanizable ya está cubierto de forma más operativa por el SIU (sección 6.2).
11. **Transacciones MIVAU archivadas:** las tablas del boletín online de MIVU específicas de compraventas (34010110/34010180/34010190) solo contienen datos 2004-2008 (marcadas "Continúa" en el propio archivo, indicando que la serie fue descontinuada ahí); se usó en su lugar la ETDP del INE, que sí cubre 2007-2025 de forma continua y es la fuente estadística vigente para transmisión de derechos de propiedad sobre vivienda.
