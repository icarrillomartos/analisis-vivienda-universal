# Carpeta de auditoría · ¿Vivienda gratis para todos? (r2, 28-09-2026)

Con esta carpeta cualquiera puede repetir las cuentas del HTML (`index.html`, en `entregables/html-vivienda-gratuita/r2/` del encargo).

## Qué cambia respecto a la r1

- Nueva lámina «¿Cuánto pagaría cada uno?»: calendario de pago año a año (2027-2076) en dos fases, con flujos de altas y bajas de adultos (cumplen 18, saldo migratorio y defunciones).
- Mapa provincial interactivo (teórico, plausible y «Toda España») con la demanda, el parque, el suelo previsto y las personas que no cabrían en su provincia.
- Comparativas con el gasto en pensiones, sanidad, educación y defensa (COFOG 2023), tanto del coste inicial como del anual.
- Tabla Singapur frente a España (población, superficie, densidad, PIB per cápita PPA, renta del hogar, años de renta por vivienda, vivienda pública nueva).
- El HTML se muestra siempre en tema oscuro.
- `anual_total` usa ahora el crecimiento neto medio de adultos a 30 años, así que coincide con la media de la fase 1.

## Contenido

| Carpeta | Qué hay |
|---|---|
| `fichas/` | Una ficha por frente de datos (demografía, parque, costes, vivienda digna, fiscalidad, Singapur, evidencia) y `r2.md` con los datos añadidos en esta revisión. Para cada dato: valor, fecha, organismo, tabla, URL exacta y advertencias. |
| `datos/<tema>/limpio/` | Tablas limpias (CSV) que usa el modelo. |
| `datos/<tema>/scripts/` | Scripts de descarga y limpieza de cada frente. |
| `datos/r2/limpio/` | `r2_constantes.json` (flujos demográficos, COFOG, Singapur) y `mapa_provincias.json` (trazados SVG de las provincias). |
| `datos/r2/scripts/procesar_r2.py` | Genera los dos archivos anteriores a partir de los originales de la r2. |
| `datos/costes/raw/` | Único original que el modelo lee directamente: la serie de valor tasado del MIVAU. |
| `modelo/hipotesis.json` | Todas las hipótesis. Cada una indica si es un dato oficial, un cálculo propio o una hipótesis con rango. |
| `modelo/modelo.py` | Cálculo completo por provincias, escenarios y calendario de pago. Genera `modelo/salida/`. |
| `modelo/build.py` + `plantilla.html` | Generan el HTML a partir de los resultados. |

Los originales descargados (PDF, XLS, JSON y GeoJSON de INE, MIVAU, AEAT, Eurostat/GISCO, BdE/BCE, BOE, SingStat/HDB, Banco Mundial…) se conservan en la bóveda: en `adjuntos/vivienda-universal/originales/<fuente>/r2/` (con `MANIFIESTO.sha256`) y en `proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/<tema>/raw/`.

## Reproducir

```bash
python3 -m venv venv && ./venv/bin/pip install pandas xlrd openpyxl
cd modelo && ../venv/bin/python modelo.py && ../venv/bin/python build.py
```

Para cambiar una hipótesis, edita `hipotesis.json` y vuelve a ejecutar. El HTML también trae un laboratorio interactivo para probar las principales sin programar. `procesar_r2.py` solo hace falta si se vuelven a descargar los originales de la r2 en `datos/r2/raw/`.

## Límites conocidos

- Sin dato oficial: honorarios técnicos, urbanización, seguridad y salud, seguro decenal y ratio útil/construida. Se tratan como hipótesis con rango.
- El coste de obra (PEM) procede del IVE (Generalitat Valenciana, 2024). Se aplica a toda España con una actualización del 7 %.
- El INE no publica viviendas por tramos de superficie inferiores a 75 m², así que no se descuentan las que miden menos que el módulo.
- Los adultos por nacionalidad y provincia, y los de las grandes ciudades, son estimaciones documentadas en la ficha de demografía.
- El valor de un punto de IVA es una estimación propia.
- El saldo migratorio de 18-19 años se aproxima con el 40 % del grupo 15-19. La comparación de rentas con Singapur es orientativa (mediana bruta con CPF frente a media neta).
- El laboratorio del HTML usa una aproximación nacional: da 5.445 € por adulto y año frente a los 5.470 € del modelo completo.
- No se simulan efectos de segunda ronda: subida de costes por la demanda, cambios de comportamiento ante los impuestos.
