---
id: "auditoria-datos"
kind: "artifact"
revision: 1
updated: "2026-09-28T20:49:16Z"
review: "current"
scopes:
  - "project:vivienda-universal"
  - "encargo:viabilidad-vivienda-universal-gratuita"
provenance:
  - source: "plan vivienda-gratuita v3"
    location: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/planes/vivienda-gratuita-v3.md"
    access: "full"
    accessed: "2026-09-28"
    version: "e39db97f825068401b8a402d0a309e1e4148a9095519b54ff3e498db4f89f2fe"
links:
  - id: "ine"
    relation: "derived_from"
  - id: "mivau"
    relation: "derived_from"
  - id: "catastro"
    relation: "derived_from"
  - id: "aeat"
    relation: "derived_from"
  - id: "igae"
    relation: "derived_from"
  - id: "bde"
    relation: "derived_from"
  - id: "boe"
    relation: "derived_from"
  - id: "eurostat"
    relation: "derived_from"
  - id: "hdb"
    relation: "derived_from"
  - id: "estudios"
    relation: "derived_from"
  - id: "html-vivienda-gratuita"
    relation: "related"
depends_on:
  - id: "ine"
  - id: "mivau"
  - id: "catastro"
  - id: "aeat"
  - id: "igae"
  - id: "bde"
  - id: "boe"
  - id: "eurostat"
  - id: "hdb"
  - id: "estudios"
storage:
  path: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/entregables/auditoria-datos/r1/MANIFIESTO.sha256"
  sha256: "7744000bd212b9ca85a6776cd00e2d51a0f96744e8cd885d09ccb329166dfe6e"
  bytes: 11421
---
# Carpeta de auditoría del HTML de vivienda gratuita · r1

## Producto conservado

Carpeta `entregables/auditoria-datos/r1/`: [LEEME](../entregables/auditoria-datos/r1/LEEME.md), fichas de datos, CSV limpios, scripts de limpieza, `hipotesis.json`, `modelo.py`, `build.py`, `plantilla.html` y resultados. El `MANIFIESTO.sha256` (archivo de `storage`) fija las huellas de sus 95 archivos. El HTML trae una copia idéntica en `html-vivienda-gratuita/r1/auditoria/`.

## Fuentes y dependencias

Derivada de las fuentes ine, mivau, catastro, aeat, igae, bde, boe, eurostat, hdb, estudios. Si cambia un dato de fuente o una hipótesis, hay que volver a ejecutar el modelo.

## Calidad y conservación

`modelo.py` se ejecuta desde esta copia y reproduce las cifras del HTML (5,47 billones en el teórico; 21,6 M de viviendas). Evaluada con P09 junto al HTML.

## Continuidad

Primera versión. Es la base para revisar hipótesis o actualizar datos en una r2.
