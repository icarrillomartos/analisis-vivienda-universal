---
id: "catastro"
kind: "source"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.catastro.hacienda.gob.es"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto sha256 8f149ef7d1b00bf403aa6512326026065be8b98308b2b6176559b207ace6fb54"
links:
  - "src-vu-costes"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/catastro/r1/MANIFIESTO.sha256"
  sha256: "8f149ef7d1b00bf403aa6512326026065be8b98308b2b6176559b207ace6fb54"
  bytes: 224
---
# Dirección General del Catastro · originales usados en el encargo de vivienda universal

## Identificación y alcance

Circulares 01.04/2025/P y 02.04/2026/P de módulos (MBC/MBR). Son 2 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-costes](src-vu-costes.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/catastro/r1/<tema>/…`, como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.
