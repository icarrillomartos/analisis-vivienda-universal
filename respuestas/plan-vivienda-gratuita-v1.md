# Propuesta: ¿Es viable la vivienda gratuita universal en España? · versión 1

**Para qué:** soporte visual y guion para un directo de YouTube. Tiene que dejar ver cada paso del razonamiento y cada cálculo, de modo que alguien de cualquier ideología pueda comprobarlos y aceptar o rebatir el resultado. **Destinatario:** audiencia general, con una explicación contada de junior a junior.

## Qué te entregaré

Un **HTML autocontenido, visual y didáctico**, pensado para ir pasando en directo: bloques grandes, gráficos, un paso por pantalla y un **panel de hipótesis** con controles para cambiarlas en directo y ver cómo se mueve el resultado. Irá acompañado de una **carpeta de auditoría** con los datasets oficiales descargados, los scripts de limpieza y cálculo y una tabla de fuentes. Así cualquiera puede reproducir las cifras.

## El hilo argumental (estructura del HTML)

**0. La tesis.** «Todo español tiene al menos una vivienda, y la primera es gratuita de por vida, pagada con impuestos, como la sanidad pública».

**1. Qué hay que demostrar.** La tesis se descompone en preguntas que se pueden calcular:
1. ¿Cuántas personas y cuántos hogares hay, y dónde viven? (INE: Padrón o Estadística Continua de Población y Encuesta Continua de Hogares)
2. ¿Cuántas viviendas harían falta en cada provincia o ciudad y cuántas existen ya? El INE (Censo 2021) cuenta viviendas principales, secundarias y vacías.
3. ¿De dónde saldrían las viviendas? Se comparan dos vías:
   - **comprar o expropiar** viviendas existentes a su valor de mercado (valor tasado del Ministerio de Vivienda por provincia);
   - **construirlas nuevas**, calculando el coste **de abajo arriba**, como pediste: suelo, urbanización, materiales, mano de obra (tablas salariales del convenio de la construcción en el BOE y horas de trabajo por m²), honorarios de arquitecto y aparejador, licencias, IVA e impuesto municipal de obras (ICIO), y financiación.
4. ¿Hay **suelo y capacidad física** para hacerlo, y en cuántos años? Se miran el suelo urbanizable (Sistema de Información Urbana del Ministerio), los visados de obra nueva y el empleo en construcción (EPA).
5. ¿Cuánto cuesta **mantenerlo cada año**? Conservación, reposición, nuevos hogares, IBI que dejan de pagar los ayuntamientos y gestión.
6. ¿Cómo se paga? El coste se compara con el PIB, con el gasto público y con lo que cuesta la sanidad pública (INE, IGAE, Eurostat). Después se traduce en **impuestos**:
   - cuántos puntos de IRPF o de IVA habría que subir;
   - cuánto pagaría de más cada contribuyente según su tramo de renta (datos de la AEAT);
   - qué pasaría con la deuda y con las reglas fiscales europeas (Banco de España).

**2. Hipótesis y condiciones de contorno.** Cada simplificación se dice en voz alta, por ejemplo: «vivienda tipo de 70 m² útiles», «el coste por m² depende de la provincia y no del barrio», «precios de 2025-2026 constantes».

**3. Datos → limpieza → operaciones → resultado**, paso a paso y con cada cifra enlazada a su fuente.

**4. La mirada del economista.** Qué pasa cuando se aplica en la realidad:
- quién acaba pagando de verdad el impuesto (incidencia fiscal);
- qué le ocurre al mercado y a los precios;
- si hay mano de obra y materiales suficientes, o si la demanda los encarece;
- incentivos, movilidad laboral y listas de espera, con la comparación de lo que pasa con la sanidad;
- encaje legal: la Constitución protege la propiedad (art. 33) y reconoce el derecho a una vivienda digna (art. 47).

**5. Modelo B: vivienda a precio fijo, al estilo de Singapur.** Cómo funciona allí, con datos de fuentes primarias (HDB, SingStat, CPF Board): el Estado es dueño de la mayoría del suelo, vende pisos con derecho de uso por 99 años a precio subvencionado y la compra se financia con un ahorro obligatorio (el CPF). Después, cuánto costaría adaptarlo a España con los mismos datos del modelo A.

**6. Contraste A frente a B.** Una tabla y un veredicto en cuatro dimensiones: fiscal, física (capacidad para construir), temporal (cuántos años) y legal/política.

**7. «Abogado del diablo».** En cada bloque, las objeciones más fuertes de los dos lados y qué dicen los datos sobre ellas.

## Reglas de rigor

- **Solo fuentes oficiales como dato.** Si algo no existe en una fuente oficial (por ejemplo, los honorarios de arquitecto dejaron de tener tarifa oficial), no lo invento ni lo saco de un blog. Lo marco como **hipótesis con un rango** y muestro cuánto cambia el resultado según ese rango.
- **El plan fija cómo investigar, no la conclusión.** Si los datos llevan a un veredicto incómodo para cualquiera de las dos posturas, se presenta tal cual.
- Cada número del HTML llevará su fuente, su fecha y su operación.

## Decisiones que cambian el resultado (mi propuesta por defecto)

1. **Unidad:** calcular por **hogar** como escenario principal, con un escenario alternativo **por persona adulta**. «Una vivienda por español» multiplica el resultado aproximadamente por dos.
2. **Beneficiarios:** **residentes**, como en la sanidad, con un escenario alternativo solo de nacionalidad española.
3. **Quien ya tiene vivienda en propiedad:** calcular dos escenarios:
   - **A1, universal pura:** el Estado se hace cargo de todas las primeras viviendas y compensa a quien ya la tiene;
   - **A2, cubrir la brecha:** solo se da vivienda a quien no la tiene en propiedad.

   Se muestra el coste de cada uno y el dilema de equidad que plantea.

## Alcance y límites

- **Incluido:** toda España, con desglose por provincia y por las grandes ciudades cuando existan datos.
- **Fuera del alcance:** propuestas de ley, modelos macroeconómicos de equilibrio general (los efectos se razonan con teoría y datos, no se simulan) y países que no sean Singapur, salvo alguna mención de contexto.
- **Efectos externos:** solo lectura web y descarga de datasets de organismos oficiales. No publico nada. El HTML queda en tu bóveda; si luego quieres un enlace para compartirlo, lo decidimos aparte.
- **Medios:** trabajaré con Opus 5.5, el modelo que tiene esta sesión. Puedo repartir la búsqueda de datos entre subagentes en paralelo. Es un trabajo largo: te iré avisando de los avances.

**¿Apruebas este plan tal cual, o quieres cambiar alguna de las tres decisiones por defecto antes de empezar?**
