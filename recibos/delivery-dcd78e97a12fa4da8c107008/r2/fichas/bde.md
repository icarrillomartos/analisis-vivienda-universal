---
id: "bde"
kind: "source"
revision: 2
updated: "2026-09-28T21:51:42Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.bde.es · BCE data-api.ecb.europa.eu (r2)"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto r2 sha256 a1a7aa562198c18d72c32dd45c215a4cfe8e52eb9a5a19395ddf5403e5fa6bc6"
links:
  - "src-vu-r2"
  - "src-vu-evidencia"
  - "src-vu-fiscal"
  - "src-vu-costes"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/bde/r2/MANIFIESTO.sha256"
  sha256: "a1a7aa562198c18d72c32dd45c215a4cfe8e52eb9a5a19395ddf5403e5fa6bc6"
  bytes: 1107
---
# Banco de España · originales usados en el encargo de vivienda universal

## Identificación y alcance

Documento Ocasional 24/33, Informe Anual 2024, intervenciones de 2024 sobre el mercado de la vivienda, Informe Trimestral 2T 2026, tipos de interés (19.6) y rentabilidad de la deuda (22.7). Son 9 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-evidencia](src-vu-evidencia.md), [src-vu-fiscal](src-vu-fiscal.md), [src-vu-costes](src-vu-costes.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/bde/r2/<tema>/…` (la r1 se conserva intacta en `…/bde/r1/`), como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.

## Revisión r2 (28-09-2026)

Para la revisión del HTML se añadió 1 archivo del Banco Central Europeo (SDW, serie EXR M.SGD.EUR.SP00.A): tipo de cambio mensual EUR/SGD desde 2024, descargado el 28-09-2026 (API de datos del BCE). Están en `adjuntos/vivienda-universal/originales/bde/r2/r2/`, junto a una copia de todos los originales de la r1. Valores, URL exactas y límites: [src-vu-r2](src-vu-r2.md).
