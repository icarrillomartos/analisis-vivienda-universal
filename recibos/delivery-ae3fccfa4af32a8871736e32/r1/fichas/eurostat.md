---
id: "eurostat"
kind: "source"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://ec.europa.eu/eurostat (API de difusión)"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto sha256 326d49a260fcc8df40d02dfafedb0fbc03459d26d7aebd2967b92174e796a8ed"
links:
  - "src-vu-demografia"
  - "src-vu-fiscal"
  - "src-vu-digna"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/eurostat/r1/MANIFIESTO.sha256"
  sha256: "326d49a260fcc8df40d02dfafedb0fbc03459d26d7aebd2967b92174e796a8ed"
  bytes: 1367
---
# Eurostat · originales usados en el encargo de vivienda universal

## Identificación y alcance

gov_10a_main, gov_10dd_edpt1, gov_10a_exp (COFOG), gov_10a_taxag, cotizaciones, PIB, ilc_lvps08, yth_demo_030 y glosario de hacinamiento. Son 13 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-demografia](src-vu-demografia.md), [src-vu-fiscal](src-vu-fiscal.md), [src-vu-digna](src-vu-digna.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/eurostat/r1/<tema>/…`, como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.
