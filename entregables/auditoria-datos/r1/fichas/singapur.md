# Ficha de datos oficiales — modelo de vivienda pública de Singapur (HDB)

Recopilación de fuentes primarias (HDB, SingStat/data.gov.sg, CPF Board, MND, MOF, gov.sg)
para comparar el modelo de "vivienda a precio fijo" de Singapur con la propuesta de
vivienda universal gratuita en España. Todas las cifras están en dólares de Singapur
(SGD) salvo que se indique lo contrario. Archivos originales en `raw/`, CSV derivados
en `limpio/`, scripts de proceso en `scripts/`.

## 1. Población, hogares y peso de HDB

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Población total de Singapur | 6,111,175 | personas | 2025 (final de junio) | SingStat | "Indicators On Population, Annual", serie "Total Population" | https://data.gov.sg/datasets/d_3d227e5d9fdec73f3bcadce671c333a6/view | raw/population_indicators.json; limpio/population_indicators.csv | Incluye residentes y no residentes |
| Población residente (ciudadanos + residentes permanentes) | 4,204,515 | personas | 2025 | SingStat | ídem, serie "Resident Population" | https://data.gov.sg/datasets/d_3d227e5d9fdec73f3bcadce671c333a6/view | raw/population_indicators.json | 2024: 4,180,868 |
| Hogares residentes (total) | 1,487,100 | hogares | 2025 | SingStat | "Resident Households By Type Of Dwelling, Annual" | https://data.gov.sg/datasets/d_edf8bb4773c25dd16b8b6875fd0b52da/view | raw/resident_households_by_dwelling_type.json; limpio/resident_households_by_dwelling_type.csv | |
| Hogares residentes en viviendas HDB (total) | 1,148,000 | hogares | 2025 | SingStat | ídem, serie "Total HDB Dwellings" | https://data.gov.sg/datasets/d_edf8bb4773c25dd16b8b6875fd0b52da/view | raw/resident_households_by_dwelling_type.json | 1,148,000 / 1,487,100 = 77.2% de los hogares residentes |
| % de hogares residentes en HDB por tramo (2025) | 1-2 hab. 108,300; 3 hab. 247,200; 4 hab. 464,000; 5 hab./Executive 328,500 | hogares | 2025 | SingStat | ídem | https://data.gov.sg/datasets/d_edf8bb4773c25dd16b8b6875fd0b52da/view | raw/resident_households_by_dwelling_type.json | |
| % de población residente que vive en pisos HDB | 76.0 | % | FY2024 (a 31/03/2025) | SingStat (citado por HDB) | HDB Key Statistics 2024/2025, "Statistical Highlights", p.6 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | FY2023 era 76.4%. HDB indica la fuente primaria es SingStat |
| % de población residente que vive en pisos HDB **en propiedad** ("HDB sold flats") | 73.0 | % | FY2024 | SingStat/HDB | ídem | ídem | raw/hdb_key_statistics_2025.pdf | Diferencia con el dato anterior son los pisos HDB en alquiler |
| Población residente en pisos HDB por ciudad-dormitorio (ej. Tampines 246,340; Woodlands 235,500; Sengkang 224,510…) | ver tabla completa | personas | a 31/03/2025 | SingStat/HDB | HDB Key Statistics 2024/2025, p.11-12 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | Total consolidado 3,190,590 residentes en pisos HDB |
| PIB nominal de Singapur (a precios corrientes) | 765,497.5 | millones SGD | 2024 | SingStat | "Expenditure on Gross Domestic Product at Current Prices, Annual", serie "GDP At Current Market Prices" | https://data.gov.sg/datasets/d_dc906ddc0e89c2210948d80cf5b75d80/view | raw/gdp_expenditure_current_prices.json; limpio/gdp_expenditure_current_prices.csv | 2023: 686,398.0 millones SGD (usado para el ratio de déficit/PIB del apartado 6) |

## 2. Tasa de propiedad de la vivienda

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Tasa de propiedad de la vivienda, hogares residentes (total país) | 90.8 | % | 2024 | SingStat | "Home Ownership Statistics" / "Key Household Income Trends" | https://www.singstat.gov.sg/find-data/explore-data-themes/households/resident-households | no descargado (bloqueo de acceso directo al recurso; cifra recogida vía buscador, pendiente de verificación con el PDF original de SingStat) | Dato muy citado (fuente SingStat) pero **no se pudo descargar el documento original**; ver huecos |
| Tasa de propiedad específica en pisos HDB | no localizada de forma desagregada | % | — | SingStat/HDB | — | — | — | Ver huecos: no se encontró una tabla oficial que separe la tasa de propiedad solo para hogares en HDB |

## 3. Parque de viviendas HDB por tipo y superficie

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Pisos de 1 habitación bajo gestión | 30,916 | unidades | a 31/03/2025 | HDB | HDB Key Statistics 2024/2025, "Properties Under Management", p.16 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | |
| Pisos de 2 habitaciones (incluye 2-Room Flexi) | 79,920 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Pisos de 3 habitaciones | 250,556 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Pisos de 4 habitaciones | 458,416 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Pisos de 5 habitaciones (incluye 3Gen) | 259,973 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Pisos Executive (incluye Multi-Generation) | 65,118 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Studio Apartments | 8,181 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Total parque residencial HDB bajo gestión | 1,153,080 | unidades | a 31/03/2025 | HDB | ídem | ídem | ídem | |
| Superficie de un piso 2-Room Flexi | 46 | m² | FY2024/2025 | HDB | HDB Key Statistics 2024/2025, "Floor Plans", p.22 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | Único tamaño confirmado con cifra explícita en el documento oficial descargado |
| Superficie típica 3-room / 4-room / 5-room / Executive | ~65 m² / ~90 m² / ~110 m² / ~130 m² | m² | orientativo | — | — | — | no descargado | **No confirmado en fuente oficial primaria**: rangos ampliamente publicados en guías inmobiliarias, pendientes de verificación directa en una ficha técnica de HDB (ver huecos) |

## 4. Precios BTO, precios de reventa y ratio precio/renta

**Precios de venta de pisos BTO nuevos (Standard) por ciudad, FY2024**, antes y después de descontar la subvención CPF asumida (fuente: HDB Key Statistics 2024/2025, "Price Range of Flats Offered", p.14):

| Ciudad | 2-Room Flexi (precio) | 2-Room Flexi (tras subvención) | 3-Room (precio) | 3-Room (tras subvención) | 4-Room (precio) | 4-Room (tras subvención) | 5-Room (precio) | 5-Room (tras subvención) |
|---|---|---|---|---|---|---|---|---|
| Bukit Batok | $140,000–$217,000 | $20,000–$97,000 | $247,000–$329,000 | $142,000–$224,000 | $335,000–$445,000 | $255,000–$365,000 | $496,000–$597,000 | $441,000–$542,000 |
| Jurong West | $109,000–$194,000 | $6,000–$74,000 | $209,000–$306,000 | $104,000–$201,000 | $290,000–$434,000 | $210,000–$354,000 | $427,000–$598,000 | $372,000–$543,000 |
| Pasir Ris | $194,000–$288,000 | $74,000–$168,000 | $329,000–$411,000 | $224,000–$306,000 | $481,000–$595,000 | $401,000–$515,000 | $635,000–$736,000 | $580,000–$681,000 |
| Sengkang | $126,000–$240,000 | $7,000–$120,000 | $277,000–$370,000 | $172,000–$265,000 | $324,000–$474,000 | $244,000–$394,000 | $465,000–$640,000 | $410,000–$585,000 |
| Woodlands | $140,000–$251,000 | $20,000–$131,000 | $275,000–$363,000 | $170,000–$258,000 | $329,000–$528,000 | $249,000–$448,000 | $486,000–$661,000 | $431,000–$606,000 |
| Yishun | $108,000–$181,000 | $6,000–$61,000 | $245,000–$295,000 | $140,000–$190,000 | $316,000–$395,000 | $236,000–$315,000 | $447,000–$533,000 | $392,000–$478,000 |

Archivo local: `raw/hdb_key_statistics_2025.pdf` (p.14). URL: https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf

**Precio mediano de reventa por tipo de piso, calculado por el equipo a partir del dataset oficial completo (transacciones registradas en 2024)**:

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Mediana precio de reventa, 1-room | 247,000 | SGD | año natural 2024 | HDB (vía data.gov.sg) | "Resale flat prices based on registration date from Jan-2017 onwards" | https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view | limpio/resale_flat_prices_2024_raw.csv; limpio/resale_median_price_by_flat_type_2024.csv | Mediana calculada por el equipo sobre 27,832 transacciones de 2024; script: scripts/computar_medianas_reventa.py |
| Mediana precio de reventa, 2-room | 340,000 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Mediana precio de reventa, 3-room | 418,000 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Mediana precio de reventa, 4-room | 590,000 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Mediana precio de reventa, 5-room | 690,000 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Mediana precio de reventa, Executive | 855,500 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Mediana precio de reventa, Multi-Generation | 1,028,000 | SGD | 2024 | ídem | ídem | ídem | ídem | |
| Transacciones de reventa registradas FY2024 (total) | 28,508 | transacciones | FY2024 | HDB | HDB Key Statistics 2024/2025, p.7 y p.10 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | Desglose por tipo: 1-room 12; 2-room 851; 3-room 7,130; 4-room 12,274; 5-room 6,491; Executive/Multi-Gen 1,750 |
| Indicador oficial de asequibilidad ("ratio precio/renta" tipo HDB) | no se localizó un índice único publicado por HDB con ese nombre; el indicador que HDB/MND citan es la proporción del ingreso mensual dedicado a la hipoteca | — | — | MND / HDB | Mortgage Servicing Ratio (MSR), tope 30% del ingreso bruto mensual, aplicable a préstamos HDB | https://www.mas.gov.sg (regulación MSR) / declaraciones MND | no descargado | En 2022 MND declaró que ~90% de compradores en zonas no maduras y >80% en zonas maduras pagaban ≤25% de su ingreso mensual en la cuota HDB tras el EHG; cifra citada en prensa oficial, no verificada en documento primario descargado — ver huecos |

## 5. Subvenciones CPF, elegibilidad y normas de tenencia

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Enhanced CPF Housing Grant (EHG), máximo familias | 120,000 | SGD | desde 20/08/2024 | CPF Board / HDB | Enhanced CPF Housing Grant | https://www.cpf.gov.sg/member/infohub/educational-resources/a-guide-to-enhanced-cpf-housing-and-proximity-grant | no descargado (página HTML dinámica no capturable con curl estático) | Sube desde 80,000 SGD; tope de ingreso familiar mensual 9,000 SGD |
| Enhanced CPF Housing Grant (EHG), máximo solteros | 60,000 | SGD | desde 20/08/2024 | CPF Board / HDB | ídem | ídem | ídem | Sube desde 40,000 SGD |
| Hogares beneficiados del CPF Housing Grant (Family/Singles/Joint Singles), FY2024 | Family 5,927; Singles 4,358; Joint Singles 46 (total 10,331) | hogares | FY2024 | HDB | HDB Key Statistics 2024/2025, "Statistical Highlights", p.7 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | FY2023: 11,229 hogares en total |
| Hogares beneficiados de AHG + EHG, FY2024 | 15,820 | hogares | FY2024 | HDB | ídem | ídem | ídem | FY2023: 14,038 |
| Hogares beneficiados de la Proximity Housing Grant (PHG), FY2024 | 10,399 | hogares | FY2024 | HDB | ídem | ídem | ídem | |
| Tope de ingreso familiar mensual para BTO (parejas/familias) | 14,000 | SGD/mes | vigente en 2024 | MND / HDB | Written answer on review of income ceiling for HDB BTO | https://www.mnd.gov.sg/newsroom/parliament-matters/q-as/view/written-answer-by-ministry-of-national-development-on-review-of-eligible-monthly-household-income-ceiling-for-purchase-of-hdb-bto-flats-given-income-levels | raw/mnd_qa_income_ceiling.html | Página descargada pero con contenido renderizado por JavaScript (solo se recuperó la navegación, no el cuerpo de la respuesta); el importe 14,000 SGD se contrasta con múltiples fuentes de prensa que citan la misma respuesta parlamentaria |
| Tope de ingreso mensual para solteros elegibles (≥35 años) | 7,000 | SGD/mes | vigente en 2024 | MND / HDB | ídem | ídem | ídem | |
| Marco de clasificación Standard / Plus / Prime | Sustituye la antigua distinción "madura/no madura" desde el lanzamiento BTO de octubre 2024; pisos Plus y Prime llevan mayor subsidio pero MOP de 10 años (en vez de 5) y restricciones adicionales de reventa (recompra de subvención) | — | desde oct. 2024 | MND / HDB | "New Flat Classification Framework: Standard, Plus, Prime" | https://www.mnd.gov.sg/our-work/public-housing/new-flat-classification-framework | no descargado (confirmado solo vía menú de navegación de mnd_qa_income_ceiling.html y fuentes secundarias) | Ver huecos: no se descargó el documento explicativo completo del marco |
| Minimum Occupation Period (MOP), pisos Standard | 5 | años desde la entrega de llaves | vigente | HDB | Reglas de reventa HDB | https://www.hdb.gov.sg (página dinámica) | no descargado | Contado desde la toma de posesión (TOP), no desde la firma |
| Minimum Occupation Period (MOP), pisos Plus/Prime | 10 | años | desde oct. 2024 | HDB/MND | ídem | ídem | no descargado | |
| Ethnic Integration Policy (EIP) | Fija topes máximos de ocupación por grupo étnico (chino/malayo/indio y otros) por bloque y por barrio; una vez alcanzado el tope no se permite la venta a compradores de ese grupo salvo entre miembros del mismo grupo | — | introducida 1 de marzo de 1989, vigente (actualizada 25/03/2025) | Ministry of National Development / gov.sg | "HDB's Ethnic Integration Policy: Why it still matters" | https://www.gov.sg/explainers/hdb-s-ethnic-integration-policy--why-it-still-matters/ | raw/gov_sg_eip_explainer.html | Introducida en respuesta a la formación de enclaves étnicos detectada en 1989 |
| Duración del arrendamiento (lease) de los pisos HDB | 99 | años | desde 1964 (Home Ownership Scheme) | HDB | Home Ownership for the People Scheme | https://www.hdb.gov.sg (histórico) | no descargado | El Estado (vía SLA) mantiene la titularidad del suelo; el comprador adquiere un arrendamiento (leasehold), no la propiedad plena del suelo |

## 6. Coste fiscal: déficit de HDB cubierto por subvención del Estado

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Déficit neto de HDB antes de subvención del Gobierno, FY2024/2025 (año fiscal cerrado a 31/03/2025) | 6,339.012 | millones SGD | FY2024/2025 | HDB | HDB Financial Statements FY ended 31 March 2025, "Income and Expenditure Statements", p.12 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB-Financial-Statements-for-the-year-ended-31st-March-2025.pdf | raw/hdb_financial_statements_FY2025.pdf | Cifra consolidada (Grupo). HDB matriz: 6,342.277 millones SGD |
| Subvención del Gobierno recibida, FY2024/2025 | 6,349.100 | millones SGD | FY2024/2025 | HDB / Ministry of Finance | ídem, Nota 16 "Government Grant Receivable" | ídem | ídem | Cubre íntegramente el déficit, conforme a la política contable 2.18 del propio estado financiero |
| Déficit neto de HDB antes de subvención, FY2023/2024 (cerrado a 31/03/2024) | 6,764.473 | millones SGD | FY2023/2024 | HDB | ídem (columna comparativa) | ídem | raw/hdb_financial_statements_FY2025.pdf y raw/hdb_financial_statements_FY2024.pdf | |
| Subvención del Gobierno recibida, FY2023/2024 | 6,789.865 | millones SGD | FY2023/2024 | HDB | ídem | ídem | ídem | |
| Déficit del segmento "Home Ownership" (venta/desarrollo de pisos + subvenciones CPF), FY2024/2025 | 5,513 | millones SGD | FY2024/2025 | HDB | ídem, Nota 28 "Segmental Information", p.64 | ídem | raw/hdb_financial_statements_FY2025.pdf | FY2023/2024: 6,225 millones SGD |
| Gasto en programas de renovación/mejora urbana (upgrading), FY2024/2025 | 532 | millones SGD | FY2024/2025 | HDB | Comunicado de prensa "HDB Spent Over $6 Billion in FY 2024..." | https://www.hdb.gov.sg/hdb-pulse/news/2025/hdb-spent-over-$6-billion-in-fy-2024-to-keep-public-housing-affordable-and-liveable | raw/hdb_press_fy2024_deficit.html | Metadatos de la propia página oficial de HDB (metaDescription), consistente con las cifras del estado financiero |
| Déficit de HDB / PIB, FY2024/2025 | ≈0.83 | % del PIB | FY2024/2025 vs PIB 2024 | cálculo propio con datos SingStat + HDB | 6,339.0 / 765,497.5 | — | — | Cálculo del equipo, no una cifra publicada directamente |
| Déficit de HDB / PIB, FY2023/2024 | ≈0.99 | % del PIB | FY2023/2024 vs PIB 2023 | cálculo propio | 6,764.5 / 686,398.0 | — | — | ídem |
| Serie histórica de déficit HDB (parcial, no verificada en fuente primaria descargada) | FY2014/15 ≈2,020; FY2017/18 ≈1,717; FY2018/19 ≈1,986; FY2019/20 ≈2,665; FY2020/21 ≈2,346; FY2021/22 ≈4,367; FY2022/23 ≈5,380; FY2023/24 6,764.5; FY2024/25 6,339.0 | millones SGD | FY2014/15–FY2024/25 | HDB (comunicados de prensa por año) | Comunicados anuales de resultados de HDB | https://www.hdb.gov.sg/hdb-pulse/reports/annual-reports-and-financial-statements | solo los dos últimos años en raw/ (ver filas anteriores) | **Serie de ~10 años incompleta**: los años FY2014/15 a FY2022/23 se han localizado solo a través de resúmenes de prensa (Mothership, The Independent, The Online Citizen, blogs) que citan los comunicados de HDB, no se han podido descargar los originales de cada año dentro del tiempo disponible; tratar como orientativos hasta confirmarlos en hdb.gov.sg/hdb-pulse/reports — ver huecos |

## 7. Suelo: propiedad estatal y mecanismo de adquisición

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Suelo bajo gestión directa de la Singapore Land Authority (SLA) | ≈11,000 hectáreas de suelo estatal y 5,000 edificios estatales | hectáreas / nº edificios | vigente | Ministry of Law (MinLaw) / SLA | "Land Policy & Administration" | https://www.mlaw.gov.sg/about-us/what-we-do/land-policy-and-administration/ | no descargado (página HTML dinámica) | Esto es solo el suelo que gestiona directamente la SLA; no es el total del suelo estatal, ya que otras entidades (HDB, JTC, etc.) también administran suelo estatal cedido |
| % del suelo total de Singapur en manos del Estado | **no se encontró una cifra oficial única y reciente** (la cifra "~90%" muy citada en literatura académica y de prensa no proviene de una publicación oficial verificable de SLA/MinLaw en el tiempo disponible) | % | — | — | — | — | no descargado | Ver huecos: tratar el "90%" como estimación extendida, no como dato oficial confirmado |
| Mecanismo de expropiación (Land Acquisition Act) | Permite al Gobierno la adquisición forzosa de suelo privado para "desarrollo nacional" (infraestructura, vivienda pública, etc.), con compensación al propietario | — | ley de 1966 (Land Acquisition Act), vigente con enmiendas | Ministry of Law / SSO (Singapore Statutes Online) | Land Acquisition Act 1966 (Cap. 152) | https://sso.agc.gov.sg/Act/LAA1966 | no descargado (no se pudo completar la descarga del texto legal dentro del tiempo disponible) | Históricamente (hasta reformas posteriores) la compensación podía fijarse por debajo del valor de mercado corriente (valores de referencia anteriores a la adquisición); MinLaw describe la compensación actual como "a valor de mercado" — ver huecos para el detalle histórico |
| Mecanismo de traspaso contable del suelo a HDB | El suelo estatal se transfiere/asigna a HDB por su valor de mercado tasado (fair value) en el momento de la transferencia; ese valor se contabiliza como coste del suelo dentro de "Properties under development" y alimenta el déficit que cubre la subvención del Gobierno | — | vigente | Ministry of Finance | Respuesta parlamentaria sobre venta de suelo estatal y tratamiento contable del coste del suelo para vivienda pública | https://www.mof.gov.sg/news-publications/parliamentary-replies/impact-from-sale-of-state-land-on-reserves-and-accounting-treatment-of-cost-of-state-land-for-public-housing | no descargado (la URL devolvió error 404 al intentar la descarga; probablemente reubicada) | Confirmado indirectamente por HDB Financial Statements FY2025, Nota 14 "Properties under development": Land 26,861.2 millones SGD (2025) / 21,973.7 millones SGD (2024) — raw/hdb_financial_statements_FY2025.pdf |

## 8. CPF: cotizaciones, cuentas y uso para vivienda

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Cotización total CPF (empleador+empleado), ≤55 años, salario ordinario | 37 | % del salario ordinario (tope 6,800 SGD/mes) | desde 01/01/2024 | CPF Board | CPF Contribution Rate Table from 1 Jan 2024, Tabla 1 | https://www.cpf.gov.sg/content/dam/web/employer/employer-obligations/documents/CPF_contribution_rates_from_1_Jan_2024.pdf | raw/cpf_contribution_rates_2024.pdf | Empleador 17% + empleado 20% |
| Cotización total CPF, 55-60 años | 31 | % (17.5/13.5 aprox.; empleado 16%) | desde 01/01/2024 | CPF Board | ídem | ídem | ídem | |
| Cotización total CPF, 60-65 años | 22 | % (empleado 10.5%) | desde 01/01/2024 | CPF Board | ídem | ídem | ídem | |
| Cotización total CPF, 65-70 años | 16.5 | % (empleado 7.5%) | desde 01/01/2024 | CPF Board | ídem | ídem | ídem | |
| Cotización total CPF, >70 años | 12.5 | % (empleado 5%) | desde 01/01/2024 | CPF Board | ídem | ídem | ídem | |
| Tope de salario ordinario (OW Ceiling) sujeto a cotización | 6,800 | SGD/mes | 2024 | CPF Board | ídem | ídem | ídem | Subió gradualmente hasta 8,000 SGD en 2026 (fuera del periodo de referencia solicitado) |
| Reparto de la cotización entre cuentas (Ordinary/Special/MediSave) | Se calcula primero MediSave, luego Special/Retirement Account, y el resto va a la Ordinary Account (OA), la cuenta usada para vivienda | — | desde 01/01/2024 | CPF Board | CPF Allocation Rates from 1 January 2024 | https://www.cpf.gov.sg/content/dam/web/employer/employer-obligations/documents/CPFAllocationRatesfrom_1_January_2024.pdf | raw/cpf_allocation_rates_2024.pdf | El documento da los porcentajes exactos por tramo de edad (tabla de una página) |
| Importe retirado anualmente de la Ordinary Account para vivienda | **no confirmado en cifra oficial reciente dentro del tiempo disponible** | SGD | — | CPF Board | CPF Trends – Home Financing / CPF Annual Report | https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-trends/home-financing | raw/cpf_annual_report_2023_part1.pdf; raw/cpf_annual_report_2024_part1.pdf (descargados pero no contienen una tabla estadística explícita de retiros OA por vivienda en las páginas narrativas revisadas) | Un dato de 2021 (21.9 mil millones SGD, +26.5% interanual) aparece citado en fuentes secundarias remitiendo al CPF Board, pero no se pudo confirmar la cifra 2023/2024 en el documento primario — ver huecos |
| % del total de retiros CPF que corresponde a vivienda | no localizado | % | — | CPF Board | — | — | — | Ver huecos |

## 9. BTO: tiempos de espera, sobresuscripción y volumen (2023-2025)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Pisos BTO reservados/asignados, FY2024 | 24,220 (incluye proyecciones de ventas en curso) | pisos | FY2024 | HDB | HDB Key Statistics 2024/2025, "Statistical Highlights", p.7 y p.9 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | De los cuales 18,986 vía sistema BTO y 5,092 vía Sale of Balance Flats (SBF) |
| Pisos BTO lanzados, año calendario 2024 | ≈19,600 | pisos | 2024 (3 lanzamientos: feb., jun., oct.) | HDB / MND | Comunicado "19,600 BTO flats to be launched in 2024 across three sales exercises" | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/19600-BTO-flats-to-be-launched-in-2024-across-three-sales-exercises | no descargado (enlace no accesible por curl en el tiempo disponible; confirmado vía buscador con cita directa al comunicado oficial) | |
| Pisos lanzados, julio 2025 (BTO+SBF) | 10,209 | pisos | jul. 2025 | HDB | "HDB Launches 10,209 Flats in the July 2025 BTO and SBF Sales Exercises" | https://www.hdb.gov.sg/hdb-pulse/news/2025/hdb-launches-10209-flats-in-the-july-2025-bto-and-sbf-sales-exercises | raw/hdb_press_bto_july2025.html | Página descargada correctamente (HTTP 200); metaDescription oficial confirma la cifra |
| Objetivo de tiempo de espera BTO ("Shorter Waiting Time", SWT) | HDB fijó el objetivo de que ~75% (3 de cada 4) de los pisos lanzados en 2024 tuvieran tiempos de espera de 4 años o menos; en 2024 unos 2,800 pisos (~14% de la oferta) fueron pisos SWT con esperas de hasta 2 años | años / % | 2024 | HDB / MND | Comunicados de prensa sobre suministro de pisos 2024 | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases (comunicados de oferta de pisos 2024) | no descargado | Cifra citada en varios comunicados oficiales resumidos por prensa; no se descargó el PDF/HTML original del comunicado específico |
| Tiempo de espera estándar (sin SWT) | ~4-5 | años desde solicitud a entrega de llaves | 2023-2025 | HDB | ídem | ídem | no descargado | |
| Tasa de sobresuscripción, ejercicio de junio 2024 | 3.8 | veces (ratio solicitudes/pisos) | jun. 2024 | HDB | Datos de ratio de aplicación por ejercicio ("application rate") | https://services-homes.hdb.gov.sg/sales/application-rate/bto/ | no descargado (portal interactivo, no genera archivo descargable con curl) | La más alta desde mayo de 2023 según los propios datos de HDB |
| Aplicaciones recibidas, ejercicio octubre 2024 | ~34,000 solicitudes para >8,500 pisos | solicitudes / pisos | oct. 2024 | HDB | Datos de ratio de aplicación | ídem | no descargado | Ratio aproximado de sobresuscripción 4-5x citado por HDB para ese ejercicio |
| Solicitudes de reventa registradas, FY2024 | 28,508 | solicitudes | FY2024 | HDB | HDB Key Statistics 2024/2025, p.7 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | raw/hdb_key_statistics_2025.pdf | |

## 10. Hitos históricos (fuente oficial)

| Año | Hito | Fuente oficial | URL | archivo local |
|---|---|---|---|---|
| 1960 | Creación de la Housing and Development Board (HDB), estatutaria bajo el Ministry of National Development, para sustituir al antiguo Singapore Improvement Trust | HDB / Ministry of National Development | https://www.hdb.gov.sg/about-us/our-role/history | no descargado (página dinámica) |
| 1964 | Introducción del "Home Ownership for the People Scheme": HDB empieza a vender pisos en arrendamiento de 99 años en vez de solo alquilarlos | HDB | https://www.hdb.gov.sg/about-us/our-role/history | no descargado |
| 1966 | Promulgación de la Land Acquisition Act, que da al Gobierno potestad de expropiación forzosa de suelo privado para "desarrollo nacional" | Singapore Statutes Online (SSO) / Ministry of Law | https://sso.agc.gov.sg/Act/LAA1966 | no descargado |
| 1968 | Enmienda del CPF Act que permite usar el ahorro de la Ordinary Account del CPF para comprar un piso HDB; la demanda pasa de ~3,000 solicitudes (1967) a ~70,000 (1968) | CPF Board / HDB | https://www.cpf.gov.sg (histórico institucional) | no descargado |
| 1989 | Introducción de la Ethnic Integration Policy (EIP), anunciada el 16/02/1989 por el ministro S. Dhanabalan e implementada el 1/03/1989, para evitar la formación de enclaves étnicos en los bloques HDB | Ministry of National Development / gov.sg | https://www.gov.sg/explainers/hdb-s-ethnic-integration-policy--why-it-still-matters/ | raw/gov_sg_eip_explainer.html |
| oct. 2024 | Sustitución del sistema "zona madura/no madura" por el marco Standard / Plus / Prime para nuevos lanzamientos BTO, con MOP de 10 años y clawback de subvención para pisos Plus/Prime | Ministry of National Development / HDB | https://www.mnd.gov.sg/our-work/public-housing/new-flat-classification-framework | no descargado |

---

## Cómo funciona el sistema

Singapur resolvió su crisis de vivienda de los años 60 con un modelo estatal integral,
no con un mercado libre corregido. El Estado controla el input más escaso —el suelo—
mediante la Land Acquisition Act de 1966, que permitió expropiar suelo privado para
"desarrollo nacional"; hoy la Singapore Land Authority gestiona directamente unas
11.000 hectáreas de suelo estatal (además del que administran HDB y otras entidades),
aunque no existe una cifra oficial reciente y verificable del porcentaje total de
suelo en manos públicas (la cifra de "90%" que circula es una estimación de fuentes
no oficiales). La HDB, creada en 1960, construye sobre ese suelo y vende los pisos no
en propiedad plena, sino en arrendamiento (*leasehold*) de 99 años, desde que en 1964
lanzó el "Home Ownership for the People Scheme".

La pieza que hace asequible la compra es el CPF (Central Provident Fund), un sistema
de ahorro forzoso: en 2024 un trabajador menor de 55 años cotiza el 37% de su salario
ordinario (20% el empleado, 17% el empleador, sobre un tope de 6.800 SGD/mes), y ese
ahorro se reparte entre tres cuentas, siendo la Ordinary Account —la que puede usarse
para comprar vivienda— la que permitió, desde 1968, financiar la compra de un piso
HDB con ahorro obligatorio en vez de con ahorro voluntario o crédito bancario. Sobre
esa base, el Estado añade subvenciones directas: el Enhanced CPF Housing Grant llega
hasta 120.000 SGD para familias (60.000 para solteros mayores de 35 años) desde agosto
de 2024, sujeto a un tope de ingreso familiar de 9.000 SGD/mes; en el año fiscal 2024,
10.331 hogares recibieron el CPF Housing Grant y 15.820 recibieron el AHG/EHG.

El parque resultante —1.153.080 pisos bajo gestión de HDB a marzo de 2025— cubre a
cerca del 77% de los hogares residentes y aloja al 76% de la población residente.
Los pisos se venden nuevos por sistema BTO ("Build-To-Order": se construyen tras la
demanda, no antes), con precios fijados por HDB muy por debajo del coste de
construcción y del suelo (en 2024, un 4-room en Woodlands costaba entre 329.000 y
528.000 SGD antes de subvención). La diferencia entre ese precio subvencionado y el
coste real —suelo más construcción— genera un déficit estructural en las cuentas de
HDB que cubre íntegramely el Gobierno: 6.339 millones SGD en el año fiscal cerrado en
marzo de 2025 (6.764 millones el año anterior), en torno al 0,8-1,0% del PIB anual de
Singapur, financiado desde el presupuesto general del Estado, no desde el mercado de
capitales de HDB. Desde 2024, un nuevo marco (Standard/Plus/Prime) reemplaza la vieja
distinción "zona madura/no madura": los pisos en las mejores ubicaciones (Plus/Prime)
llevan mayor subsidio pero también un periodo mínimo de ocupación (MOP) de 10 años en
vez de 5, y restricciones más duras a la reventa, para evitar que la subvención estatal
se convierta en ganancia de capital privada a corto plazo. El sistema se completa con
la Ethnic Integration Policy (1989), que limita la concentración étnica por bloque y
barrio, y con controles de asequibilidad (Mortgage Servicing Ratio, tope del 30% del
ingreso bruto mensual) que buscan que la cuota hipotecaria nunca comprometa el resto
del presupuesto familiar.

## Huecos y advertencias

- **Tasa de propiedad específica de hogares en HDB** (frente a la tasa general del
  90,8%) no se localizó desagregada en una tabla oficial dentro del tiempo disponible.
- **Superficies de 3-room, 4-room, 5-room y Executive**: solo se confirmó oficialmente
  el tamaño del 2-Room Flexi (46 m², HDB Key Statistics 2024/2025). Los demás tamaños
  citados (~65/~90/~110/~130 m²) son rangos ampliamente publicados pero no verificados
  contra una ficha técnica oficial de HDB dentro del tiempo disponible.
- **Ratio precio/renta ("price-to-income") de HDB**: no existe, hasta donde se ha
  podido comprobar, un índice único con ese nombre publicado periódicamente por HDB.
  El indicador oficial más citado es la proporción del ingreso mensual dedicada a la
  hipoteca (Mortgage Servicing Ratio, tope 30%; dato de 2022 del MND sobre uso real
  ≤25% del ingreso en la mayoría de compradores), no descargado en documento primario.
- **Serie de 10 años del déficit de HDB**: solo los ejercicios FY2023/24 y FY2024/25
  están confirmados con los estados financieros originales descargados. Los años
  FY2014/15 a FY2022/23 se han recogido de resúmenes de prensa que citan comunicados
  oficiales de HDB no descargados directamente; deben tratarse como orientativos.
- **Porcentaje de suelo total en manos del Estado**: no se encontró una cifra oficial
  reciente y única de SLA/MinLaw. La cifra "~90%" citada en múltiples fuentes
  académicas y periodísticas no pudo verificarse contra una publicación oficial
  primaria en el tiempo disponible.
- **Detalle histórico de compensación en la Land Acquisition Act de 1966** (si el
  precio de expropiación fue igual, superior o inferior al valor de mercado en cada
  época) no se documentó con el texto legal original (sso.agc.gov.sg) por limitaciones
  de tiempo; solo se registró la caracterización general de MinLaw ("compensación a
  valor de mercado" en el régimen actual).
- **Importe y porcentaje de retiros de la Ordinary Account del CPF destinados a
  vivienda** (2023/2024): no se localizó una cifra oficial reciente dentro de los
  informes anuales del CPF Board descargados (son informes narrativos; los datos
  estadísticos detallados probablemente están en publicaciones separadas de
  "CPF Trends" no descargadas).
- Varias páginas oficiales (mof.gov.sg, hdb.gov.sg con ciertas rutas antiguas,
  mnd.gov.sg, singstat.gov.sg con rutas .ashx) devolvieron error 404 al intentar la
  descarga directa con curl, probablemente por reestructuración reciente de esos
  sitios o por ser páginas renderizadas en el cliente (JavaScript); en esos casos se
  dejó constancia explícita de "no descargado" en la tabla y, cuando fue posible, se
  contrastó la cifra con al menos una fuente que cita directamente el documento
  oficial.
- Los precios BTO detallados (apartado 4) corresponden a FY2024 (año fiscal cerrado
  en marzo de 2025) y a seis ciudades no maduras/mixtas publicadas en HDB Key
  Statistics; no cubren todas las ciudades ni el nuevo marco Plus/Prime en detalle.
