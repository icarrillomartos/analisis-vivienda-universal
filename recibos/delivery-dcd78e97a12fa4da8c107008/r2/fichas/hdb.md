---
id: "hdb"
kind: "source"
revision: 2
updated: "2026-09-28T21:51:42Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.hdb.gov.sg · data.gov.sg · cpf.gov.sg · gov.sg"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto r2 sha256 b92321049dbde10da2271990bf23269f67a7262783e65e902869db0718760f6c"
links:
  - "src-vu-r2"
  - "src-vu-singapur"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/hdb/r2/MANIFIESTO.sha256"
  sha256: "b92321049dbde10da2271990bf23269f67a7262783e65e902869db0718760f6c"
  bytes: 1718
---
# Singapur: HDB, SingStat, CPF Board y gov.sg · originales usados en el encargo de vivienda universal

## Identificación y alcance

HDB Key Statistics 2024/25, estados financieros FY2024 y FY2025, población, hogares, PIB, reventa, cotizaciones y asignación del CPF, informes anuales del CPF y política de integración étnica (EIP). Son 14 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-singapur](src-vu-singapur.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/hdb/r2/<tema>/…` (la r1 se conserva intacta en `…/hdb/r1/`), como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.

## Revisión r2 (28-09-2026)

Para la revisión del HTML se añadieron 2 archivos de SingStat vía data.gov.sg: superficie total de Singapur (2025) y renta mensual mediana y media de los hogares residentes (2024), descargados el 28-09-2026 (data.gov.sg). Están en `adjuntos/vivienda-universal/originales/hdb/r2/r2/`, junto a una copia de todos los originales de la r1. Valores, URL exactas y límites: [src-vu-r2](src-vu-r2.md).
