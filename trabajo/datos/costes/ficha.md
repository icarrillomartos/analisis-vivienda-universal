# Ficha de datos oficiales — Precio de mercado y coste de construcción de vivienda en España

Encargo: viabilidad de "vivienda gratuita universal" — frente de precio de mercado y coste de construir una vivienda "de abajo arriba".
Elaborado por: analista de costes (perfil aparejador/economista de la construcción), asistido por Claude (modelo Sonnet 5 / claude-sonnet-5).
Fecha de elaboración: 28-09-2026. Todas las fuentes son oficiales (MIVAU, INE, BOE, Catastro, Banco de España, Juntas/Generalitats/Comunidades Autónomas, IVE-UPV como entidad pública instrumental de la Generalitat Valenciana). No se han usado portales inmobiliarios, prensa ni generadores privados de precios.

Todos los archivos originales descargados están en `raw/`. Los CSV limpios/derivados están en `limpio/`. El script de extracción MIVAU está en `scripts/extraer_mivau_valor_tasado.py`.

---

## 1. Precio de mercado de la vivienda libre

### 1.1 Valor tasado de vivienda libre — Serie nacional y por provincia objetivo, 2T 2026 (último dato publicado)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Valor tasado vivienda libre, Total Nacional | 2.355,0 | €/m² | 2T 2026 | MIVAU | Estadística de Valor Tasado de Vivienda, Tabla 1 | https://apps.fomento.gob.es/boletinonline2/sedal/35101000.XLS | mivau_valor_tasado_nacional_serie.xls | Variación interanual 1T→2T2026: +1,7% trimestral; anual +12,5% |
| Valor tasado vivienda libre, provincia Madrid | 4.089,6 | €/m² | 2T 2026 | MIVAU | ídem, hoja "2023,2024,2025,2026" | ídem | ídem | Provincia uniprovincial = CCAA Madrid |
| Valor tasado vivienda libre, provincia Barcelona | 3.204,2 | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| Valor tasado vivienda libre, provincia Valencia/València | 1.980,1 | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| Valor tasado vivienda libre, provincia Sevilla | 1.889,8 | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |
| Valor tasado vivienda libre, provincia Zaragoza | 1.944,3 | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | Provincia uniprovincial |
| Valor tasado vivienda libre, provincia Málaga | 3.083,5 | €/m² | 2T 2026 | MIVAU | ídem | ídem | ídem | |

Serie nacional anual completa (media de los 4 trimestres de cada año, calculada a partir de los datos oficiales trimestrales del MIVAU; 2026 solo tiene 2 trimestres) desde 1995: ver `limpio/mivau_valor_tasado_serie_nacional_y_provincias_anual.csv` (224 filas: nacional + las 6 provincias/CCAA objetivo, todos los años). Selección relevante:

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Valor tasado vivienda libre, Total Nacional (media anual) | 1.019,0 | €/m² | 2000 | MIVAU | ídem, hoja "1999,2000,2001,2002" | ídem | ídem | Media de los 4 trimestres de 2000 |
| Valor tasado vivienda libre, Total Nacional (media anual) | 1.799,1 | €/m² | 2007 | MIVAU | ídem, hoja "2003…2006" y "2007…2010" | ídem | ídem | Pico previo a la crisis (aprox., ver CSV) |
| Valor tasado vivienda libre, Total Nacional (media anual) | 2.335,3 | €/m² | 2026 (parcial, 2 trim.) | MIVAU | ídem, hoja "2023,2024,2025,2026" | ídem | ídem | Media de 1T+2T 2026 únicamente |

### 1.2 Valor tasado por municipio (>25.000 hab.), 2T 2026

| variable | valor total | valor ≤5 años | valor >5 años | unidad | fecha ref | organismo | URL exacta | archivo local |
|---|---|---|---|---|---|---|---|---|
| Madrid (municipio) | 5.418,4 | 6.205,3 | 5.395,0 | €/m² | 2T 2026 | MIVAU | https://apps.fomento.gob.es/boletinonline2/sedal/35103500.XLS | mivau_valor_tasado_municipios25000.xls |
| Barcelona (municipio) | 4.601,8 | 5.109,8 | 4.594,6 | €/m² | 2T 2026 | MIVAU | ídem | ídem |
| Valencia (municipio) | 2.972,8 | 3.464,9 | 2.957,4 | €/m² | 2T 2026 | MIVAU | ídem | ídem |
| Sevilla (municipio) | 2.652,3 | 2.995,3 | 2.640,6 | €/m² | 2T 2026 | MIVAU | ídem | ídem |
| Zaragoza (municipio) | 2.240,3 | 2.552,2 | 2.230,9 | €/m² | 2T 2026 | MIVAU | ídem | ídem |
| Málaga (municipio) | 3.320,5 | 4.140,3 | 3.282,7 | €/m² | 2T 2026 | MIVAU | ídem | ídem |

Tabla completa (los 6 municipios, con nº de tasaciones) en `limpio/mivau_valor_tasado_municipios_2T2026.csv`.

### 1.3 INE — Índice de Precios de Vivienda (IPV)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| IPV general, variación interanual | +12,9 | % | 1T 2026 | INE | Nota de prensa IPV 1T2026 (cambio de base a 2025=100) | https://www.ine.es/dyngs/Prensa/IPV1T26.htm | ine_ipv_1T2026_tablas.xlsx | Vivienda nueva +9,1%; segunda mano +13,5% interanual |
| IPV general, variación interanual | +12,2 | % | 2T 2026 | INE | Nota de prensa IPV 2T2026 | https://www.ine.es/dyngs/Prensa/es/IPV2T26.htm (no descargada; ver nota) | — | Dato citado en nota de prensa; no se descargó el Excel de 2T 2026 (gap) |
| IPV, mayor subida autonómica | +15,6 | % interanual | 1T 2026 | INE | Nota de prensa IPV 1T2026 | https://www.ine.es/dyngs/Prensa/IPV1T26.htm | ine_ipv_1T2026_tablas.xlsx | Aragón y Murcia empatadas; menor subida País Vasco +10,3% |

---

## 2. Coste de construcción por m²

### 2.1 Catastro — Módulo básico de construcción (MBC) y valores de repercusión de suelo (MBR)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Módulo de valor M (base del sistema) | 1.000,00 | €/m² | fijado 2005, vigente | Dirección General del Catastro | Orden EHA/1213/2005, de 26 de abril | https://www.boe.es/buscar/pdf/2005/BOE-A-2005-7254-consolidado.pdf | boe_orden_eha_1213_2005_consolidado.pdf | El MBC = MBR × coeficiente (0,80–1,30 según Norma 16 RD 1020/1993); el MBR = M × coeficiente (0,18–2,80) |
| Jerarquía de repercusión de suelo, escalón R00 (máximo) | 5.554 | €/m² | 2025 | Dirección General del Catastro | Circular 01.04/2025/P, 13-feb-2025, Instrucción Tercera | https://www.catastro.hacienda.gob.es/documentos/01042025_P.pdf | catastro_circular_01042025_modulos.pdf | Coeficiente GB asociado = 1,45 |
| Jerarquía de repercusión de suelo, escalón R34 (mínimo) | 8 | €/m² | 2025 | Dirección General del Catastro | ídem | ídem | ídem | Coeficiente GB asociado = 1,00. Tabla completa (35 escalones) en `limpio/catastro_jerarquias_mbr_suelo_2025.csv` |
| Jerarquías de suelo, actualización 2026 | (35 escalones actualizados) | €/m² | 2026 | Dirección General del Catastro | Circular 02.04/2026/P | https://www.catastro.hacienda.gob.es/documentos/02042026_P.pdf | catastro_circular_02042026_modulos.pdf | Descargada pero no tabulada en detalle por límite de tiempo (gap parcial) |

Nota metodológica: el MBC catastral es un valor de referencia administrativo para valoración fiscal (incluye coste de ejecución material, beneficio del promotor, honorarios profesionales y tributos de la construcción, según definición de la Norma 16), **no** es directamente el PEM real de mercado; se usa aquí solo como referencia oficial de coste "de arriba abajo" y se contrasta con los datos de licitación pública y BCCA/IVE (de abajo arriba).

### 2.2 Bases de precios oficiales autonómicas

**Andalucía — Base de Costes de la Construcción de Andalucía (BCCA), actualización julio 2023 (publicada enero 2024)**

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Oficial 1ª albañilería, precio básico (coste hora todo incluido) | 23,17 | €/h | jul-2023 | Junta de Andalucía (Consejería de Fomento, Articulación del Territorio y Vivienda) | BCCA — Listado de Precios Básicos, código TO00100 | https://www.juntadeandalucia.es/organismos/fomentoarticuladodelterritorioyvivienda/.../bcca-jul-2023.html | bcca2023_listado_precios_basicos.pdf | Precio "básico" de la base = coste total repercutido por hora de oficial, incluye costes empresariales según metodología BCCA |
| Ayudante, precio básico | 22,36 | €/h | jul-2023 | Junta de Andalucía | BCCA — código TA00100 | ídem | ídem | |
| Peón especial, precio básico | 22,01 | €/h | jul-2023 | Junta de Andalucía | BCCA — código TP00100 | ídem | ídem | |
| Hormigón HA-25/B/20/XC2 suministrado | 97,10 | €/m³ | jul-2023 | Junta de Andalucía | BCCA — código CH02910 | ídem | ídem | |
| Acero B 500 S | 0,95 | €/kg | jul-2023 | Junta de Andalucía | BCCA — código CA00320 | ídem | ídem | |
| Ladrillo cerámico GAFA 25x11,5x7 cm | 87,04 | €/millar | jul-2023 | Junta de Andalucía | BCCA — código FL00200 | ídem | ídem | |

Tabla completa de precios unitarios seleccionados en `limpio/bcca_precios_unitarios_clave_jul2023.csv`. El listado íntegro de precios unitarios (partidas completas de obra, con descompuestos) está en `raw/bcca2023_listado_precios_unitarios.pdf` (301+ páginas), no volcado a CSV por volumen.

**Comunitat Valenciana — IVE (Instituto Valenciano de la Edificación), Informe sobre costes de construcción y VPO, junio 2024**

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| PEM (Presupuesto de Ejecución Material) vivienda protegida | 888 | €/m² construido | jun-2024 | IVE (entidad pública adscrita a la Generalitat Valenciana / UPV) | Informe costes construcción y VPO, pág. 5 | https://descargas.five.es/archivos/Blog/Articulos/Informe_Costes_construccion_VPO.pdf | ive_informe_costes_construccion_vpo_2024.pdf | Basado en Módulo Básico de Edificación (MBE) actualizado con fórmula 811 (RD 1359/2011) |
| PEC (Presupuesto de Ejecución por Contrata) | 1.057 | €/m² construido | 2024 | IVE | ídem | ídem | ídem | PEC = PEM × 1,19 (6% beneficio industrial + 13% gastos generales) |
| PEC histórico mínimo (post-crisis, estable 2008-2021) | 877 | €/m² construido | 2008-2021 | IVE | ídem | ídem | ídem | |
| Precio de contrata actual vivienda protegida (rango operativo) | 1.050 – 1.150 | €/m² construido | 2024 | IVE | Conclusiones del informe | ídem | ídem | Solo plantas de vivienda, excluye locales/sótanos |
| Peso de la mano de obra en el índice de revisión del MBE | 42 (término fijo) / hasta 35% en formulaciones alternativas | % | 2024 | IVE | ídem, pág. 8 | ídem | ídem | La fórmula oficial 811 no separa explícitamente mano de obra |

**Comunidad de Madrid — Base de Precios de la Construcción (BPCM)**

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Base de Precios de la Construcción de la Comunidad de Madrid | No accesible por descarga directa | — | edición 2024 (última citada) | Comunidad de Madrid (Dir. Gral. de Vivienda y Rehabilitación) | Portal "Base de Datos de la Construcción" | https://gestiona.comunidad.madrid/bdco_inter | — | **GAP**: la BPCM se sirve mediante un visor/aplicación interactiva (gestiona.comunidad.madrid), no mediante ficheros PDF/Excel descargables por URL directa; no se ha podido descargar en este encargo. Requeriría sesión interactiva o exportación manual desde el visor. |

### 2.3 Presupuestos de licitación de promociones públicas de vivienda (2024-2026)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Casa47 (antes SEPES) — licitación redacción de proyectos, Regimiento de Artillería, Sevilla, 146 viviendas asequibles | 737.660 | € (valor estimado del contrato, IVA excluido; es honorarios de redacción de proyecto, NO el PEM de obra) | 2025 | Casa47 / Ministerio de Vivienda y Agenda Urbana | Nota de prensa y licitación en Plataforma de Contratación del Sector Público | https://www.casa47.es/w/sepes-licita-los-proyectos-de-edificaci%C3%B3n... | casa47_plan_anual_actuacion_2025.pdf ; casa47_plan_anual_actuacion_2026.pdf | Este importe es de honorarios técnicos, no de PEM/PBL de la obra; no se ha localizado en el tiempo disponible el PEM/PBL de obra de esta actuación concreta en la Plataforma de Contratación del Sector Público |
| Casa47 — Plan Anual de Actuación 2025 y 2026 | Descargados íntegros | — | 2025 y 2026 | Casa47 (Entidad Estatal de Vivienda, antes SEPES) | Plan Anual de Actuación | https://www.casa47.es/documents/36596/58792/Plan+Anual+de+Actuaci%C3%B3n+2025.pdf ; .../2026.pdf | casa47_plan_anual_actuacion_2025.pdf ; casa47_plan_anual_actuacion_2026.pdf | Contienen relación de actuaciones y presupuestos globales de la entidad, no un desglose sistemático de PEM/€ por vivienda por promoción individual |
| EMVS Madrid — Plan Suma Vivienda (Los Ahijones/Los Berrocales) | >2.200 viviendas; primera fase 1.600 viviendas, contratación concluida 2025 | viviendas | 2025 | EMVS Madrid (Ayuntamiento de Madrid) | Notas de prensa oficiales del Ayuntamiento (diario.madrid.es) | https://diario.madrid.es/blog/notas-de-prensa/... | — | **GAP**: no se ha logrado descargar en el tiempo disponible un pliego/memoria valorada de la Plataforma de Contratación del Sector Público con el desglose de PEM/PBL en €/m² de esta promoción; la búsqueda solo permitió confirmar cifras de presupuesto global de la EMVS (168 M€ en 2025) y nº de viviendas, no €/m² |
| Agencia de Vivienda Social de la Comunidad de Madrid (antes IVIMA) — adquisición de 175 viviendas de alquiler social | Expediente EG/2024/0000008038 localizado | — | 2024 | Comunidad de Madrid | Portal de contratos públicos de la Comunidad de Madrid | https://www.contratos-publicos.comunidad.madrid/contrato-publico/eg20240000008038... | — | **GAP**: se localizó el expediente pero no se descargó el pliego con el desglose económico por limitación de tiempo |

**Advertencia sobre esta sección**: pese a la instrucción de conseguir 3-6 ejemplos de licitaciones públicas con PEM/PBL en €/m² y €/vivienda, en el tiempo disponible **solo se ha logrado extraer un dato de coste de construcción de promoción pública con desglose €/m² completo y trazable**: el informe del IVE sobre VPO en la Comunitat Valenciana (sección 2.2), que sí es de una entidad pública (IVE, adscrita a la Generalitat) aunque no es estrictamente un "pliego de licitación" sino un informe técnico oficial que usa el mismo PEM que se aplica en las licitaciones de VPO valencianas. Los expedientes concretos de EMVS/Casa47/Agencia de Vivienda Social citados arriba están identificados y con URL, pero no se ha completado la descarga y extracción del desglose PEM/PBL de cada uno. Se recomienda una sesión de trabajo adicional dedicada específicamente a la Plataforma de Contratación del Sector Público (contrataciondelestado.es) para completar este punto.

### 2.4 Índices de costes de la construcción (para actualizar precios)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Fórmula de revisión de precios "811. Obras de edificación general" | Kt = 0,04A+0,01B+0,08C+0,01E+0,02F+0,03L+0,08M+0,04P+0,01Q+0,06R+0,15S+0,02T+0,02U+0,01V+0,42 | fórmula polinómica | vigente desde 2011 | Ministerio de Hacienda / IVE (aplicador) | Real Decreto 1359/2011 | citada en ive_informe_costes_construccion_vpo_2024.pdf, pág. 5 | ive_informe_costes_construccion_vpo_2024.pdf | Term fijo 0,42 = parte no indexada (incluye implícitamente mano de obra) |
| Índice nacional de mano de obra en construcción (INE), evolución 2002→2023 | de 303,36 a 457,57 | índice (base no especificada en el informe) | 2002-2023 | INE (citado por IVE) | Gráfico "Índice nacional de la mano de obra en construcción" | ídem, pág. 8 | ídem | **GAP**: no se ha descargado directamente de INE la serie de índices de coste de la mano de obra en la construcción (ICMO) ni el Índice de Costes del Sector de la Construcción (ICSC); solo se dispone del dato citado indirectamente por el IVE |

---

## 3. Mano de obra: tablas salariales y coste empresa por hora

### 3.1 VII Convenio General del Sector de la Construcción (estatal, BOE) — marco de incrementos

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Incremento salarial pactado tablas provinciales 2025 | +3,50 (+0,40 adicional por cláusula de garantía IPC 2024) | % | 2025 | BOE / Comisión Negociadora VII Convenio | Resolución de 24-nov-2025, DGT (BOE-A-2025-25234) | https://www.boe.es/boe/dias/2025/12/10/pdfs/BOE-A-2025-25234.pdf | boe_resolucion_2025-25234_convenio_construccion.pdf | El convenio estatal fija porcentajes de incremento aplicables a las tablas provinciales; no fija salarios absolutos |
| Incremento salarial pactado tablas provinciales 2026 | +3,00 | % | 2026 | ídem | ídem | ídem | ídem | |

### 3.2 Convenio Colectivo del Sector de Construcción y Obras Públicas de la Comunidad de Madrid 2025-2026 (BOCM, tablas salariales reales)

Categorías del "grupo de operarios" (mano de obra directa de obra), retribución diaria y anual (salario base + plus actividad + plus extrasalarial; sin incluir pagas extra prorrateadas, ya incluidas en el TOTAL ANUAL):

| variable | valor 2025 | valor 2026 | unidad | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Encargado (Nivel VI) — total día | 67,97 | 70,01 | €/día | Comunidad de Madrid (DG Trabajo) | BOCM núm. 311, 31-dic-2025, Anexo VI (2025) y Anexo VIII (2026) | https://www.bocm.es/boletin/CM_Orden_BOCM/2025/12/31/BOCM-20251231-1.PDF | bocm_convenio_construccion_madrid_2025_2026.pdf | Texto del PDF viene con caracteres invertidos por extracción; verificado manualmente invirtiendo cadena |
| Encargado (Nivel VI) — total anual | 25.401,94 | 26.164,38 | €/año | ídem | ídem | ídem | ídem | |
| Oficial 1ª de oficio (Nivel VIII) — total día | 65,40 | 67,36 | €/día | ídem | ídem | ídem | ídem | Equivalente a "oficial de 1ª albañil" en obra de edificación |
| Oficial 1ª de oficio (Nivel VIII) — total anual | 24.372,60 | 25.103,23 | €/año | ídem | ídem | ídem | ídem | |
| Oficial 2ª de oficio (Nivel IX) — total día | 62,29 | 64,16 | €/día | ídem | ídem | ídem | ídem | |
| Oficial 2ª de oficio (Nivel IX) — total anual | 23.137,22 | 23.831,20 | €/año | ídem | ídem | ídem | ídem | |
| Especialista de 2ª / Peón especializado (Nivel XI) — total día | 60,83 | 62,66 | €/día | ídem | ídem | ídem | ídem | |
| Especialista de 2ª / Peón especializado (Nivel XI) — total anual | 22.405,53 | 23.079,10 | €/año | ídem | ídem | ídem | ídem | |
| Peón suelto (Nivel XII) — total día | 60,78 | 62,61 | €/día | ídem | ídem | ídem | ídem | |
| Peón suelto (Nivel XII) — total anual | 22.378,81 | 23.051,90 | €/año | ídem | ídem | ídem | ídem | |

Tabla completa (8 categorías, ambos años, con desglose salario base/plus actividad/plus extrasalarial) en `limpio/mano_obra_convenio_construccion_madrid_2025_2026.csv`.

### 3.3 Cotizaciones a la Seguridad Social a cargo de la empresa, 2025

| variable | tipo total | tipo empresa | tipo trabajador | fecha ref | organismo | documento/tabla | URL exacta | archivo local |
|---|---|---|---|---|---|---|---|---|
| Contingencias comunes | 28,30% | 23,60% | 4,70% | 2025 | Ministerio de la Presidencia / BOE | Orden PJC/178/2025, 25-feb-2025 | https://www.boe.es/boe/dias/2025/02/26/pdfs/BOE-A-2025-3780.pdf | boe_orden_pjc_178_2025_cotizaciones.pdf |
| Desempleo (contratación indefinida, incl. fijo-obra) | 7,05% | 5,50% | 1,55% | 2025 | ídem | ídem | ídem | ídem |
| Desempleo (contratación de duración determinada) | 8,30% | 6,70% | 1,60% | 2025 | ídem | ídem | ídem | ídem |
| FOGASA | 0,20% | 0,20% | 0% | 2025 | ídem | ídem | ídem | ídem |
| Formación profesional | 0,70% | 0,60% | 0,10% | 2025 | ídem | ídem | ídem | ídem |
| AT/EP — Construcción de edificios / Ingeniería civil / Construcción especializada (CNAE 41/42/43) | 6,70% | 6,70% (a cargo íntegro de la empresa) | 0% | 2025-2026 | Seguridad Social / LGSS | Disposición Adicional 61ª LGSS, tarifa de primas (actualizada por RDL 16/2025 para 2026, sin cambio en el tipo construcción) | https://contratos.gobierto.es/normativa/ley-general-seguridad-social/da-sexagesima-primera/versiones/3 | — (no descargado PDF; consultado vía texto consolidado) |
| Mecanismo de Equidad Intergeneracional (MEI) | 0,80% | 0,67% | 0,13% | 2025 | Seguridad Social | RDL 2/2023, disposición transitoria | (referencia normativa; no incluido en el Orden PJC/178/2025 que regula el resto de tipos) | — |

**Coste empresa por hora — cálculo orientativo (Oficial 1ª de oficio, convenio Madrid 2026, 1.736 h efectivas/año):**
Salario bruto anual 25.103,23 € + cotizaciones empresa (23,60+5,50+0,20+0,60+6,70+0,67 = 37,27% sobre bases de cotización, aplicado de forma simplificada sobre el bruto) ≈ 25.103,23 × 1,3727 ≈ **34.454 €/año** de coste empresa ⇒ **≈ 19,8 €/hora efectiva** (34.454 / 1.736 h). *Este cálculo es una elaboración propia a partir de los datos oficiales de la tabla; no proviene directamente de una fuente única, y simplifica la base de cotización asimilándola al salario bruto (en la práctica la base de cotización tiene topes mínimos/máximos y conceptos excluidos que no se han modelado aquí).*

Tabla completa de cotizaciones en `limpio/cotizaciones_seguridad_social_2025.csv`.

---

## 4. Estructura de costes de una promoción (gastos generales, beneficio industrial, honorarios, seguridad y salud, seguros)

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Gastos generales de estructura (sobre PEM) | 13 – 17 | % | vigente desde 2001 | Ministerio de Hacienda | RD 1098/2001, art. 131 (Reglamento General LCAP) | https://www.boe.es/buscar/pdf/2001/BOE-A-2001-19995-consolidado.pdf | boe_rd_1098_2001_consolidado.pdf | Lo fija cada departamento ministerial; en obras del Estado (Fomento) se aplica habitualmente el 13% (Orden FOM/1824/2013) |
| Beneficio industrial del contratista (sobre PEM) | 6 | % | vigente desde 2001 | ídem | ídem art. 131 | ídem | ídem | Presupuesto Base de Licitación (PBL) = PEM × 1,19 (13%+6%) en la práctica habitual |
| Gastos generales + beneficio industrial aplicados por IVE (Com. Valenciana) | 13% + 6% = 19% sobre PEM | % | 2024 | IVE | Informe costes construcción y VPO, pág. 5 | https://descargas.five.es/archivos/Blog/Articulos/Informe_Costes_construccion_VPO.pdf | ive_informe_costes_construccion_vpo_2024.pdf | Confirma exactamente los mismos porcentajes que el RD 1098/2001 |
| Honorarios técnicos (proyecto + dirección de obra), % orientativo en licitaciones públicas | Sin tarifa oficial vigente desde 1997 (STC 116/1997 declaró inconstitucionales los baremos obligatorios de honorarios) | % | — | — | — | — | — | **GAP declarado expresamente**: no existe un baremo o porcentaje oficial de honorarios de arquitecto/aparejador. Los pliegos de licitación pública fijan un presupuesto máximo de licitación para la redacción de proyecto + dirección de obra caso por caso (p. ej., el ejemplo de Casa47/Sevilla: 737.660 € para 2 edificios de 146 viviendas, proyecto básico+ejecución, sin desglose de %); no se ha podido derivar un porcentaje medio fiable en el tiempo disponible |
| Seguridad y salud (estudio y coordinación), % típico | Sin porcentaje oficial fijado por ley | % | — | RD 1627/1997 (obligatoriedad, no cuantía) | — | https://www.boe.es/buscar/act.php?id=BOE-A-1997-22614 (no descargado) | — | El RD 1627/1997 obliga a incluir presupuesto de seguridad y salud pero no fija %; en la práctica de licitaciones suele rondar 1-2% del PEM, pero esto es una práctica de mercado, no un dato oficial normativo — se declara como hueco |
| Control de calidad, % típico | Sin porcentaje oficial fijado por ley | % | — | — | — | — | — | Mismo caso que seguridad y salud: no hay porcentaje legal fijado; hueco declarado |
| Seguro decenal de daños (LOE) | Obligatorio, sin tipo de prima oficial fijado | — | vigente desde 2000 | BOE | Ley 38/1999, de 5 de noviembre, de Ordenación de la Edificación (LOE), art. 19 | https://www.boe.es/buscar/pdf/1999/BOE-A-1999-21567-consolidado.pdf | boe_ley_38_1999_loe_consolidado.pdf | La LOE obliga a suscribir el seguro decenal para daños materiales por vicios estructurales, pero la prima la fija el mercado asegurador libremente; no existe tipo oficial — hueco declarado |

---

## 5. Impuestos y tasas aplicables a obra nueva

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| IVA vivienda nueva, tipo general | 10 | % | vigente | Agencia Tributaria / Ley 37/1992 IVA | Ley del IVA, art. 91.Uno.1.7º | https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-inmobiliarias/compro-vivienda-tengo-que-pagar-itp.html | — (consultado en sede electrónica, no PDF) | Incluye VPO de régimen general |
| IVA VPO de régimen especial / promoción pública | 4 | % | vigente | ídem | Ley del IVA, art. 91.Dos.1.6º | ídem | — | Solo cuando la vivienda está calificada como régimen especial o promoción pública, y la entrega la hace el promotor directamente |
| ICIO, tipo máximo legal | 4 | % | vigente desde 2004 | BOE | RDL 2/2004 (TRLRHL), art. 102.3 | https://www.boe.es/buscar/pdf/2004/BOE-A-2004-4214-consolidado.pdf | boe_rdl_2_2004_trlrhl_consolidado.pdf | Base imponible = coste de ejecución material, excluye IVA, honorarios y beneficio empresarial (art. 102.1) |
| ICIO, tipo vigente Madrid capital | 3,75 | % | desde 01-01-2025 | Ayuntamiento de Madrid | Ordenanza Fiscal 7/2023 modificada por Ordenanza 12/2025 | https://transparencia.madrid.es/.../Ordenanza-12-2025... | — (no descargado PDF; confirmado por búsqueda oficial) | Rebajado desde el 4% anterior |
| AJD, tipo general Madrid (Comunidad de) | 0,75 | % | 2025 | Comunidad de Madrid | Texto refundido ITPAJD (RDLeg 1/1993) y normativa autonómica de Madrid | https://www.comunidad.madrid/atencion-contribuyente/actos-juridicos-documentados | — | 0,2% para VPO ≤90 m² útiles; 1,5% en renuncia a exención de IVA |
| AJD, tipo general Cataluña | 1,50 (3,50 en renuncia a exención IVA) | % | desde 27-jun-2025 | Generalitat de Catalunya | Decret llei 5/2025, de 25 de marzo | https://atc.gencat.cat/es/tributs/itpajd/ajd/ | — | Subida desde el 2,5%/2% anterior |
| AJD, tipo general Comunitat Valenciana | 1,40 | % | desde 01-06-2026 | Generalitat Valenciana | Llei 5/2025 (ATV) | https://atv.gva.es/es/actos-juridicos-documentados | — | Bajada desde el 1,5% |
| AJD, tipo general Andalucía | 1,20 | % | desde 2021 | Junta de Andalucía | Ley 5/2021, de 20 de octubre, de Tributos Cedidos | https://www.juntadeandalucia.es/organismos/economiahaciendayfondoseuropeos/.../medidasAJD.html | — | 0,3% jóvenes <35 años (vivienda ≤150.000€); 0,1% familia numerosa/discapacidad |
| AJD, tipo general Aragón | 1,20 (1,50 en renuncia a exención IVA) | % | 2025 | Gobierno de Aragón | Normativa ITP-AJD Aragón | https://www.aragon.es/administracion-tributaria-de-aragon/impuestos/transmisiones-patrimoniales-y-actos-juridicos-documentados | — | |
| Aranceles notariales, tramo hasta 6.010,12 € | 90,151816 | € fijos | vigente desde 1989 (importes en euros) | BOE | RD 1426/1989, Anexo I, Número 2 | https://www.boe.es/buscar/pdf/1989/BOE-A-1989-28111-consolidado.pdf | boe_rd_1426_1989_notarios_consolidado.pdf | Rebaja adicional del 5% sobre el arancel resultante en todos los casos |
| Aranceles notariales, tramo 150.253,04-601.012,10 € | 0,5 | por mil | ídem | ídem | ídem | ídem | ídem | Tramo típico de una compraventa de vivienda de precio medio-alto |
| Aranceles registradores, tramo hasta 6.010,12 € | 24,040484 | € fijos | vigente desde 1989 | BOE | RD 1427/1989, Anexo I, Número 2 | https://www.boe.es/buscar/pdf/1989/BOE-A-1989-28112-consolidado.pdf | boe_rd_1427_1989_registradores_consolidado.pdf | Arancel global topado entre 24,04 € y 2.181,67 € |
| Aranceles registradores, tramo 150.253,04-601.012,10 € | 0,30 | por mil | ídem | ídem | ídem | ídem | ídem | |
| Plusvalía municipal (IIVTNU) | Variable por municipio; método objetivo (valor catastral × coeficiente por años) o real (plusvalía real), lo que sea menor | — | vigente desde reforma 2021 (STC 182/2021 y RDL 26/2021) | BOE | RDL 2/2004 (TRLRHL) arts. 104-110, redacción RDL 26/2021 | https://www.boe.es/buscar/pdf/2004/BOE-A-2004-4214-consolidado.pdf | boe_rdl_2_2004_trlrhl_consolidado.pdf | No aplica a primera transmisión de obra nueva (no hay incremento de valor del suelo previo transmitido por el promotor); relevante solo en transmisiones posteriores — se cita por completitud pero no es un coste del promotor en obra nueva |

Tablas completas de aranceles y AJD en `limpio/aranceles_notarios_registradores_1989.csv` y `limpio/ajd_tipos_ccaa_obra_nueva_2025_2026.csv`.

---

## 6. Suelo y urbanización

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Valor de repercusión de suelo, jerarquía máxima (R00) | 5.554 | €/m² edificable | 2025 | Dirección General del Catastro | Circular 01.04/2025/P | https://www.catastro.hacienda.gob.es/documentos/01042025_P.pdf | catastro_circular_01042025_modulos.pdf | Aplicable en ponencias de valores de zonas de máximo valor (grandes capitales, ej. Madrid/Barcelona centro) |
| Valor de repercusión de suelo, jerarquía mínima (R34) | 8 | €/m² edificable | 2025 | ídem | ídem | ídem | ídem | Zonas rurales/periferia de escaso valor |
| Coste de urbanización por m² de suelo urbanizado | No localizado dato agregado oficial nacional | €/m² | — | — | — | — | — | **GAP declarado**: no se ha encontrado en el tiempo disponible un estudio o estadística oficial del MIVAU con el coste medio de urbanización por m². Se recomienda buscar específicamente en proyectos de urbanización licitados de SEPES/Casa47 (que sí gestionan suelo finalista) o en memorias de las Juntas de Compensación de actuaciones públicas recientes (p.ej. Los Berrocales/Los Ahijones, Madrid), no completado aquí |
| Suelo de las actuaciones "Los Ahijones" y "Los Berrocales" (Madrid) | Identificadas como actuaciones de referencia | — | 2025-2026 | Ayuntamiento de Madrid / EMVS | Plan Suma Vivienda | https://www.emvs.es/Vivienda/Suma/Documents/Descripci%C3%B3n-Plan-Suma-Vivienda.pdf | — | No descargado ni tabulado el coste de urbanización específico por limitación de tiempo |

---

## 7. Vivienda protegida (VPO) — precio máximo de venta como referencia de coste "asequible" regulado

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Precio máximo de venta VPO, Comunitat Valenciana, régimen general | 2.200 | €/m² útil | Decreto 68/2023, vigente | Generalitat Valenciana | Decreto 68/2023, de 12 de mayo, del Consell | citado en ive_informe_costes_construccion_vpo_2024.pdf | ive_informe_costes_construccion_vpo_2024.pdf | El IVE señala que a este precio la promoción privada solo es viable en ~40 municipios de la Comunitat |
| Precio de venta recomendado para viabilidad (no normativo) | 2.400 | €/m² útil | análisis IVE 2024 | IVE | ídem | ídem | ídem | Es una recomendación técnica del informe, no un precio legal vigente |
| Precio máximo VPO Andalucía, municipios grupo A/1, régimen concertado/tasado | 2.523 | €/m² útil | 2024 (dato recogido por IVE) | Junta de Andalucía (citado por IVE) | Tabla comparativa CCAA, informe IVE | ídem | ídem | Ver tabla completa en `limpio/vpo_precios_maximos_venta_ccaa.csv` |
| Precio máximo VPO Cataluña, zona A1/A2 | 3.002 | €/m² útil | 2024 (dato recogido por IVE) | Generalitat de Catalunya (citado por IVE) | ídem | ídem | ídem | El más alto de España según el informe IVE |
| Precio máximo VPO Madrid (Comunidad de) | 2.820 | €/m² útil | 2024 (dato recogido por IVE) | Comunidad de Madrid (citado por IVE) | ídem | ídem | ídem | Segundo más alto, según IVE; **no se ha verificado de forma independiente en fuente primaria madrileña por límite de tiempo** — dato de segunda mano (IVE cita a Madrid) |
| Precio máximo VPO Aragón, grupo A | 910 – 1.054 | €/m² útil | 2024 (dato recogido por IVE) | Gobierno de Aragón (citado por IVE) | ídem | ídem | ídem | Uno de los más bajos junto a Castilla-La Mancha |
| Módulo Básico de Edificación (MBE) Comunitat Valenciana | Base del cálculo del PEM=888€/m² (jun-2024); una actualización posterior citada en búsqueda (no verificada documentalmente) sitúa el MBE en 685 €/m² tras una subida del 13% | €/m² | jun-2024 y posterior | IVE | Informe costes construcción y VPO | https://descargas.five.es/archivos/Blog/Articulos/Informe_Costes_construccion_VPO.pdf | ive_informe_costes_construccion_vpo_2024.pdf | La cifra de 685 €/m² procede de un resultado de búsqueda no verificado documentalmente (artículo de innovandoenlaconstruccion.com que cita al IVE); no se ha confirmado en fuente oficial primaria — tratar con cautela |

Nota: no se ha localizado en el tiempo disponible el "módulo básico estatal (MBE)" del Plan Estatal de Vivienda vigente a nivel nacional (el RD 2066/2008 y sucesivos han ido siendo sustituidos y el marco actual delega mayoritariamente en las CCAA); se declara como hueco parcial.

---

## 8. Financiación

| variable | valor | unidad | fecha ref | organismo | documento/tabla | URL exacta | archivo local | notas |
|---|---|---|---|---|---|---|---|---|
| Tipo de interés TAE, crédito a hogares para adquisición de vivienda (operaciones nuevas) | 2,94 | % | jul-2026 | Banco de España | Boletín Estadístico, tabla 19.6 | https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a1906.pdf | bde_a1906_tipos_interes_operaciones_nuevas.pdf | Dato mensual más reciente publicado (P = provisional) |
| Tipo de interés TAE, crédito a hogares para adquisición de vivienda | 2,64 | % | dic-2025 | Banco de España | ídem | ídem | ídem | |
| Rendimiento deuda pública española, tramo "a diez años" (mercado secundario) | 3,64 | % | ago-2026 | Banco de España | Boletín Estadístico, tabla 22.7 | https://www.bde.es/webbe/es/estadisticas/compartido/datos/pdf/a2207.pdf | bde_a2207_mercados_secundarios_deuda.pdf | La tabla agrupa emisiones "a diez, quince, veinte" años en columnas separadas; el valor citado corresponde a la columna "a diez años" |
| Rendimiento deuda pública española, tramo "a diez años" | 3,27 | % | dic-2025 | Banco de España | ídem | ídem | ídem | |
| Estadísticas de la deuda del Estado (documento completo) | Descargado, no tabulado en detalle | — | 2026 | Tesoro Público | Estadísticas de la Deuda del Estado | https://www.tesoro.es/sites/default/files/estadisticas/Estadisticas_ES.pdf | tesoro_estadisticas_deuda_estado.pdf | Documento de 2,8 MB con series completas; no se ha extraído tabla específica por límite de tiempo — disponible para consulta posterior |

---

## Huecos y advertencias

1. **Licitaciones públicas de vivienda con desglose PEM/PBL en €/m²**: es el hueco más importante del encargo. Se pidieron 3-6 ejemplos trazables (EMVS, Casa47/SEPES, Agencia de Vivienda Social de Madrid, IMPSOL Barcelona) con PEM y PBL en €/m² y €/vivienda. Solo se ha conseguido un dato de coste de construcción con desglose completo y trazable a fuente pública (informe técnico del IVE, Comunitat Valenciana, que usa el mismo módulo de las licitaciones VPO valencianas). Los expedientes de Madrid (EMVS, Agencia de Vivienda Social) y de Casa47 están identificados con URL pero no se ha completado la descarga y extracción del pliego/memoria con el desglose económico. **Recomendación**: sesión de trabajo dedicada a contrataciondelestado.es y a contratos-publicos.comunidad.madrid con búsqueda por CPV de construcción de vivienda y filtro de adjudicación 2024-2026.

2. **Base de Precios de la Construcción de la Comunidad de Madrid (BPCM)**: no es descargable como fichero estático; se sirve mediante un visor interactivo (gestiona.comunidad.madrid/bdco_inter) que requiere sesión de usuario. No se ha podido obtener el coste de referencia €/m² de vivienda plurifamiliar de Madrid desde esta base oficial. Se ha suplido parcialmente con datos de Andalucía (BCCA) y Comunitat Valenciana (IVE).

3. **Honorarios profesionales de arquitecto y aparejador**: confirmado que no existe baremo oficial vigente desde la STC 116/1997 (que declaró inconstitucionales los baremos obligatorios de honorarios de los colegios profesionales). No se ha podido derivar, en el tiempo disponible, un porcentaje medio fiable a partir de licitaciones públicas de redacción de proyecto y dirección de obra (solo se dispone de un ejemplo en valor absoluto: 737.660 € para 2 edificios/146 viviendas en Sevilla, Casa47, sin desglose porcentual sobre PEM).

4. **Seguridad y salud, control de calidad y seguro decenal**: no existen porcentajes oficiales fijados por ley para estos tres conceptos (solo la obligatoriedad normativa: RD 1627/1997 para seguridad y salud, LOE para el seguro decenal). Se declara expresamente este hueco en vez de inventar un porcentaje "de mercado" no verificable oficialmente.

5. **Coste de urbanización por m²**: no se ha localizado una estadística o estudio oficial agregado del MIVAU ni de otra administración con este dato a nivel nacional o de las 6 ciudades objetivo.

6. **Módulo básico estatal de VPO**: el marco estatal (RD 2066/2008 y Plan Estatal de Vivienda) ha ido delegando en las CCAA la fijación de precios máximos; no se ha encontrado un módulo básico estatal único vigente y aplicable de forma homogénea. Los precios máximos de venta recabados (sección 7) proceden todos, salvo Comunitat Valenciana (fuente primaria IVE), de una tabla comparativa de segunda mano incluida en el informe del IVE — se recomienda verificar Madrid, Cataluña, Andalucía y Aragón contra su normativa autonómica primaria en un trabajo posterior.

7. **INE — Índice de Precios de Vivienda 2T 2026**: solo se descargó el Excel de tablas del 1T 2026; el dato de variación interanual del 2T 2026 (+12,2%) se tomó de la nota de prensa vía búsqueda, sin descargar el Excel correspondiente (gap menor, fácilmente subsanable).

8. **Índices de coste de mano de obra y de materiales del INE/MIVAU**: no se han descargado series propias del INE (Índice de Costes del Sector de la Construcción) para actualizar precios de forma sistemática; se ha usado como proxy la fórmula de revisión de precios (RD 1359/2011) citada indirectamente por el informe del IVE.

9. **Catastro — circular 2026 y tablas MBC por municipio**: se descargó la Circular 02.04/2026/P pero no se tabularon sus 35 escalones actualizados por límite de tiempo (sí se tabularon los de 2025). El MBC específico de cada uno de los 6 municipios objetivo (Madrid, Barcelona, Valencia, Sevilla, Zaragoza, Málaga) no se ha extraído individualmente porque depende de la ponencia de valores vigente en cada municipio (documento distinto por municipio, no centralizado en la circular general).

10. **Cálculo de "coste empresa por hora"**: el valor de 19,8 €/h presentado en la sección 3 es una elaboración propia (combinando la tabla salarial oficial de Madrid y los tipos de cotización oficiales), no un dato publicado directamente por ninguna fuente única. Se advierte explícitamente para que no se cite como si fuera un dato primario.

11. **AJD y ordenanzas fiscales municipales (ICIO)**: se han confirmado desde páginas oficiales de cada administración (Comunidad de Madrid, ATC Cataluña, ATV Valencia, Junta de Andalucía, Gobierno de Aragón, Ayuntamiento de Madrid) pero no se han descargado los textos legales completos (leyes/decretos-ley autonómicos) a `raw/`, solo se referencian sus páginas oficiales de consulta. Se recomienda descargar los DOGC/DOGV/BOJA/BOA de las leyes citadas si se necesita cita normativa exacta con artículo.

12. **Aranceles reales de una compraventa concreta**: se han transcrito los tramos oficiales del RD 1426/1989 y RD 1427/1989, pero no se ha calculado un ejemplo numérico completo para una vivienda de precio medio en cada una de las 6 ciudades (posible ampliación futura, es un cálculo directo a partir de las tablas ya incluidas).
