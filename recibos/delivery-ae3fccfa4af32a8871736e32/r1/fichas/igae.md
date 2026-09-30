---
id: "igae"
kind: "source"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.igae.pap.hacienda.gob.es · hacienda.gob.es · sanidad.gob.es · airef.es · tesoro.es"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto sha256 c7292b8f16c81b4258ecdd3cf6fc14f2a34db7c54fabef9e2693c11b8db88e78"
links:
  - "src-vu-fiscal"
  - "src-vu-costes"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/igae/r1/MANIFIESTO.sha256"
  sha256: "c7292b8f16c81b4258ecdd3cf6fc14f2a34db7c54fabef9e2693c11b8db88e78"
  bytes: 1227
---
# IGAE, Ministerio de Hacienda y otras fuentes de finanzas públicas (Sanidad, AIReF, Tesoro) · originales usados en el encargo de vivienda universal

## Identificación y alcance

Informe mensual de las AAPP, Haciendas Locales en Cifras 2023 (IBI), PGE 2023 (política 26 y Memoria de Beneficios Fiscales), gasto sanitario público, Plan Fiscal 2025-2028, estadísticas de la deuda del Estado e informes de la AIReF. Son 11 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-fiscal](src-vu-fiscal.md), [src-vu-costes](src-vu-costes.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/igae/r1/<tema>/…`, como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.
