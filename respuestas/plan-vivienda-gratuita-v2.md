# Propuesta: ¿Es viable la vivienda gratuita universal en España? · versión 2

Cambios respecto a la v1:
- La unidad pasa a ser **cada adulto**, con derecho a vivir solo.
- Se añade un **estándar de «vivienda digna»**.
- La **compensación** a quien ya tiene vivienda pasa a ser el escenario principal.
- Se añaden **escenarios plausibles** y un tratamiento explícito de los dilemas que planteaste.

Lo que no cambia: sigue siendo un soporte visual y un guion para un directo de YouTube, contado de junior a junior y auditable por cualquiera.

## Qué te entregaré

Un **HTML autocontenido, visual y didáctico**, con pantallas para ir pasando en directo, gráficos y un **panel de hipótesis** con controles para cambiarlas en directo. Va acompañado de una **carpeta de auditoría** con los datasets oficiales, los scripts de limpieza y cálculo y una tabla de fuentes.

## La tesis que se pone a prueba (modelo A)

> «Todo residente en España, al cumplir 18 años, tiene derecho a una vivienda digna **para él solo**, gratuita de por vida y pagada con impuestos, como la sanidad pública. Quien ya tiene una vivienda en propiedad recibe una compensación equivalente, para que el trato sea igualitario».

- **Beneficiarios:** residentes, como en la sanidad. Se calcula también el escenario alternativo de solo nacionalidad española.
- **Unidad:** cada persona de 18 años o más. El Estado no puede obligar a nadie a casarse ni a compartir piso, así que el derecho es individual.

## Paso previo: definir «vivienda digna»

El artículo 47 de la Constitución habla de «vivienda digna», pero no la define. Propongo construir un **módulo de vivienda digna mínima** a partir de normas oficiales:
- los decretos autonómicos de habitabilidad;
- las normas urbanísticas de Madrid;
- el Código Técnico de la Edificación;
- los límites de la vivienda protegida (VPO).

Como referencia inicial, y **pendiente de verificar con esas normas**: un dormitorio, salón-comedor, cocina y baño, en torno a 40-50 m² útiles (unos 55-65 m² construidos), con las condiciones de luz, ventilación y accesibilidad que exigen las normas.

Así el mínimo se basa en lo que la propia ley considera habitable y no en un número elegido por mí. El panel permitirá cambiar ese tamaño en directo para ver cuánto mueve el coste.

## El hilo argumental (estructura del HTML)

**1. Qué hay que calcular**
1. **Demanda:** cuántos adultos hay, por provincia y grandes ciudades (INE: Estadística Continua de Población o Padrón) y cuántos cumplen 18 años cada año.
2. **Oferta existente:** qué viviendas hay (INE, Censo 2021: principales, secundarias y vacías) y cuántas cumplen el estándar digno según su superficie y características.
3. **La brecha:** cuántas viviendas dignas faltan, en total y en cada provincia.
4. **Precio de una vivienda, de abajo arriba:** suelo, urbanización, materiales, mano de obra (tablas salariales del convenio de la construcción en el BOE y horas de trabajo por m²), honorarios de arquitecto y aparejador, licencias, ICIO, IVA y financiación. Se compara con el **coste de comprar** viviendas existentes a su valor de mercado (valor tasado del Ministerio de Vivienda).
5. **Compensación a quien ya es propietario:** cuánto vale y cómo se reparte (pago único, deducción fiscal o renta), con su coste total.
6. **Capacidad física y plazos:** suelo urbanizable por provincia (Sistema de Información Urbana), capacidad del sector (visados, empleo de la EPA) y cuántos años costaría.
7. **Coste anual:** mantenimiento, reposición, las nuevas personas que cumplen 18 años cada año, el IBI que dejan de ingresar los ayuntamientos y la gestión.
8. **Financiación:** comparación con el PIB, con el gasto público y con la sanidad. Luego, cuántos **puntos de IRPF o IVA** habría que subir y **cuánto paga de más cada contribuyente según su tramo** (datos de la AEAT). Por último, la deuda y las reglas fiscales europeas.

**2. Escenarios**
- **Teórico puro:** todos los adultos viven solos en su vivienda digna. Es el techo de coste.
- **Plausible:** con datos reales de convivencia del INE (parejas, familias, jóvenes que siguen en casa de sus padres), cuánta gente ejercería de verdad el derecho a vivir sola. Se plantean también variantes, por ejemplo que dos personas que convivan puedan juntar sus derechos en una vivienda mayor.
- **Mínimo gratis más copago:** la vivienda digna mínima es gratuita y quien quiera una mayor o mejor situada paga la diferencia.

**3. Hipótesis y condiciones de contorno.** Todas explícitas y con rango.

**4. Datos → limpieza → operaciones → resultado.** Cada cifra lleva su fuente, su fecha y la operación con la que se obtiene.

**5. La mirada del economista y los dilemas**
- **¿Qué es digno?** Qué cambia si el mínimo sube o baja.
- **Madrid y otras zonas tensionadas:** qué pasa si la demanda supera el suelo disponible. Se comparan tres respuestas: densificar, asignar por listas o sorteo, o repartir la población hacia otras zonas.
- **¿Cómo se decide entre dos viviendas distintas?** Asignación, colas y el paralelismo con las listas de espera de la sanidad.
- **Economía:** quién acaba pagando de verdad el impuesto; efectos sobre el mercado, los precios y los materiales; incentivos y movilidad.
- **Encaje legal:** la Constitución protege la propiedad (art. 33), ampara la expropiación con indemnización y reconoce el derecho a la vivienda (art. 47).

**6. Modelo B: vivienda a precio fijo, al estilo de Singapur.** Cómo funciona allí, con fuentes primarias (HDB, SingStat, CPF Board): suelo público, pisos con derecho de uso por 99 años a precio subvencionado y ahorro obligatorio con el que se pagan. Después, cuánto costaría adaptarlo a España con los mismos datos del modelo A.

**7. Contraste A frente a B.** Tabla y veredicto en cuatro dimensiones: fiscal, física (capacidad para construir), temporal (cuántos años) y legal.

**8. «Abogado del diablo».** En cada bloque, las objeciones más fuertes de ambos lados y qué dicen los datos sobre ellas.

## Reglas de rigor

- **Solo fuentes oficiales como dato.** Lo que no exista en una fuente oficial se trata como **hipótesis con rango**, y se muestra cuánto cambia el resultado según ese rango.
- **El plan fija cómo investigar, no la conclusión.** Que el planteamiento parezca un disparate a primera vista no cuenta como prueba: lo que se ponga en pantalla tiene que salir de los números.

## Alcance y límites

- **Incluido:** toda España, con desglose por provincia y grandes ciudades cuando existan datos.
- **Fuera del alcance:** propuestas de ley, simulaciones de equilibrio general (los efectos se razonan con teoría y datos) y otros países salvo alguna mención de contexto.
- **Efectos externos:** solo lectura web y descarga de datasets de organismos oficiales. No publico nada: el HTML queda en tu bóveda.
- **Medios:** trabajaré con Opus 5.5 y, si ayuda, con subagentes en paralelo para recoger datos. Te avisaré si el volumen descargado supera unos 500 MB. Es un trabajo largo: iré informando de los avances.

**¿Apruebas esta versión 2 para empezar?**
