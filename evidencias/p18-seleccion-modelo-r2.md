# P18 · Selección de modelo y medios · r2 (28-09-2026)

- **Modelo observado:** Opus 5.5 (`claude-opus-5-5`), declarado por el entorno de esta sesión de Claude Code Desktop. No se usaron subagentes en esta sesión: el trabajo restante (empaquetado, conservación, revisión y sello) es secuencial y depende de huellas que cambian paso a paso.
- **Selección del cliente:** la sesión no expone al agente un cambio de modelo propio; la selección la hace la persona en la interfaz. Opus 5.5 es adecuado para revisión y control de calidad; no hacía falta un modelo menor.
- **Medios:** Python del venv de la sesión anterior (pandas, xlrd, openpyxl) para `modelo.py` y `build.py`; `cp -c` (clones APFS) para copias durables sin duplicar espacio; `shasum` para manifiestos; servidor HTTP local (127.0.0.1) y navegador integrado para la revisión visual con el sistema en modo claro, en escritorio y a 375 px.
- **Recuperación:** el fallo de control anterior se debió a un `cd` persistente fuera de la raíz. En esta sesión las órdenes se lanzan desde la raíz, con subshells para cambiar de carpeta.
- **Volumen:** originales nuevos de la r2 ≈ 3 MB (clones APFS); entregables r2 ≈ 7,9 MB. Muy por debajo del umbral de aviso de 500 MB.
