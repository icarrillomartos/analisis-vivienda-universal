---
id: "ine"
kind: "source"
revision: 2
updated: "2026-09-28T21:51:42Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.ine.es · API Tempus (servicios.ine.es/wstempus) e INEbase"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto r2 sha256 44e54366260e61ce68eb4379f8f8535ab9a4ff5d4f16b77993a7aa5f08986ef3"
links:
  - "src-vu-r2"
  - "src-vu-demografia"
  - "src-vu-parque"
  - "src-vu-fiscal"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/ine/r2/MANIFIESTO.sha256"
  sha256: "44e54366260e61ce68eb4379f8f8535ab9a4ff5d4f16b77993a7aa5f08986ef3"
  bytes: 6741
---
# Instituto Nacional de Estadística (INE) · originales usados en el encargo de vivienda universal

## Identificación y alcance

ECP (1-7-2026), ECP-Hogares, Proyecciones, ECV 2025, Padrón 2025, Censo 2021 (viviendas, superficie, conservación), EPA, ETDP, IPV y CNTR (PIB). Son 49 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-demografia](src-vu-demografia.md), [src-vu-parque](src-vu-parque.md), [src-vu-fiscal](src-vu-fiscal.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/ine/r2/<tema>/…` (la r1 se conserva intacta en `…/ine/r1/`), como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.

## Revisión r2 (28-09-2026)

Para la revisión del HTML se añadieron 8 archivos: defunciones (tablas 6545 y 6561), saldos migratorios exteriores por edad (69759), renta neta media por hogar de la ECV 2025 (9949) con su nota de prensa, y los listados de operaciones y tablas usados para localizarlas, descargados el 28-09-2026 (Tempus). Están en `adjuntos/vivienda-universal/originales/ine/r2/r2/`, junto a una copia de todos los originales de la r1. Valores, URL exactas y límites: [src-vu-r2](src-vu-r2.md).
