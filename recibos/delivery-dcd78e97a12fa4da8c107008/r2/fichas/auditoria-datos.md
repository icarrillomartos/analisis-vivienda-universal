---
id: "auditoria-datos"
kind: "artifact"
revision: 2
updated: "2026-09-28T21:54:28Z"
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
  - source: "feedback revise sobre la entrega r1 (delivery-ae3fccfa4af32a8871736e32) y petición de tema oscuro del 28-09-2026"
    location: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/preparacion/traspaso-r2.md"
    access: "full"
    accessed: "2026-09-28"
    version: "r2"
links:
  - id: "src-vu-r2"
    relation: "derived_from"
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
  - id: "src-vu-r2"
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
  path: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/entregables/auditoria-datos/r2/MANIFIESTO.sha256"
  sha256: "13bb31d1efa8f50ea4051b6a156292f225ae3f901900714f39255b086854bcf1"
  bytes: 11810
---
# Carpeta de auditoría del HTML de vivienda gratuita · r2

## Producto conservado

Carpeta `entregables/auditoria-datos/r2/`: [LEEME](../entregables/auditoria-datos/r2/LEEME.md), fichas de datos (incluida `r2.md`), CSV limpios, `datos/r2/` (constantes y mapa, con `procesar_r2.py`), scripts de limpieza, `hipotesis.json`, `modelo.py`, `build.py`, `plantilla.html` (tema oscuro) y resultados. El `MANIFIESTO.sha256` (archivo de `storage`) fija las huellas de sus 99 archivos. El HTML trae una copia idéntica en `html-vivienda-gratuita/r2/auditoria/`. La r1 sigue en `entregables/auditoria-datos/r1/`.

## Fuentes y dependencias

Derivada de las fuentes ine, mivau, catastro, aeat, igae, bde, boe, eurostat, hdb y estudios, más el dossier src-vu-r2. Si cambia un dato de fuente o una hipótesis, hay que volver a ejecutar el modelo.

## Calidad y conservación

`modelo.py` y `build.py` se ejecutan desde una copia de esta carpeta y reproducen byte a byte los resultados y el HTML r2 (teórico: 5,47 billones y 21,6 M de viviendas; fase 1: 251.000 M€ al año). Evaluada con P09 junto al HTML.

## Continuidad

Segunda versión. `anual_total` usa ahora el crecimiento neto medio de adultos a 30 años (≈ 180.000 al año), por eso el coste anual del teórico baja de ~298.000 M€ en la r1 a ~251.000 M€.
