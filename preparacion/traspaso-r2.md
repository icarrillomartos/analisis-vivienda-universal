# Traspaso · revisión r2 del HTML de vivienda gratuita (28-09-2026)

## Situación

- **Encargo:** `vivienda-universal/viabilidad-vivienda-universal-gratuita`. Plan v3 aprobado (digest `e39db97f…`).
- **Fase:** F04 `revision_en_alcance`, tras el feedback «revise» sobre la entrega r1 (`delivery-ae3fccfa4af32a8871736e32`).
- **Bloqueo:** la sesión anterior dejó el directorio de trabajo del shell en `trabajo/modelo`. El hook de Second Brain solo acepta la invocación del controlador desde la raíz de la bóveda, así que no pudo situar el turno ni sellar.
- **Lección:** no hacer `cd` persistente a subcarpetas. Usar rutas absolutas o subshells `( cd … && … )`.

## Qué está hecho (r2, sin conservar todavía)

El HTML r2 está construido en `trabajo/modelo/salida/index.html` (~170 KB, 22 láminas). Se regenera con:

```
venv/bin/python modelo.py && venv/bin/python build.py
```

El venv está en el scratchpad o se recrea con pandas, xlrd y openpyxl.

Cambios de la r2 frente a la r1, uno por punto del feedback:

1. **Calendario de pago.** Nueva lámina «¿Cuánto pagaría cada uno?» con gráfico año a año de 2027 a 2076 y dos fases.
   - Fase 1, 30 años: 251.000 M€/año (14,8 % del PIB), es decir, 5.470 € por adulto y año (456 €/mes) o 10.460 € por declarante.
   - Fase 2, del año 31 en adelante: 45.000 M€/año (2,7 %), es decir, 970 € por adulto y año (80 €/mes).
   - Flujo con defunciones: +551.000 que cumplen 18, +472.000 de saldo migratorio adulto (INE 2024), −436.118 defunciones (INE 2024), ≈ +588.000 netos.
   - El crecimiento neto medio a 30 años según la proyección del INE es de unos 180.000 al año.
   - El coste anual del escenario (`anual_total`) usa ahora el crecimiento medio a 30 años, así que es igual a la media de la fase 1.
2. **Mapa provincial interactivo** (Eurostat GISCO NUTS3 2024).
   - Muestra teórico y plausible, y un botón «Toda España».
   - Por provincia: demanda, viviendas existentes, lo que falta, suelo SIU, % de suelo demandado sobre el disponible y personas sin sitio, con los datos brutos.
   - Personas sin sitio en su provincia: 14,06 M en el teórico y 1,59 M en el plausible.
3. **Comparativas.** En L07 se aclara que el coste inicial se paga una sola vez, con una tabla de «años de» pensiones, sanidad, educación y defensa (COFOG 2023). En «¿Quién paga?» hay un gráfico anual frente a pensiones (153.051 M€), sanidad (98.630), educación (62.532) y defensa (14.008), y una tabla de equivalencias por fase.
4. **Singapur frente a España.**
   - Población: 6,11 M frente a 49,8 M.
   - Superficie: 744 km² frente a 505.983 km².
   - Densidad: 8.210 hab./km² frente a 98.
   - PIB per cápita en PPA (Banco Mundial 2025): 163.354 $ frente a 59.868 $ (×2,7).
   - Renta del hogar: mediana SGD 9.541/mes (2024, incluido el CPF del empleador) frente a 38.994 €/año netos (ECV 2025).
   - Tipo de cambio del BCE (ago-2026): 1,48 SGD/EUR.
   - BTO 4-room ≈ 3,7 años de renta frente a 70 m² en España ≈ 4,5 años.
   - Viviendas públicas nuevas por cada 1.000 habitantes: 3,2 frente a 2,0.
   - Incluye la pausa «¿Se puede extrapolar?».

Datos nuevos en `trabajo/datos/r2/`: `raw/`, `limpio/r2_constantes.json`, `limpio/mapa_provincias.json` y `scripts/procesar_r2.py`.

## Qué falta para entregar la r2

1. Desde la raíz: `route` con `event: continue`, `project` y `encargo`.
2. Empaquetar:
   - `entregables/html-vivienda-gratuita/r2/index.html` más `auditoria/`: copia de la r1 actualizada con `modelo.py`, `build.py`, `plantilla.html`, `hipotesis.json`, `salida/*`, `datos/r2/{limpio,scripts}` y el resto de `limpio` que ya había.
   - `entregables/auditoria-datos/r2/` (clon), con un `MANIFIESTO.sha256` nuevo.
   - Comprobar que `modelo.py` se ejecuta desde la copia. Necesita `datos/demografia/limpio/proyeccion_poblacion_nacional_edadsimple_largoplazo.csv` y `datos/r2/limpio/*`.
3. Fuentes r2: crear `adjuntos/vivienda-universal/originales/<id>/r2/` (archivos de la r1 más los nuevos) con manifiesto, y subir las fichas a `revision: 2`.
   - `ine`: defunciones 6545, saldos 69759, ECV 9949.
   - `eurostat`: COFOG 2023, `reg_area3` y GISCO.
   - `hdb`: SingStat, superficie y renta.
   - `estudios`: Banco Mundial.
   - `bde`: BCE.
   - Añadir la ficha r2 a `trabajo/datos/r2/` y a la auditoría.
4. Fichas artifact a `revision: 2`, con `storage` en r2 y `links` tipados `derived_from`.
5. Actualizar `memoria/conocimientos/mem-vu-viabilidad-vivienda-gratuita.md` con las cifras de la r2 y reservar y liberar `memoria/indice.md`.
6. `start`/`finish` de P03, P08, P09, P10, P12 y P14 con los archivos r2.
7. Puertas `production_complete` y `quality_passed`.
8. `recibos/solicitud-r2.json` (schema 3), `seal` y `respond` delivery.

## Revisión visual ya hecha

Revisados en escritorio con tema oscuro: mapa (Madrid 743 %, 2,84 M sin sitio), calendario, gráfico comparativo, tabla de Singapur (se ajusta al ancho) y laboratorio (5.445 €/adulto frente a 5.470 en la página, diferencia por la aproximación nacional). Consola sin errores.

## Resolución (28-09-2026, sesión 4f8a012b)

Fallo de control recuperado desde la raíz. A petición de la persona, el HTML r2 queda fijo en tema oscuro (`data-theme="dark"`). Pasos 1-8 ejecutados: entregables r2, originales r2 con manifiesto, fichas source y artifact en revisión 2, dossier `src-vu-r2`, nota de conocimiento e índice, procesos acreditados en `evidencias/*-r2.json`, sello y entrega.
