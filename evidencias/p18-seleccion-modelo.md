# Selección de modelos · viabilidad-vivienda-universal-gratuita

## Bloque y funciones

- **Bloque sustancial:** recogida y descarga de datasets oficiales en 7 frentes, cálculo reproducible y producción del HTML. Supera el umbral porque produce archivos, investiga fuera y consume mucho contexto.
- **Dirección:** solicitado Opus 5.5 · observado `claude-opus-5-5` · Anthropic · Claude Code Desktop (macOS) · esfuerzo según sesión.
- **Ejecución (recogida de datos):** solicitado Sonnet 5 (`model: sonnet` en el tool Agent) · observado: el modelo que declare cada subagente · Anthropic · Claude Code.
- **Revisión:** Opus 5.5 (dirección). Revisa cada ficha de datos contra su fuente antes de usarla en los cálculos.

## Decisión

- **Criterio de elección:** la búsqueda y descarga de tablas oficiales es mecánica y se hace en paralelo, así que Sonnet basta y cuesta menos. El modelo, los cálculos, la interpretación económica y el relato quedan en Opus.
- **Solvencia esperada:** cada ficha trae valor, unidad, fecha, organismo, tabla, URL y archivo local.
- **Escalado:** si una ficha llega incompleta, con una fuente no oficial o con contradicciones, Opus la rehace o la verifica directamente.
- **El cliente permite selección explícita:** sí; el tool Agent admite el parámetro `model`.
- **Herencia accidental descartada:** el modelo se pasa de forma explícita en cada llamada.

## Vinculación con el control

- Plan `vivienda-gratuita` v3 · digest `e39db97f825068401b8a402d0a309e1e4148a9095519b54ff3e498db4f89f2fe`.
