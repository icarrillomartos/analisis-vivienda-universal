---
id: "hdb"
kind: "source"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
provenance:
  - source: "https://www.hdb.gov.sg · data.gov.sg · cpf.gov.sg · gov.sg"
    location: "descargas del 28-09-2026 listadas en el manifiesto"
    access: "full"
    accessed: "2026-09-28"
    version: "manifiesto sha256 b913b5ad654e92d8958b8d38c96d26e3fd53cd31876c5ed4272c7514f6319901"
links:
  - "src-vu-singapur"
depends_on: []
storage:
  path: "adjuntos/vivienda-universal/originales/hdb/r1/MANIFIESTO.sha256"
  sha256: "b913b5ad654e92d8958b8d38c96d26e3fd53cd31876c5ed4272c7514f6319901"
  bytes: 1494
---
# Singapur: HDB, SingStat, CPF Board y gov.sg · originales usados en el encargo de vivienda universal

## Identificación y alcance

HDB Key Statistics 2024/25, estados financieros FY2024 y FY2025, población, hogares, PIB, reventa, cotizaciones y asignación del CPF, informes anuales del CPF y política de integración étnica (EIP). Son 14 archivos originales, descargados el 28-09-2026 de sitios oficiales.

## Extracción

Los valores utilizados, con tabla, URL exacta y advertencias de cada uno, están en los dossiers temáticos: [src-vu-singapur](src-vu-singapur.md).

## Original y límites

Las copias durables están en `adjuntos/vivienda-universal/originales/hdb/r1/<tema>/…`, como clones APFS de los descargados en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`. Las huellas de cada archivo están en el manifiesto de `storage`. Las páginas oficiales que no se pudieron descargar (403, 404 o renderizado por JavaScript) figuran solo como URL en las fichas.
