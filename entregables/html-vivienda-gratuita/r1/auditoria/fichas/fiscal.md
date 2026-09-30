# Ficha de datos — Cuentas públicas, impuestos y deuda (España)

Frente: viabilidad fiscal de una «vivienda gratuita universal» financiada con impuestos.
Todas las fuentes son oficiales (INE, IGAE, AEAT, Banco de España, Ministerio de Sanidad, Ministerio de Hacienda, Eurostat, AIReF, Tesoro Público, Comisión Europea/BOE). Archivos originales en `raw/`, tablas limpias en `limpio/*.csv`.

> Nota de contexto temporal: la fecha de referencia de este trabajo es septiembre de 2026. Por ello, "2025" es ya dato cerrado o provisional consolidado (no una previsión) en la mayoría de fuentes, y existen datos reales de 2026 (T1–T2) además de proyecciones oficiales para el resto de 2026 y 2027.

## 1. PIB nominal de España

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| PIB pm, precios corrientes, suma trimestres 2025 | 1.690.012 | millones € | 2025 (provisional) | INE | Contabilidad Nacional Trimestral (CNTR), tabla 67823 "PIB pm Demanda (Precios corrientes)" | https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/67823?nult=8&det=2 | raw/ine_pib_demanda_corrientes_det.json | Suma de los 4 trimestres NSA (no ajustados de estacionalidad); dato "Provisional" según INE Tempus |
| PIB pm 2025T1 | 397.762 | millones € | 2025T1 | INE | CNTR tabla 67823 | ídem | ídem | |
| PIB pm 2025T2 | 423.891 | millones € | 2025T2 | INE | CNTR tabla 67823 | ídem | ídem | |
| PIB pm 2025T3 | 417.091 | millones € | 2025T3 | INE | CNTR tabla 67823 | ídem | ídem | |
| PIB pm 2025T4 | 451.268 | millones € | 2025T4 | INE | CNTR tabla 67823 | ídem | ídem | |
| PIB pm 2026T1 (dato real) | 422.650 | millones € | 2026T1 | INE | CNTR tabla 67823 | ídem | ídem | |
| PIB pm 2026T2 (dato real) | 447.365 | millones € | 2026T2 | INE | CNTR tabla 67823 | ídem | ídem | |
| Crecimiento PIB nominal 2025 | +5,8 | % | 2025 | AEAT / INE | Informe Anual de Recaudación Tributaria 2025, cap. 1 | https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_Anuales_de_Recaudacion_Tributaria/Ejercicio_2025/IART25_es_es.pdf | raw/aeat_informe_anual_recaudacion_2025.pdf | Confirma de forma independiente la cifra calculada a partir del INE |
| Previsión PIB nominal 2026 | 1.774.513 (≈ +5,0%) | millones € (estimado) / % | 2026 (proyección, cierre mayo 2026) | Banco de España | Informe Trimestral T2 2026, Cuadro 2 "Proyección de las principales macromagnitudes" | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/26/T2/Fich/be2602-it.pdf | raw/bde_informe_trimestral_2026T2.pdf | El BdE publica tasas de variación, no niveles; el nivel en € es cálculo propio (PIB 2025 × 1,05) |
| Previsión PIB nominal 2027 | ≈ +4,3 | % (variación) | 2027 (proyección) | Banco de España | ídem | ídem | ídem | |

## 2. AAPP: gasto, ingresos, déficit y deuda

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Gasto total AAPP | 725.001 / 45,5 | millones € / % PIB | 2024 | Eurostat (fuente IGAE) | gov_10a_main, sector S13, España | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main?format=JSON&geo=ES&sector=S13&na_item=TE&na_item=TR&unit=MIO_EUR&unit=PC_GDP&time=2023&time=2024&time=2025 | raw/eurostat_gov_10a_main_ES_2025.json | |
| Gasto total AAPP | 764.884 / 45,3 | millones € / % PIB | 2025 | Eurostat (fuente IGAE) | gov_10a_main | ídem | ídem | |
| Ingresos totales AAPP | 673.734 / 42,3 | millones € / % PIB | 2024 | Eurostat (fuente IGAE) | gov_10a_main | ídem | ídem | |
| Ingresos totales AAPP | 724.554 / 42,9 | millones € / % PIB | 2025 | Eurostat (fuente IGAE) | gov_10a_main | ídem | ídem | |
| Déficit público (B9) | -51.267 / -3,2 | millones € / % PIB | 2024 | Eurostat (Procedimiento de Déficit Excesivo) | gov_10dd_edpt1, sector S13 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10dd_edpt1?format=JSON&geo=ES&sector=S13&na_item=B9&na_item=GD&unit=MIO_EUR&unit=PC_GDP&time=2023&time=2024&time=2025 | raw/eurostat_gov_10dd_edpt1_ES.json | |
| Déficit público (B9) | -40.330 / -2,4 | millones € / % PIB | 2025 | Eurostat (PDE) | gov_10dd_edpt1 | ídem | ídem | Coincide con la cifra "excluyendo DANA" citada por AIReF |
| Deuda pública (consolidada, GD) | 1.620.573,4 / 101,6 | millones € / % PIB | 2024 | Eurostat (PDE) | gov_10dd_edpt1 | ídem | ídem | |
| Deuda pública (consolidada, GD) | 1.698.224,6 / 100,7 | millones € / % PIB | 2025 | Eurostat (PDE) | gov_10dd_edpt1 | ídem | ídem | |
| Déficit AAPP proyectado | -2,4 | % PIB | 2026 (proyección) | Banco de España | Informe Trimestral T2 2026, Cuadro 2 | https://www.bde.es/f/webbe/SES/Secciones/Publicaciones/InformesBoletinesRevistas/BoletinEconomico/26/T2/Fich/be2602-it.pdf | raw/bde_informe_trimestral_2026T2.pdf | |
| Deuda AAPP proyectada | 98,9 | % PIB | 2026 (proyección) | Banco de España | ídem | ídem | ídem | |
| Deuda AAPP proyectada | 97,9 | % PIB | 2027 (proyección) | Banco de España | ídem | ídem | ídem | |

CSV: `limpio/02_aapp_ingresos_gastos_deficit_deuda.csv`

## 3. Gasto público por funciones (COFOG), último año (2023)

| función | código | España (M€) | España (%PIB) | UE-27 (M€) | UE-27 (%PIB) |
|---|---|---|---|---|---|
| Vivienda y servicios comunitarios (total) | GF06 | 7.821 | 0,5 | 201.252,7 | 1,2 |
| — Desarrollo de la vivienda (subfunción) | GF0601 | 2.961 | 0,2 | 120.782,1 | 0,7 |
| Sanidad | GF07 | 98.630 | 6,6 | 1.249.906,1 | 7,2 |
| Protección social (total) | GF10 | 277.327 | 18,5 | 3.310.555,1 | 19,1 |
| — Vejez (pensiones) | GF1002 | 153.051 | 10,2 | n/d | n/d |
| — Vivienda (dentro de protección social) | GF1006 | 627 | ~0,0 | 63.557,7 | 0,4 |
| **Vivienda TOTAL (GF0601+GF1006)** | — | **3.588** | **~0,2** | **184.339,8** | **~1,1** |

Fuente: Eurostat, dataset `gov_10a_exp` (sector S13), https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_exp?format=JSON&geo=ES&sector=S13&na_item=TE&unit=MIO_EUR&unit=PC_GDP&cofog99=GF0601&cofog99=GF06&cofog99=GF1006&cofog99=GF10&cofog99=GF07&cofog99=GF1002&time=2022&time=2023 (España) y análoga con `geo=EU27_2020` (UE-27). Archivos: `raw/eurostat_gov_10a_exp_ES_v2.json`, `raw/eurostat_gov_10a_exp_EU27_v2.json`. CSV: `limpio/03_cofog_gasto_funciones.csv`.

**Hallazgo clave**: España dedica ~0,2% del PIB a vivienda (GF0601+GF1006) frente a ~1,1% del PIB de media en la UE-27 — más de 5 veces menos. En euros, igualar la media UE-27 supondría multiplicar por ~5 el gasto actual en vivienda (unos 15.000-16.000 M€ adicionales sobre PIB 2025).

## 4. Gasto sanitario público (referencia de "lo que cuesta la sanidad")

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Gasto sanitario público total | 101.739 | millones € | 2024 | Ministerio de Sanidad | Estadística de Gasto Sanitario Público (EGSP) | https://www.sanidad.gob.es/gabinete/notasPrensa.do?id=6908 (nota reproducida en https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/sanidad14/paginas/2026/130526-gasto-sanitario-publico-2024.aspx) | raw/lamoncloa_gasto_sanitario_2024.html | |
| Gasto sanitario público (% PIB) | 6,4 | % PIB | 2024 | Ministerio de Sanidad | ídem | ídem | ídem | |
| Gasto sanitario público por habitante | 2.084 | €/habitante | 2024 | Ministerio de Sanidad | ídem | ídem | ídem | |
| Variación interanual | +4,2 | % | 2024 vs 2023 | Ministerio de Sanidad | ídem | ídem | ídem | |
| Gasto sanitario público total (serie histórica, verificación) | 97.661,2 (calculado) | millones € | 2023 | Ministerio de Sanidad | Cuentas Satélite del Gasto Sanitario Público, tablas 2002-2023 | https://www.sanidad.gob.es/estadEstudios/estadisticas/sisInfSanSNS/pdf/egspGastoReal.pdf | raw/sanidad_egsp_gastoreal.pdf | Suma de sectores (Admón. Central + Seg. Social + Mutualidades + CC.AA. + Corporaciones Locales); coherente con 101.739 M€ en 2024 (+4,2%) |
| Gasto sanitario público (%PIB, Eurostat COFOG) | 6,6 | % PIB | 2023 | Eurostat | gov_10a_exp GF07 | ver sección 3 | raw/eurostat_gov_10a_exp_ES_v2.json | Ligera diferencia metodológica con Ministerio de Sanidad (6,4% en 2024) por clasificación COFOG vs cuenta satélite |

CSV: `limpio/04_sanidad.csv`

## 5. Recaudación tributaria y presión fiscal

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Ingresos tributarios totales AEAT | 325.356 | millones € | 2025 | AEAT | Informe Anual de Recaudación Tributaria 2025, "Resumen" | https://sede.agenciatributaria.gob.es/static_files/AEAT/Estudios/Estadisticas/Informes_Estadisticos/Informes_Anuales_de_Recaudacion_Tributaria/Ejercicio_2025/IART25_es_es.pdf | raw/aeat_informe_anual_recaudacion_2025.pdf | +10,4% vs 2024 |
| IRPF | 142.466 | millones € | 2025 | AEAT | ídem, cap. 2 | ídem | ídem | +10,1% |
| Impuesto sobre Sociedades | 42.266 | millones € | 2025 | AEAT | ídem, cap. 3 | ídem | ídem | +8,1% |
| IVA | 99.532 | millones € | 2025 | AEAT | ídem, cap. 4 | ídem | ídem | +9,9% |
| Impuestos Especiales | 23.083 | millones € | 2025 | AEAT | ídem, cap. 5 | ídem | ídem | +4,3% |
| Cotizaciones sociales (D61) | 197.003 | millones € | 2023 | Eurostat | gov_10a_taxag, sector S13 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_taxag?format=JSON&geo=ES&sector=S13&unit=MIO_EUR&na_item=D61&time=2022&time=2023 | raw/eurostat_social_contrib_ES.json | |
| Presión fiscal total (impuestos + cotizaciones) España | 36,8 | % PIB | 2023 | Eurostat | gov_10a_taxag | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_taxag?format=JSON&geo=ES&geo=EU27_2020&sector=S13&unit=PC_GDP&na_item=D2_D5_D91&na_item=D2_D5_D91_D61_M_D995&na_item=D211&na_item=D51&time=2022&time=2023 | raw/eurostat_gov_10a_taxag.json | |
| Presión fiscal total UE-27 | 39,7 | % PIB | 2023 | Eurostat | ídem | ídem | ídem | España ~2,9 puntos por debajo de la media UE |

CSV: `limpio/05_recaudacion_tributaria.csv`, `limpio/06_presion_fiscal.csv`

## 6. IRPF por tramos (AEAT, Estadística de los declarantes del IRPF 2023 — último ejercicio publicado)

Tabla completa en `limpio/07_irpf_tramos_2023.csv`. Fuente: AEAT, "Estadística de los declarantes del IRPF: 2023", partida 595 (Cuota resultante de la autoliquidación) y partida 435 (Base imponible general), por tramos de rendimiento.
URL base: https://sede.agenciatributaria.gob.es/AEAT/Contenidos_Comunes/La_Agencia_Tributaria/Estadisticas/Publicaciones/sites/irpf/2023/home.html
Archivos locales: `raw/aeat_irpf_2023_595_cuota_resultante_tabla.html`, `raw/aeat_irpf_2023_435_baseimponiblegeneral_tabla.html`

| tramo (rendimiento, €) | nº declarantes | % | cuota resultante total (€) | cuota media (€) | base imponible general (€) | tipo medio efectivo aprox. (%) |
|---|---|---|---|---|---|---|
| Negativo o cero | 1.270.127 | 5,30% | 176.331 | 4.766 | -688.445.925 | n/a |
| (0 - 1.500] | 1.691.865 | 7,05% | 293.781 | 190 | 445.004.112 | 0,07% |
| (1.500 - 6.000] | 3.127.766 | 13,04% | 4.567.774 | 43 | 11.421.045.903 | 0,04% |
| (6.000 - 12.000] | 2.688.297 | 11,21% | 753.441.925 | 450 | 23.146.938.905 | 3,26% |
| (12.000 - 21.000] | 4.302.709 | 17,94% | 7.265.122.953 | 1.806 | 72.250.134.157 | 10,06% |
| (21.000 - 30.000] | 4.277.053 | 17,83% | 15.881.458.369 | 3.761 | 105.462.578.500 | 15,06% |
| (30.000 - 60.000] | 5.282.994 | 22,02% | 44.169.592.854 | 8.370 | 206.653.385.643 | 21,38% |
| (60.000 - 150.000] | 1.170.735 | 4,88% | 28.462.476.734 | 24.317 | 88.860.368.854 | 32,03% |
| (150.000 - 601.000] | 160.927 | 0,67% | 13.128.053.696 | 81.586 | 28.578.584.666 | 45,94% |
| Mayor de 601.000 | 14.738 | 0,06% | 8.008.604.978 | 543.472 | 11.116.532.372 | 72,05% |
| **TOTAL** | **23.987.211** | **100%** | **117.673.789.396** | **7.067** | **547.246.127.188** | **21,51%** |

Notas: "declarantes" = 23.987.211 (total nacional 2023); de ellos, 16.651.601 tuvieron cuota resultante positiva. El "tipo medio efectivo" de la última columna es un cálculo propio (cuota resultante del tramo ÷ base imponible general del tramo); no es exactamente el tipo medio estatal+autonómico sobre base liquidable que publica la AEAT en otras tablas (partida 587, cuota líquida incrementada), pero sirve como aproximación razonable de la progresividad real observada para simular una subida de tramos.

## 7. IVA

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Recaudación IVA | 99.532 | millones € | 2025 | AEAT | Informe Anual de Recaudación Tributaria 2025, cap. 4 | https://sede.agenciatributaria.gob.es/static_files/AEAT/.../IART25_es_es.pdf | raw/aeat_informe_anual_recaudacion_2025.pdf | +9,9% vs 2024 |
| Recaudación IVA (%PIB) | 6,4 | % PIB | 2023 | Eurostat | gov_10a_taxag D211 | ver sección 5 | raw/eurostat_gov_10a_taxag.json | |
| Beneficio fiscal total tipos reducidos IVA | 31.299,10 | millones € | 2023 | Ministerio de Hacienda | Memoria de Beneficios Fiscales, PGE 2023 (proyecto) | https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Proyecto/MaestroTomos/PGE-ROM/doc/L_23_A_A2.PDF | raw/pge2023_memoria_beneficios_fiscales.pdf | |
| — del que, tipo 4% (superreducido) | 8.604,34 | millones € | 2023 | ídem | ídem | ídem | ídem | Permite estimar base imponible a tipo 4%: ≈50.614 M€ (beneficio ÷ 0,17) |
| — del que, tipo 10% (reducido) | 22.694,76 | millones € | 2023 | ídem | ídem | ídem | ídem | Permite estimar base imponible a tipo 10%: ≈206.316 M€ (beneficio ÷ 0,11) |

CSV: `limpio/08_iva.csv`. **No existe una cifra oficial única y explícita de "cuánto recauda un punto del tipo general del IVA"** publicada como tal por AEAT/AIReF/Hacienda (ver Huecos).

## 8. IBI

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Recaudación IBI urbana (municipios, derechos reconocidos netos) | 14.820,9 | millones € | 2023 | Ministerio de Hacienda | Haciendas Locales en Cifras. Año 2023, Tabla 32 "Ingresos de los municipios" | https://www.hacienda.gob.es/cdi/sgfal/hhll%20en%20cifras/hhll-en-cifras-2023.pdf | raw/hacienda_haciendas_locales_en_cifras_2023.pdf | Último año publicado (publicación de noviembre 2025) |
| IBI / ingresos no financieros municipales | 23,13 | % | 2023 | Ministerio de Hacienda | ídem | ídem | ídem | |
| IBI / ingresos fiscales municipales | 46,8 | % | 2023 | Ministerio de Hacienda | ídem, párrafo A11 | ídem | ídem | |
| Eficacia recaudatoria del IBI | 91,51 | % | 2023 | Ministerio de Hacienda | ídem, párrafo A11 | ídem | ídem | |

CSV: `limpio/09_ibi.csv`. **No se ha localizado el número de recibos de IBI a nivel nacional** en esta publicación (ver Huecos).

## 9. Presupuesto actual de vivienda (PGE) y beneficios fiscales

El PGE vigente es el de **2023** (prorrogado consecutivamente para 2024, 2025 y 2026, al no haberse aprobado nuevos presupuestos).

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Política de gasto 26 "Acceso a la vivienda y fomento de la edificación" (TOTAL) | 3.476,84 | millones € | 2023 (PGE vigente) | Ministerio de Hacienda / Congreso | PGE 2023 (Ley), Informe Económico y Financiero | https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Ley/MaestroDocumentos/PGE-ROM/doc/3/1/3/2/N_23_E_A_1_2_2_11.PDF | raw/pge2023_ley_politica26_vivienda.pdf | 997 M€ sin MRR + 2.480 M€ financiados por el Mecanismo de Recuperación y Resiliencia |
| Plan Estatal de Vivienda 2022-2025 — subvenciones anuales | 359 | millones € | 2023 | ídem | ídem | ídem | ídem | |
| Bono Alquiler Joven | 200 | millones € | 2023 | ídem | ídem | ídem | ídem | |
| Deducción IRPF por inversión en vivienda habitual (régimen transitorio) | 753,51 | millones € | 2023 | Ministerio de Hacienda | Memoria de Beneficios Fiscales PGE2023, Cuadro 1 IRPF (C.1) | https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Proyecto/MaestroTomos/PGE-ROM/doc/L_23_A_A2.PDF | raw/pge2023_memoria_beneficios_fiscales.pdf | 2.663.223 beneficiarios |
| Deducción IRPF por alquiler de vivienda habitual (régimen transitorio) | 29,74 | millones € | 2023 | ídem | ídem, (C.2) | ídem | ídem | 147.690 beneficiarios |
| Reducción en base imponible por arrendamiento de viviendas (propietarios) | 716,61 | millones € | 2023 | ídem | ídem, (A.2) | ídem | ídem | 2.033.555 beneficiarios |

CSV: `limpio/10_pge_vivienda.csv`

## 10. Reglas fiscales de la UE y coste de la deuda

| variable | valor | unidad | fecha ref | organismo | tabla/documento | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Límite de déficit | 3,0 | % PIB | vigente | UE (Reglamento 2024/1263 / TFUE) | Plan Fiscal y Estructural de Medio Plazo España 2025-2028 | https://economy-finance.ec.europa.eu/document/download/45e0463e-1216-459a-820a-c7eb9381f27d_es?filename=national_medium-term_fiscal-structural_plan_spain_es.pdf | raw/plan_fiscal_estructural_espana_2025_2028.pdf | |
| Límite de deuda | 60,0 | % PIB | vigente | UE | ídem | ídem | ídem | |
| Trayectoria de gasto neto acordada España | 3,4 (2025-2028) / 3,0 (2025-2031) | % anual | 2025-2031 | Comisión Europea / España | Plan Fiscal y Estructural de Medio Plazo España 2025-2028, avalado por la Comisión (nov. 2024) y aprobado por el Consejo (ene. 2025) | ídem | ídem | Periodo extendido a 7 años por reformas e inversiones comprometidas |
| Déficit público 2023 (punto de partida del Plan) | 3,5 | % PIB | 2023 | España/CE | ídem | ídem | ídem | |
| Objetivo déficit 2031 | 0,8 | % PIB | 2031 (proyección) | España/CE | ídem | ídem | ídem | |
| Objetivo deuda 2031 | ~90 | % PIB | 2031 (proyección) | España/CE | ídem | ídem | ídem | |
| Tipo de interés medio de la deuda del Estado en circulación | 2,089 / 2,214 / 2,433 | % | 2023 / 2024 / ago-2026 | Tesoro Público | Estadísticas de la Deuda del Estado (31/08/2026) | https://www.tesoro.es/sites/default/files/estadisticas/Estadisticas_ES.pdf | raw/tesoro_estadisticas_deuda.pdf | |
| Rentabilidad bono a 10 años (última emisión) | 3,448 | % | mayo 2026 | Tesoro Público | Nota de prensa La Moncloa, emisión de bonos | https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/economia-comercio-empresa/paginas/2026/270526-emision-bonos-tesoro-publico.aspx | (no descargado; referencia web) | |
| Gasto en intereses de la deuda pública | 35.551 (2,4% PIB) / 38.793 (2,4% PIB) | millones € / %PIB | 2023 / 2024 | Eurostat | gov_10dd_edpt1, D41PAY | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10dd_edpt1?format=JSON&geo=ES&sector=S13&na_item=D41PAY&unit=MIO_EUR&unit=PC_GDP&time=2023&time=2024 | raw/eurostat_interest_expenditure_ES.json | |

CSV: `limpio/11_reglas_fiscales_ue_y_deuda.csv`

---

## Huecos y advertencias

1. **Valor de un punto del IVA general**: no existe una cifra oficial única publicada por AEAT, AIReF o Hacienda como "recaudación de 1 punto del tipo general (21%)". Se aportan piezas para estimarlo (recaudación total IVA 2025 = 99.532 M€; bases imponibles a tipos reducidos deducidas de la Memoria de Beneficios Fiscales 2023: ≈206.316 M€ a tipo 10% y ≈50.614 M€ a tipo 4%), pero la base sujeta al tipo general (21%) no se pudo aislar en el tiempo disponible; requeriría el Cuadro 8.7 del propio informe AEAT (archivo Excel/PDF enlazado aparte, no descargado) o el detalle de "gasto final sujeto a IVA por tipos".
2. **Número de recibos de IBI**: la publicación "Haciendas Locales en Cifras 2023" da la recaudación total (14.820,9 M€) pero no el número de recibos girados a nivel nacional; no se ha localizado esa cifra en el tiempo disponible (podría estar en Catastro, no consultado).
3. **PGE vigente = 2023 prorrogado**: España lleva desde 2024 sin presupuestos nuevos aprobados (prórroga consecutiva por tercer año en 2026); todas las cifras de "presupuesto actual" corresponden al PGE 2023 (Ley), no a un PGE 2025 o 2026 (que no existen como documentos aprobados). El "Plan Estatal de Vivienda 2026-2030" sucesor del 2022-2025 se anunció (17/09/2025, La Moncloa) con una dotación global de 7.000 M€ para todo el periodo, pero no se ha aprobado aún como partida presupuestaria anual ejecutable; no se incluye en las tablas por no ser gasto ejecutado ni presupuesto en vigor.
4. **IRPF por tramos**: se usa el ejercicio 2023 (último publicado por AEAT en la Estadística de declarantes). El "tipo medio efectivo" por tramo es un cálculo propio (cuota resultante de la autoliquidación ÷ base imponible general del mismo tramo), no una serie oficial directa; la AEAT publica series de tipo medio sobre bases distintas (líquida, liquidable) que no se cruzaron por tramos en el tiempo disponible.
5. **PIB 2026 (nivel en euros)**: el Banco de España publica tasas de variación (nominal +5,0% en 2026, +4,3% en 2027), no niveles en euros; el nivel de 1.774.513 M€ para 2026 es un cálculo propio (PIB 2025 real × tasa proyectada), no una cifra publicada directamente por el BdE.
6. **Gasto sanitario 2025**: el Ministerio de Sanidad solo tenía publicado el dato de 2024 (101.739 M€, 6,4% PIB) en el momento de la consulta; no se ha localizado el cierre de 2025.
7. **COFOG vivienda vs Ministerio de Vivienda**: las cifras de Eurostat/IGAE (GF0601+GF1006 ≈ 3.588 M€ en 2023) son de contabilidad nacional (gasto consolidado de todas las AAPP) y no coinciden exactamente con la "Política de gasto 26" del PGE (3.476,84 M€, solo AGE) por diferencias de perímetro (AGE vs. AAPP consolidadas, incluye CC.AA. y ayuntamientos) y de año (2023 en ambos casos, coincidencia razonable que valida ambas fuentes).
8. **Deducciones fiscales por vivienda**: los importes de la Memoria de Beneficios Fiscales corresponden al **proyecto** de PGE 2023 (última memoria de beneficios fiscales disponible dado que no hay PGE posterior); no se ha localizado una actualización 2025/2026 de este documento porque no se ha tramitado un nuevo PGE.
9. Todos los importes en miles/millones de euros se han verificado por consistencia interna (ej. Media × Número ≈ Importe en las tablas de IRPF; suma de trimestres del PIB ≈ cifra de crecimiento anual citada por AEAT) para detectar errores de formato numérico español (punto = separador de miles, coma = decimal) en la extracción automática de las fuentes HTML/PDF.
