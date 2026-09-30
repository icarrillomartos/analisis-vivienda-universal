# Ficha de datos — Demografía y hogares (España)

Frente: **Demografía y hogares**, para el análisis de viabilidad de «vivienda gratuita universal» en España.
Elaborado por: analista de datos (modelo Claude Sonnet 5), 28-09-2026.
Todas las fuentes son oficiales: INE (API JSON Tempus3, `servicios.ine.es/wstempus`) y Eurostat (API JSON-stat, `ec.europa.eu/eurostat/api`). No se han usado fuentes de prensa, portales inmobiliarios ni Statista.

Scripts de extracción/limpieza: `trabajo/datos/demografia/scripts/` (no se generó ningún script final único; el detalle de las llamadas API y la lógica de limpieza está documentado abajo, tabla por tabla, y los ficheros JSON originales están en `trabajo/datos/demografia/raw/`).
Tablas limpias (CSV): `trabajo/datos/demografia/limpio/`.

**Nota sobre vintage/fechas**: la Estadística Continua de Población (ECP) del INE tiene varias familias de tablas para el mismo concepto; algunas se han dejado de actualizar (p. ej. id 56934/56940/56945, ancladas en 1-1-2025) mientras que sus "sucesoras" siguen vivas (id 59583/59589/82104, actualizadas a 1-7-2026). Se han usado siempre las tablas **activas** más recientes; se indica la fecha exacta en cada fila.

---

## 1. Población residente por edad y nacionalidad (España, ECP)

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Población total nacional | 49.801.559 | personas | 1-7-2026 | INE | ECP, tabla 59583 (Población residente por fecha, sexo y edad, nacional, edad simple) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/59583?nult=1 | `raw/ecp_poblacion_nacional_sexo_edadsimple_ACTUAL_59583.json` | Última estimación semestral ECP disponible en la fecha del encargo (28-09-2026). Sustituye a la tabla 56934 (id discontinuada, quedó en 1-1-2025). |
| Población 18 años o más, nacional (exacta, edad simple) | 42.009.991 | personas | 1-7-2026 | INE | ECP, tabla 59583 | ídem | ídem | Suma de edades simples 18 a "100 y más años". |
| Población nacional por nacionalidad: española | 42.364.016 | personas | 1-7-2026 | INE | ECP, tabla 82104 (Población por fecha, sexo, grupo de edad y nacionalidad española/extranjera; nacional+CCAA+provincia) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/82104?nult=1 | `raw/ecp_poblacion_geo_sexo_grupoedad_nacionalidad_82104.json` | Grupos quinquenales de edad, no edad simple. |
| Población nacional por nacionalidad: extranjera | 7.437.543 | personas | 1-7-2026 | INE | ECP, tabla 82104 | ídem | ídem | ídem |
| Población 18+ nacional, española (aproximada) | 35.711.197 | personas | 1-7-2026 | INE (cálculo propio) | ECP, tabla 82104 + corrección de banda 15-19 | ídem | `limpio/poblacion_18mas_por_provincia_y_nacionalidad_APROX.csv` | **Estimación**: la tabla 82104 da grupos quinquenales (…,15-19,20-24,…), no edad simple, por lo que el corte exacto en 18 años no existe cruzado con nacionalidad. Se sumó el grupo 20+ íntegro y se añadió el 40,96% del grupo "15 a 19 años" (fracción de 18-19 años dentro de ese grupo, calculada con datos de edad simple sin nacionalidad, tabla 59583, curso 2026: pob(18)+pob(19) / pob(15..19) = 0,4096). Ver `limpio/nota_fraccion_18_19_en_15_19.txt`. Al aplicar la misma fracción al total sin desagregar por nacionalidad, el resultado reproduce el valor exacto (42.009.991), validando el método. |
| Población 18+ nacional, extranjera (aproximada) | 6.298.795 | personas | 1-7-2026 | INE (cálculo propio) | ídem | ídem | ídem | ídem |
| Población total y 18+ **por provincia** (todas las nacionalidades) | ver CSV (52 provincias + Ceuta/Melilla) | personas | 1-7-2026 | INE | ECP, tabla 59589 (Población residente por fecha, sexo y edad, provincias, edad simple) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/59589?nult=1 | `raw/ecp_poblacion_provincia_sexo_edadsimple_ACTUAL_59589.json` → `limpio/poblacion_18mas_por_provincia_ECP.csv` | Edad simple exacta, sin corte de banda. Ejemplos: Madrid 7.201.554 (18+: 6.051.137); Barcelona 6.028.373 (18+: 5.079.276); Sevilla 2.004.487 (18+: 1.662.951). |
| Población total y 18+ **por provincia y nacionalidad** (española/extranjera) | ver CSV | personas | 1-7-2026 | INE (cálculo propio) | ECP, tabla 82104, con la misma corrección de banda 15-19 (fracción 0,4096) aplicada provincia a provincia | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/82104?nult=1 | `limpio/poblacion_18mas_por_provincia_y_nacionalidad_APROX.csv` | **Aproximado** (ver metodología arriba). Cobertura: 52 provincias + Total Nacional. |
| Cohorte de personas de 15-19 años (nacional) | 2.746.606 | personas | 1-7-2026 | INE | ECP, tabla 59583 | ídem | `limpio/nota_fraccion_18_19_en_15_19.txt` | Usado solo para calcular la fracción de corrección anterior. |

**Huecos en el punto 1**: no existe en Tempus una tabla ECP con edad simple cruzada con nacionalidad a nivel provincial (solo grupos quinquenales); de ahí la necesidad de aproximar. La tabla provincial de edad simple sin nacionalidad (id 56945, la "más granular" en teoría) está bloqueada por el API ("No puede mostrarse por restricciones de volumen"); se usó su sucesora activa (59589), que sí responde.

---

## 2. Cohortes que cumplen 18 años y proyección de población adulta 2030-2039

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Personas que cumplen 18 años cada año, 2026-2039 (aprox., escenario central) | ver serie: 551.342 (2026) → 559.737 (2030) → 526.242 (2035) → 455.235 (2039) | personas/año | proyección anual 1-1 | INE | Proyecciones de Población, tabla 36643 (Población residente por fecha, sexo y edad, nacional, edad simple, proyección a largo plazo 2026-2076) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/36643?nult=60 | `raw/proy_poblacion_largoplazo_nacional_edad_36643.json` → `limpio/cohorte_18_anyos_proyectada_2026_2039.csv` | Aproximación estándar: población proyectada de 18 años exactos a 1 de enero de cada año, como proxy de la cohorte que cumple 18 ese año (no es el nº exacto de cumpleaños, pero es la cifra que publica y usa el INE para este tipo de análisis). Tendencia claramente descendente desde 2027 por el "valle" demográfico de nacimientos de comienzos de los 2010. |
| Población adulta (18+) proyectada, nacional | 2030: 43.910.010 · 2035: 45.740.260 · 2039: 46.487.930 | personas | 1-1 de cada año | INE | Proyecciones de Población, tabla 36643 | ídem | `limpio/proyeccion_poblacion_18mas_nacional_2026_2039.csv` | Escenario central (única variante publicada en esta tabla; el INE también publica un "análisis de sensibilidad", tabla 36652, no descargado por alcance). |
| Población adulta (18+) proyectada, **por provincia**, 2030/2035/2039 | ver CSV completo (52 provincias) | personas | 1-1 de cada año | INE | Proyecciones de Población, tabla 36726 (proyección a corto plazo 2026-2041, provincias, edad simple) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/36726?nult=16 | `raw/proy_poblacion_cortoplazo_provincia_edad_36726.json` → `limpio/proyeccion_poblacion_18mas_por_provincia_2030_2035_2039.csv` | El agregado nacional de esta tabla (corto plazo) coincide casi exactamente con la de largo plazo (43,91M / 45,74M / 46,49M en 2030/35/39), lo que valida la consistencia entre ambos escenarios/tablas del INE. |

---

## 3. Hogares: total, tamaño medio, distribución por tamaño, proyección

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Hogares totales, nacional | 19.874.860 | hogares | 1-7-2026 | INE | ECP-Hogares, tabla 60135 (Hogares de personas residentes en viviendas familiares, nacional, por tamaño) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/60135?nult=1 | `raw/ecp_hogares_nacional_tamano_60135.json` → `limpio/hogares_nacional_tamano.csv` | Fuente más reciente disponible (ECP), tal y como pide el encargo. |
| Tamaño medio del hogar, nacional | 2,49 | personas/hogar | 1-7-2026 | INE | ECP-Hogares, tabla 60136 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/60136?nult=1 | `raw/ecp_hogares_nacional_tamanomedio_60136.json` | |
| Hogares de 1 persona (unipersonales), nacional | 5.678.769 (28,6% del total) | hogares | 1-7-2026 | INE | ECP-Hogares, tabla 60135 | ídem | `limpio/hogares_nacional_tamano.csv` | |
| Hogares de 2 personas, nacional | 5.779.949 | hogares | 1-7-2026 | INE | ídem | ídem | ídem | |
| Hogares de 3 personas, nacional | 3.926.489 | hogares | 1-7-2026 | INE | ídem | ídem | ídem | |
| Hogares de 4 o más personas, nacional | 4.489.653 | hogares | 1-7-2026 | INE | ídem | ídem | ídem | |
| Hogares por tamaño y tamaño medio, **por CCAA** | ver CSV (19 CCAA + Ceuta/Melilla) | hogares / personas·hogar | 1-7-2026 | INE | ECP-Hogares, tablas 60131 (tamaño) y 60132 (tamaño medio) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/60131?nult=1 · .../60132?nult=1 | `raw/ecp_hogares_ccaa_*` → `limpio/hogares_ccaa_tamano.csv`, `limpio/hogares_ccaa_tamanomedio.csv` | |
| Hogares por tamaño y tamaño medio, **por provincia** | ver CSV (52 provincias) | hogares / personas·hogar | 1-7-2026 | INE | ECP-Hogares, tablas 60133 (tamaño) y 60134 (tamaño medio) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/60133?nult=1 · .../60134?nult=1 | `raw/ecp_hogares_provincia_*` → `limpio/hogares_provincia_tamano.csv`, `limpio/hogares_provincia_tamanomedio.csv` | Cumple el "por provincia si es posible" del encargo. |
| Proyección de hogares, nacional y por tamaño, 2026-2041 | Total: 19,76M (2026) → 20,61M (2030) → 21,36M (2035) → 21,78M (2039) | hogares | anual, 1 de cada año | INE | Proyección de Hogares (operación 70), tabla 54562 (por tamaño del hogar y año, CCAA + nacional) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/54562?nult=16 | `raw/proy_hogares_ccaa_tamano_54562.json` → `limpio/proyeccion_hogares_ccaa_tamano_2026_2041.csv` | Es la única tabla de la operación "Proyección de Hogares" disponible en Tempus; cubre 2026-2041 (no hemos podido confirmar en esta sesión si corresponde a la edición "2024-2039" u otra edición posterior, por no tener acceso a la ficha metodológica; el rango de años observado en los datos es 2026-2041). Tamaño medio proyectado: 2,49 (2026) → 2,47 (2030) → 2,45 (2035) → 2,44 (2039), es decir, sigue bajando. |
| Hogares unipersonales proyectados, nacional | 5.620.017 (2026) → 5.986.743 (2030) → 6.363.634 (2035) → 6.618.406 (2039) | hogares | anual | INE | Tabla 54562 | ídem | ídem | Crecimiento sostenido de los hogares de 1 persona en todo el horizonte de proyección. |

**Huecos en el punto 3**: no se ha localizado en el servicio Tempus del INE una tabla de "Censo de Población 2021" (operación 463) ni de "Encuesta Continua de Hogares 2020" con hogares por tamaño/provincia bajo esos nombres exactos (se revisaron los ~988 títulos de tablas de la operación 463 sin encontrar coincidencia con "hogar" o "vivienda"). Es posible que estos datos existan en el explorador de resultados del Censo 2021 (aplicación específica de INE, fuera de Tempus) o en ficheros de descarga masiva no cubiertos en esta sesión; se deja como pendiente para una revisión manual en https://www.ine.es/censos2021/.

---

## 4. Convivencia: jóvenes con sus padres y personas que viven solas

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Jóvenes de 18-34 años que viven con sus padres (o dependen económicamente del hogar paterno) | 68,7% | % de la población 18-34 | 2025 | Eurostat | `ilc_lvps08` (EU-SILC) | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_lvps08?format=JSON&geo=ES | `raw/eurostat_ilc_lvps08.json` → `limpio/eurostat_ilc_lvps08_jovenes_con_padres.csv` | Definición Eurostat: "Persons living with their parents or contributing/benefiting from the household income". Serie histórica completa 2004-2025 en el CSV; tendencia ascendente sostenida (51,4% en 2004 → 68,7% en 2025). |
| Edad media estimada de emancipación (abandono del hogar familiar) | 30,2 | años | 2025 | Eurostat | `yth_demo_030` | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/yth_demo_030?format=JSON&geo=ES | `raw/eurostat_yth_demo_030.json` → `limpio/eurostat_yth_demo_030_edad_emancipacion.csv` | España tiene una de las edades de emancipación más altas de la UE. Serie 2000-2025 en el CSV. |
| Personas que viven solas (= hogares unipersonales), nacional | 5.678.769 | personas/hogares | 1-7-2026 | INE | ECP-Hogares, tabla 60135 (ver punto 3) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/60135?nult=1 | `limpio/hogares_nacional_tamano.csv` | Por definición, el nº de hogares unipersonales equivale al nº de personas que viven solas. |
| Personas que viven solas, **por tramo de edad** | no encontrado | — | — | — | — | — | — | **No encontrado** en Tempus del INE (ni en ECP ni en ECV) una tabla que cruce "hogar unipersonal / vive solo" con la edad de esa persona. Se revisaron los ~254 títulos de tablas de la ECV (operación 155) sin encontrar ninguna con "unipersonal" combinado con edad. El Censo de Población 2021 sí suele publicar esta desagregación en su explotación estándar, pero no se localizó la tabla correspondiente en Tempus dentro del tiempo de esta sesión. Aproximación oficial más cercana: ECV tabla 9994 "Hogares por régimen de tenencia de la vivienda y edad y sexo de la persona de referencia" cruza edad del sustentador principal con tenencia (no con tamaño de hogar), por lo que no resuelve la pregunta directamente. |

---

## 5. Régimen de tenencia de la vivienda principal (ECV)

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Propiedad (con o sin hipoteca) | 73,3 | % de hogares | 2025 (ECV, ingresos de 2024) | INE | ECV, tabla 76845 (Hogares por régimen de tenencia de la vivienda y comunidades autónomas) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/76845?nult=1 | `raw/ecv_tenencia_ccaa_nacional_76845.json` → `limpio/ecv_tenencia_vivienda_ccaa.csv` | La tabla 9997 (id antigua) devuelve exactamente los mismos valores; se ha tomado 76845 como tabla activa de referencia. |
| Propiedad sin hipoteca | 48,9 | % de hogares | 2025 | INE | ídem | ídem | ídem | |
| Propiedad con hipoteca | 24,4 | % de hogares | 2025 | INE | ídem | ídem | ídem | |
| Alquiler a precio de mercado | 16,7 | % de hogares | 2025 | INE | ídem | ídem | ídem | |
| Alquiler inferior al precio de mercado | 3,5 | % de hogares | 2025 | INE | ídem | ídem | ídem | |
| Cesión | 6,5 | % de hogares | 2025 | INE | ídem | ídem | ídem | Suma total: 100,0% (redondeos incluidos). |
| Régimen de tenencia, **por comunidad autónoma** | ver CSV (19 CCAA + nacional) | % de hogares | 2025 | INE | ECV, tabla 76845 | ídem | `limpio/ecv_tenencia_vivienda_ccaa.csv` | |
| Número de hogares en propiedad (estimado) | ≈ 14.568.272 | hogares | cruce 2025 (ECV) × 2026 (ECP) | INE (cálculo propio) | 73,3% × 19.874.860 hogares totales (ECP, tabla 60135) | — | `limpio/resumen_hogares_tenencia.txt` | **Estimación por cruce de dos operaciones con vintage distinto** (ECV 2025 y ECP jul-2026): la ECV publica solo porcentajes, no cifras absolutas, en Tempus. El desajuste temporal (unos meses) es menor comparado con la magnitud del dato y no se considera relevante para el análisis de viabilidad. |

---

## 6. Personas propietarias de al menos una vivienda (no hogares)

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Nº de personas físicas propietarias de vivienda | **no encontrado** | — | — | — | — | — | — | El INE no publica esta estadística (ni en ECP, ni en ECV, ni en Censo). Se comprobó la operación 388 "Estadística de los Declarantes del IRPF" (INE/AEAT): no tiene tablas en el servicio Tempus (devuelve 0 tablas), por lo que sus datos de imputación de rentas inmobiliarias solo están disponibles como ficheros de descarga directa en la web de la AEAT/INE, no explorados en esta sesión por no ser accesibles vía API. La Dirección General del Catastro (Ministerio de Hacienda) publica "Estadísticas Catastrales" con nº de titulares catastrales, pero no es un organismo INE/Eurostat y no se pudo acceder a `catastro.hacienda.gob.es` desde este entorno (timeout de conexión). **Recomendación**: consultar manualmente la Estadística de Titulares Catastrales (Catastro) y/o el "Panel de hogares y mercado de trabajo" del IRPF (AEAT-INE) para una aproximación oficial. |

---

## 7. Población de grandes ciudades (Padrón, 1-1-2025) y adultos estimados

| variable | valor | unidad | fecha de referencia | organismo | tabla/operación y código | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Madrid (municipio) | 3.506.730 | personas | 1-1-2025 | INE | Padrón continuo — Revisión del Padrón Municipal, tabla 2881 (Madrid: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2881?nult=1 | `raw/padron_municipios_madrid_sexo_2881.json` | Fila "Madrid" (municipio), distinta de la fila "Madrid" agregada de provincia (7.137.031) presente en la misma tabla. |
| Barcelona (municipio) | 1.731.649 | personas | 1-1-2025 | INE | Tabla 2861 (Barcelona: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2861?nult=1 | `raw/padron_municipios_barcelona_sexo_2861.json` | |
| Valencia/València (municipio) | 840.792 | personas | 1-1-2025 | INE | Tabla 2903 (Valencia/València: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2903?nult=1 | `raw/padron_municipios_valencia_sexo_2903.json` | En esta tabla el municipio aparece etiquetado solo como "València" (topónimo valenciano), distinto de la fila de provincia "Valencia/València" (2.758.633). |
| Sevilla (municipio) | 689.423 | personas | 1-1-2025 | INE | Tabla 2895 (Sevilla: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2895?nult=1 | `raw/padron_municipios_sevilla_sexo_2895.json` | |
| Zaragoza (municipio) | 693.091 | personas | 1-1-2025 | INE | Tabla 2907 (Zaragoza: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2907?nult=1 | `raw/padron_municipios_zaragoza_sexo_2907.json` | |
| Málaga (municipio) | 599.063 | personas | 1-1-2025 | INE | Tabla 2882 (Málaga: Población por municipios y sexo) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/2882?nult=1 | `raw/padron_municipios_malaga_sexo_2882.json` | |
| Adultos (18+) estimados en cada ciudad | Madrid ≈ 2.946.545 · Barcelona ≈ 1.459.021 · Valencia ≈ 707.795 · Sevilla ≈ 571.955 · Zaragoza ≈ 585.532 · Málaga ≈ 500.484 | personas | Padrón 1-1-2025 (total) aplicando % de 18+ de la provincia a 1-7-2026 | INE (cálculo propio) | Combinación tabla Padrón (2881/2861/2903/2895/2907/2882) × % de 18+ provincial de ECP (tabla 59589) | — | `limpio/grandes_ciudades_padron2025_adultos_estimado.csv` | **Estimación, no cifra oficial**: el INE no publica en Tempus la población municipal desagregada por edad para estos municipios (las tablas de Padrón por municipio solo dan sexo). Se aplicó el % de población adulta de la provincia correspondiente (81-85% según la provincia) al total municipal del Padrón. El sesgo esperado es pequeño porque las grandes capitales suelen tener una estructura de edad similar a la de su provincia, pero puede haber diferencias (p. ej. más estudiantes jóvenes en la capital). |

---

## Huecos y advertencias (resumen)

1. **Población 18+ por provincia y nacionalidad cruzada**: no existe una tabla INE con edad simple × nacionalidad × provincia; se aproximó asumiendo distribución uniforme de edades dentro del grupo quinquenal "15 a 19 años" (fracción 18-19/15-19 = 0,4096, calculada y validada con datos nacionales exactos). Ver `limpio/nota_fraccion_18_19_en_15_19.txt`.
2. **Proyección de Hogares (tabla 54562)**: es la única tabla de esa operación disponible en Tempus; no se pudo confirmar la edición exacta (2024-2039 u otra) por falta de acceso a la ficha metodológica en esta sesión. Los datos cubren 2026-2041.
3. **Censo de Población y Viviendas 2021 y Encuesta Continua de Hogares 2020**: no se localizaron tablas de hogares (total, tamaño, unipersonalidad) para estas operaciones en el servicio Tempus del INE dentro del tiempo disponible. Se recomienda revisar manualmente el explorador de resultados del Censo 2021 (censos2021.ine.es).
4. **Jóvenes 18-34 con padres y edad de emancipación por comunidad autónoma o provincia**: Eurostat solo publica estos indicadores a nivel de país (España = "ES"), no hay desagregación territorial disponible en `ilc_lvps08` ni en `yth_demo_030`.
5. **Personas que viven solas por tramo de edad**: no encontrado en fuente oficial vía Tempus (ver punto 4 de la ficha). Solo se dispone del total de hogares unipersonales (sin desagregar por edad de la persona).
6. **Personas físicas propietarias de al menos una vivienda**: no encontrado en INE ni Eurostat. La fuente candidata (Catastro — Estadística de Titulares Catastrales) no fue accesible desde este entorno (timeout de red); la Estadística de Declarantes del IRPF (INE/AEAT, operación 388) no tiene tablas en el API Tempus. Pendiente de consulta manual.
7. **Número de hogares en propiedad**: cifra derivada de cruzar dos operaciones (ECV 2025 y ECP jul-2026) con vintage ligeramente distinto; tratar como estimación, no como dato oficial directo.
8. **Adultos en las 6 grandes ciudades**: estimación por aplicación del % provincial de 18+ al total municipal del Padrón, no un dato oficial de edad a nivel municipal (el INE no publica esa desagregación en Tempus para estos municipios).
9. **Tabla ECP 56945** (provincial, edad simple, sin nacionalidad, la tabla "canónica" para este cruce): bloqueada por el propio API del INE por "restricciones de volumen"; se resolvió usando su tabla sucesora activa (59589), que contiene los mismos datos y está más actualizada (1-7-2026 frente a 1-1-2025).
