# Carpeta de auditoría · ¿Vivienda gratis para todos? (r1, 28-09-2026)

Con esta carpeta cualquiera puede repetir las cuentas del HTML (`index.html`, en `entregables/html-vivienda-gratuita/r1/` del encargo).

## Contenido

| Carpeta | Qué hay |
|---|---|
| `fichas/` | Una ficha por frente de datos (demografía, parque, costes, vivienda digna, fiscalidad, Singapur, evidencia). Para cada dato: valor, fecha, organismo, tabla, URL exacta y advertencias. |
| `datos/<tema>/limpio/` | Tablas limpias (CSV) que usa el modelo. |
| `datos/<tema>/scripts/` | Scripts de descarga y limpieza de cada frente. |
| `datos/costes/raw/` | Único original que el modelo lee directamente: la serie de valor tasado del MIVAU. |
| `modelo/hipotesis.json` | Todas las hipótesis. Cada una indica si es un dato oficial, un cálculo propio o una hipótesis con rango. |
| `modelo/modelo.py` | Cálculo completo por provincias y escenarios. Genera `modelo/salida/`. |
| `modelo/build.py` + `plantilla.html` | Generan el HTML a partir de los resultados. |

Los originales descargados (unos 190 MB: PDF, XLS y JSON de INE, MIVAU, AEAT, Eurostat, BdE, BOE, HDB…) se conservan en la bóveda, en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`, cada uno con un `MANIFIESTO.sha256`.

## Reproducir

```bash
python3 -m venv venv && ./venv/bin/pip install pandas xlrd openpyxl
cd modelo && ../venv/bin/python modelo.py && ../venv/bin/python build.py
```

Para cambiar una hipótesis, edita `hipotesis.json` y vuelve a ejecutar. El HTML también trae un laboratorio interactivo para probar las principales sin programar.

## Límites conocidos

- Sin dato oficial: honorarios técnicos, urbanización, seguridad y salud, seguro decenal y ratio útil/construida. Se tratan como hipótesis con rango.
- El coste de obra (PEM) procede del IVE (Generalitat Valenciana, 2024). Se aplica a toda España con una actualización del 7 %.
- El INE no publica viviendas por tramos de superficie inferiores a 75 m², así que no se descuentan las que miden menos que el módulo.
- Los adultos por nacionalidad y provincia, y los de las grandes ciudades, son estimaciones documentadas en la ficha de demografía.
- El valor de un punto de IVA es una estimación propia.
- No se simulan efectos de segunda ronda: subida de costes por la demanda, cambios de comportamiento ante los impuestos.
