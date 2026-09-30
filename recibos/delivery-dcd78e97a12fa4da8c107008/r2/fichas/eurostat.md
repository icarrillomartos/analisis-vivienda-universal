---
id: "eurostat"
kind: "source"
revision: 2
updated: "2026-09-28T21:51:42Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://ec.europa.eu/eurostat (API de difusión) · GISCO (r2)"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto r2 sha256 6c15f2b325c0491d97d882368302c1e000eaf421ec76b9b59a31399f1f1c32f8"
links:
  - "src-vu-r2"
  - "src-vu-demografia"
  - "src-vu-fiscal"
  - "src-vu-digna"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/eurostat/r2/MANIFIESTO.sha256"
  sha256: "6c15f2b325c0491d97d882368302c1e000eaf421ec76b9b59a31399f1f1c32f8"
  bytes: 1658
---
# Eurostat · originales usados en el encargo de vivienda universal

## Identificación y alcance

gov_10a_main, gov_10dd_edpt1, gov_10a_exp (COFOG), gov_10a_taxag, cotizaciones, PIB, ilc_lvps08, yth_demo_030 y glosario de hacinamiento. Son 13 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-demografia](src-vu-demografia.md), [src-vu-fiscal](src-vu-fiscal.md), [src-vu-digna](src-vu-digna.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/eurostat/r2/<tema>/…` (la r1 se conserva intacta en `…/eurostat/r1/`), como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.

## Revisión r2 (28-09-2026)

Para la revisión del HTML se añadieron 3 archivos: gasto COFOG 2023 de España (gov_10a_exp: pensiones, sanidad, educación, defensa, protección social y total), superficie de España (reg_area3) y límites provinciales NUTS3 2024 de GISCO para el mapa, descargados el 28-09-2026 (API de difusión y GISCO). Están en `adjuntos/vivienda-universal/originales/eurostat/r2/r2/`, junto a una copia de todos los originales de la r1. Valores, URL exactas y límites: [src-vu-r2](src-vu-r2.md).
