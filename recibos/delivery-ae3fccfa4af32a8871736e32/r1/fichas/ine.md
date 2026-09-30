---
id: "ine"
kind: "source"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.ine.es · API Tempus (servicios.ine.es/wstempus) e INEbase"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto sha256 af882c1292f89fe54b38efd7470f526673feeecd5e0050b48eadb9ccae2bde6c"
links:
  - "src-vu-demografia"
  - "src-vu-parque"
  - "src-vu-fiscal"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/ine/r1/MANIFIESTO.sha256"
  sha256: "af882c1292f89fe54b38efd7470f526673feeecd5e0050b48eadb9ccae2bde6c"
  bytes: 5987
---
# Instituto Nacional de Estadística (INE) · originales usados en el encargo de vivienda universal

## Identificación y alcance

ECP (1-7-2026), ECP-Hogares, Proyecciones, ECV 2025, Padrón 2025, Censo 2021 (viviendas, superficie, conservación), EPA, ETDP, IPV y CNTR (PIB). Son 49 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-demografia](src-vu-demografia.md), [src-vu-parque](src-vu-parque.md), [src-vu-fiscal](src-vu-fiscal.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/ine/r1/<tema>/…`, como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.
