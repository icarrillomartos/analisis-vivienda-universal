---
id: "html-vivienda-gratuita"
kind: "artifact"
revision: 1
updated: "2026-09-28T20:44:07Z"
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
  - id: "mem-vu-viabilidad-vivienda-gratuita"
    relation: "related"
  - id: "mem-vu-diagnostico-vivienda-espana"
    relation: "related"
  - id: "auditoria-datos"
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
  path: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/entregables/html-vivienda-gratuita/r1/index.html"
  sha256: "19e602794c9229e1b10e8d0c6e01fba634866dd303d8cb3392174015c91299bb"
  bytes: 97485
---
# ¿Vivienda gratis para todos? · HTML didáctico para directo · r1

## Producto conservado

[index.html](../entregables/html-vivienda-gratuita/r1/index.html) es un HTML autocontenido (fuentes de Google con fuentes de respaldo) de 20 láminas navegables con las flechas del teclado, con modo directo, gráficos SVG y un laboratorio de hipótesis interactivo. Lo acompaña la carpeta [auditoria/](../entregables/html-vivienda-gratuita/r1/auditoria/LEEME.md) con fichas, CSV limpios, scripts, `hipotesis.json`, `modelo.py`, `build.py`, `plantilla.html` y los resultados. El modelo se reproduce desde la copia de auditoría con las mismas cifras.

## Fuentes y dependencias

Se deriva de las fuentes ine, mivau, catastro, aeat, igae, bde, boe, eurostat, hdb, estudios (con sus dossiers temáticos src-vu-*) y de las hipótesis declaradas en `auditoria/modelo/hipotesis.json`. Si cambia un dato de una fuente o una hipótesis, hay que volver a ejecutar `modelo.py` y `build.py`.

## Calidad y conservación

Evaluado con P09 frente a los criterios del plan v3: cifras contrastadas con las fichas, etiquetas dato/evidencia/debate/opinión, preguntas de reflexión, contraste A frente a B y diagnóstico multidisciplinar. Revisión visual en claro y oscuro. El recibo de entrega queda en `recibos/`. La aceptación humana se registra aparte.

## Continuidad

Primera versión. Pendientes posibles: verificar la norma de Madrid contra la edición vigente de 2025, sustituir la hipótesis de honorarios por licitaciones reales, revalidar las cifras vivas (CIS, Eurostat, MIVAU) antes del directo y, si se pide, publicarlo como enlace.
