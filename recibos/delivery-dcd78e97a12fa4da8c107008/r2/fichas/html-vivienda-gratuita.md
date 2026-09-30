---
id: "html-vivienda-gratuita"
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
  - id: "mem-vu-viabilidad-vivienda-gratuita"
    relation: "related"
  - id: "mem-vu-diagnostico-vivienda-espana"
    relation: "related"
  - id: "auditoria-datos"
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
  path: "proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/entregables/html-vivienda-gratuita/r2/index.html"
  sha256: "482c60231c67ab8f43805c2c415c722d6a37c92ea56778a6c8445c8f9f33d771"
  bytes: 171852
---
# ¿Vivienda gratis para todos? · HTML didáctico para directo · r2

## Producto conservado

[index.html](../entregables/html-vivienda-gratuita/r2/index.html) es un HTML autocontenido (fuentes de Google con fuentes de respaldo) de 22 láminas, **siempre en tema oscuro**, navegable con las flechas del teclado, con modo directo, gráficos SVG, mapa provincial interactivo y laboratorio de hipótesis. Lo acompaña la carpeta [auditoria/](../entregables/html-vivienda-gratuita/r2/auditoria/LEEME.md) con fichas (incluida `r2.md`), CSV limpios, scripts, `hipotesis.json`, `modelo.py`, `build.py`, `plantilla.html` y los resultados. El modelo se reproduce desde la copia de auditoría con resultados idénticos byte a byte. La r1 sigue conservada en `entregables/html-vivienda-gratuita/r1/`.

## Cambios de la r2

1. **¿Cuánto pagaría cada uno?** Calendario 2027-2076 en dos fases. Fase 1 (30 años): 251.000 M€/año (14,8 % del PIB), 5.470 € por adulto y año (456 €/mes) o 10.460 € por declarante. Fase 2: 45.000 M€/año (2,7 %), 970 € por adulto y año (80 €/mes). Flujo anual: +551.000 que cumplen 18, +472.000 de saldo migratorio adulto, −436.118 defunciones.
2. **Mapa provincial** (GISCO NUTS3 2024) con teórico, plausible y «Toda España». No cabrían en su provincia 14,06 M de personas (teórico) o 1,59 M de hogares (plausible). Madrid necesita el 743 % de su suelo previsto: 2,84 M sin sitio.
3. **Comparativas.** El coste inicial se paga una vez y se expresa en años de pensiones, sanidad, educación y defensa (COFOG 2023). El anual se compara con esas partidas.
4. **Singapur frente a España.** Población, superficie, densidad, PIB per cápita PPA (×2,7), renta del hogar, años de renta por vivienda (BTO 4-room ≈ 3,7 frente a ≈ 4,5 en España) y vivienda pública nueva por 1.000 habitantes (3,2 frente a 2,0), con la pausa «¿Se puede extrapolar?».
5. **Tema oscuro fijo**, a petición de la persona: `data-theme="dark"` en `<html>` y `color-scheme: dark`.

## Fuentes y dependencias

Se deriva de las fuentes ine, mivau, catastro, aeat, igae, bde, boe, eurostat, hdb y estudios (con sus dossiers src-vu-*, incluido [src-vu-r2](../../../../../memoria/fuentes/src-vu-r2.md)) y de las hipótesis de `auditoria/modelo/hipotesis.json`. Si cambia un dato o una hipótesis, hay que volver a ejecutar `modelo.py` y `build.py`.

## Calidad y conservación

Evaluado con P09 frente a los criterios del plan v3 y los cuatro puntos del feedback. Revisión visual con el sistema en modo claro (la página se ve oscura), mapa, calendario, comparativas, tabla de Singapur y laboratorio; sin desbordamiento a 375 px y consola sin errores. El recibo de entrega queda en `recibos/`. La aceptación humana se registra aparte.

## Continuidad

Segunda versión. Pendientes posibles: verificar la norma de Madrid contra la edición vigente de 2025, sustituir la hipótesis de honorarios por licitaciones reales, revalidar las cifras vivas antes del directo y, si se pide, publicarlo como enlace.
