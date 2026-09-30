# Ficha de datos — Revisión r2 (calendario de pago, mapa provincial, comparativas y Singapur)

Datos añadidos el 28-09-2026 para responder al feedback sobre la r1. Originales en `raw/` (con `MANIFIESTO.sha256`), tablas limpias en `limpio/` generadas por `scripts/procesar_r2.py`. Todas las fuentes son oficiales.

## 1. Flujos demográficos (calendario de pago)

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Defunciones, total nacional | 436.118 | personas | 2024 | INE | Movimiento Natural de la Población, tabla 6545 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/6545?nult=3 | raw/ine_defunciones_6545.json | 2023: 436.124; 2022: 464.417 |
| Defunciones (tabla alternativa, contraste) | — | personas | 2022-2024 | INE | MNP, tabla 6561 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/6561?nult=3 | raw/ine_defunciones_6561.json | Solo para contrastar la 6545 |
| Saldo migratorio exterior de adultos | ≈ 472.000 | personas | 2024 | INE | Estadística de Migraciones, tabla 69759 (saldo exterior por edad) | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/69759?nult=2 | raw/ine_saldos_migratorios_69759.json | Cálculo propio: grupos de 20 años o más completos y el 40 % del grupo 15-19 (edades 18-19) |
| Personas que cumplen 18 años | ≈ 551.000 | personas/año | 2027 | INE | Proyección de población a largo plazo (ya conservada en la r1, `demografia/limpio/`) | ver ficha de demografía | — | Cálculo del modelo |
| Crecimiento neto medio de adultos a 30 años | ≈ 180.000 | personas/año | 2027-2056 | INE | Proyección de población a largo plazo | ver ficha de demografía | — | Base de `anual_total` en la r2 |

## 2. Gasto público por funciones (comparativas)

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Pensiones de vejez (GF1002) | 153.051 / 10,2 | millones € / % PIB | 2023 | Eurostat (fuente IGAE) | gov_10a_exp, COFOG, S13 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_exp?format=JSON&geo=ES&sector=S13&na_item=TE&unit=MIO_EUR&unit=PC_GDP&cofog99=GF09&cofog99=GF02&cofog99=GF1002&cofog99=GF07&cofog99=GF10&cofog99=TOTAL&time=2023 | raw/eurostat_cofog_es_2023.json | Último año COFOG cerrado |
| Sanidad (GF07) | 98.630 / 6,6 | millones € / % PIB | 2023 | Eurostat (IGAE) | ídem | ídem | ídem | |
| Educación (GF09) | 62.532 / 4,2 | millones € / % PIB | 2023 | Eurostat (IGAE) | ídem | ídem | ídem | |
| Defensa (GF02) | 14.008 / 0,9 | millones € / % PIB | 2023 | Eurostat (IGAE) | ídem | ídem | ídem | |
| Protección social total (GF10) | 277.327 / 18,5 | millones € / % PIB | 2023 | Eurostat (IGAE) | ídem | ídem | ídem | |
| Gasto total AAPP | 680.225 / 45,4 | millones € / % PIB | 2023 | Eurostat (IGAE) | ídem | ídem | ídem | |

## 3. Mapa provincial

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Límites NUTS3 (provincias e islas) | 59 recintos ES (52 provincias tras agrupar islas) | geometría | 2024 | Eurostat GISCO | NUTS 2024, escala 1:10M, EPSG:4326, nivel 3 | https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/NUTS_RG_10M_2024_4326_LEVL_3.geojson | raw/gisco_nuts3_2024_10m.geojson | Simplificado (Douglas-Peucker) y proyectado en `limpio/mapa_provincias.json`; islas agrupadas en su provincia; Canarias en recuadro |
| Superficie de España | 505.983 | km² | último disponible | Eurostat | reg_area3 (landuse TOTAL) | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/reg_area3?format=JSON&geo=ES&landuse=TOTAL&unit=KM2 | raw/eurostat_reg_area3_es.json | |

Los datos por provincia (demanda, parque, suelo SIU) son los de la r1 (fichas de demografía y parque); la r2 solo añade su representación.

## 4. Singapur frente a España

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Superficie de Singapur | 744,3 | km² | 2025 | SingStat / data.gov.sg | Total Land Area of Singapore (d_0b2c034da121ef8efc71949af1694b4d) | https://data.gov.sg/api/action/datastore_search?resource_id=d_0b2c034da121ef8efc71949af1694b4d&limit=100 | raw/sg_d_0b2c034da121ef8efc71949af1694b4d.json | |
| Renta mensual mediana del hogar residente | 9.541 | SGD/mes | 2024 | SingStat / data.gov.sg | Key Household Income Trends (d_d31bb77bd99f8305e6c65b61d9762617) | https://data.gov.sg/api/action/datastore_search?resource_id=d_d31bb77bd99f8305e6c65b61d9762617&limit=100 | raw/sg_d_d31bb77bd99f8305e6c65b61d9762617.json | Incluye aportaciones del empleador al CPF; media 12.547 |
| Renta neta media por hogar en España | 38.994 | €/año | ECV 2025 (rentas 2024) | INE | ECV, tabla 9949 | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/9949?nult=1 | raw/ine_ecv_renta_hogar_9949.json | Nota de prensa en raw/ine_ecv2025_nota.pdf (https://www.ine.es/dyngs/Prensa/ECV2025.pdf). Media neta frente a mediana bruta con CPF: comparación orientativa |
| PIB per cápita PPA, Singapur | 163.354 | $ internacionales | 2025 | Banco Mundial | WDI NY.GDP.PCAP.PP.CD | https://api.worldbank.org/v2/country/SGP;ESP/indicator/NY.GDP.PCAP.PP.CD?format=json&date=2020:2025 | raw/wb_gdp_pc_ppp.json | |
| PIB per cápita PPA, España | 59.868 | $ internacionales | 2025 | Banco Mundial | ídem | ídem | ídem | Ratio ×2,7 |
| Tipo de cambio EUR/SGD | 1,48 | SGD por € | media de ago-2026 | BCE | EXR M.SGD.EUR.SP00.A | https://data-api.ecb.europa.eu/service/data/EXR/M.SGD.EUR.SP00.A?format=csvdata&startPeriod=2024-01 | raw/ecb_eur_sgd.csv | 1,4796 |

Las demás cifras de Singapur (población, precios BTO, viviendas públicas nuevas) proceden de la ficha de Singapur de la r1.

## 5. Archivos auxiliares

`raw/ine_operaciones.json` (https://servicios.ine.es/wstempus/js/ES/OPERACIONES_DISPONIBLES), `raw/ine_tablas_op309.json` y `raw/ine_tablas_op455.json` (listados `TABLAS_OPERACION` del INE) sirvieron para localizar las tablas; el modelo no los lee.

## Límites

- El saldo migratorio de 18-19 años se aproxima con el 40 % del grupo 15-19.
- Las rentas de Singapur y España no son homogéneas (mediana bruta con CPF frente a media neta); la comparación de años de renta es orientativa y así se dice en el HTML.
- COFOG 2023 es el último año cerrado; los gastos de 2025-2026 serán algo mayores en euros.
