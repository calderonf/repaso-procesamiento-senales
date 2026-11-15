# Resumen teórico del curso

Este resumen recorre el curso en el mismo orden en que se vio: filtros analógicos, conversión A/D y D/A, sobremuestreo y sigma-delta, filtros digitales, punto fijo, análisis espectral y filtrado óptimo. No reemplaza las presentaciones de clase; sirve para repasar las ideas y las fórmulas que más se usan. Al final hay una tabla con las fórmulas clave.

!!! nota "Cómo estudiar con este material"
    Lea cada sección, cierre la página e intente explicar en voz alta las ideas principales. Luego vaya al [banco de preguntas](preguntas.html), intente responder cada pregunta antes de desplegar la respuesta y vuelva aquí cuando falle.

## 1. El sistema de procesamiento de señales

Casi todo sistema práctico sigue la misma cadena: **adquirir**, **procesar** y **reconstruir**.

1. **Sensor y acondicionamiento.** Un micrófono, un electrodo o un sensor de vibración entrega un voltaje pequeño que se amplifica y se desplaza al rango del conversor.
2. **Filtro antialias (analógico).** Limita la banda de la señal antes de muestrear.
3. **Muestreo y retención (S/H) y conversor A/D.** Toman muestras a una tasa constante fs y las cuantizan con N bits.
4. **Procesamiento digital.** Filtros FIR o IIR, análisis espectral, detección, compresión.
5. **Conversor D/A** (por ejemplo, PWM o sigma-delta) y **filtro de reconstrucción**, que elimina las réplicas espectrales y entrega una señal continua al actuador.

Aunque el procesamiento sea digital, siempre hacen falta filtros analógicos: uno antes del muestreo, para evitar el solapamiento (aliasing), y otro después del D/A, para reconstruir.

## 2. Respuesta en frecuencia y diagramas de Bode

Un sistema lineal e invariante en el tiempo (SLIT) continuo se describe con su función de transferencia

$$
H(s) = \frac{N(s)}{D(s)} = K\frac{(s-z_1)(s-z_2)\cdots}{(s-p_1)(s-p_2)\cdots}
$$

Los **ceros** son las raíces de $N(s)$ y los **polos** las de $D(s)$. Para que el sistema sea estable, todos los polos deben estar en el semiplano izquierdo ($\operatorname{Re}\{p_i\} < 0$): así cada modo $e^{p_i t}$ decae.

En estado estable senoidal, $s = j\omega$. La **respuesta en frecuencia** $H(j\omega)$ es un número complejo: su magnitud dice cuánto se amplifica una senoide de frecuencia $\omega$ y su fase cuánto se desplaza. Como cualquier señal se puede escribir como suma de senoides, $H(j\omega)$ contiene toda la información del sistema.

### Decibeles

$$
G_{dB} = 20\log_{10}\lvert H(j\omega)\rvert \qquad\qquad P_{dB} = 10\log_{10}\frac{P_2}{P_1}
$$

| Ganancia en dB | Factor de amplitud | Factor de potencia |
| --- | --- | --- |
| +20 dB | 10 | 100 |
| +6 dB | ≈ 2 | ≈ 4 |
| 0 dB | 1 | 1 |
| −3 dB | $1/\sqrt{2} \approx 0{,}707$ | 1/2 |
| −6 dB | ≈ 0,5 | ≈ 0,25 |
| −20 dB | 0,1 | 0,01 |
| −40 dB | 0,01 | 0,0001 |

### Reglas de Bode

| Término | Magnitud | Fase |
| --- | --- | --- |
| Constante $K$ | Recta horizontal en $20\log_{10}\lvert K\rvert$ | 0° si $K>0$; −180° si $K<0$ |
| Cero en el origen, $s$ | +20 dB/década, cruza 0 dB en $\omega=1$ | +90° constante |
| Polo en el origen, $1/s$ | −20 dB/década, cruza 0 dB en $\omega=1$ | −90° constante |
| Polo simple, $1/(1+s/\omega_c)$ | 0 dB hasta $\omega_c$, luego −20 dB/década; vale −3 dB en $\omega_c$ | De 0° a −90°; −45° en $\omega_c$; pendiente −45°/década entre $0{,}1\omega_c$ y $10\omega_c$ |
| Cero simple, $1+s/\omega_c$ | Igual que el polo pero +20 dB/década | De 0° a +90° |
| Par de polos complejos | 0 dB, luego −40 dB/década; cerca de $\omega_0$ hay un pico que depende de $\xi$ | De 0° a −180°; −90° en $\omega_0$ |

−20 dB/década equivale a −6 dB/octava, y −40 dB/década a −12 dB/octava.

**Interpretación geométrica.** $\lvert H(j\omega)\rvert$ es proporcional al producto de las distancias desde $j\omega$ hasta los ceros, dividido por el producto de las distancias hasta los polos. Cerca de un polo próximo al eje $j\omega$ la magnitud crece (resonancia) y la fase cambia rápido. Cerca de un cero próximo al eje la magnitud se hunde.

## 3. La señal de voz y la transmisión con ruido

### Características en el tiempo

En clase se analizó una grabación de voz a 8 kHz y 16 bits. Sus estadísticas típicas son:

- Distribución de amplitudes de tipo **exponencial bilateral** (laplaciana), muy concentrada cerca de cero, con picos ocasionales grandes.
- **Factor de cresta** (pico/rms) alrededor de 11, es decir unos 21 dB. Un seno tiene factor de cresta $\sqrt{2}$ (3 dB).
- Por eso la voz necesita un **rango dinámico** amplio: si el conversor se ajusta para no recortar los picos, el nivel típico queda muy por debajo de la escala completa.

### Características en frecuencia

- El espectro de potencia tiene un máximo cerca de 600 Hz y cae unos 30 dB hacia 4 kHz.
- Más del 90 % de la potencia está en menos del 40 % del ancho de banda (las bajas frecuencias).
- **Sonidos sonoros** (vocales): son cuasiperiódicos. Su espectro tiene armónicos de la frecuencia fundamental $f_0$, que es la vibración de las cuerdas vocales. En idiomas europeos, $f_0$ media es cerca de 119 Hz en hombres y 207 Hz en mujeres.
- **Sonidos no sonoros** (consonantes como /s/, /f/): no son periódicos y su energía está dispersa en altas frecuencias, como un ruido.
- El **tracto vocal** actúa como un filtro que da forma a la envolvente del espectro (formantes).
- El **espectrograma** muestra la energía en tiempo y frecuencia. Una ventana larga da buena resolución en frecuencia y mala en tiempo; una corta, lo contrario.

### Canal con ruido y énfasis

Un canal ideal con ruido blanco gaussiano aditivo (AWGN) suma ruido con la misma densidad espectral en todas las frecuencias. Como la voz tiene poca energía en altas frecuencias, allí la relación señal a ruido es mala y se pierde inteligibilidad (las consonantes).

- **Pre-énfasis (transmisor):** realza las altas frecuencias antes de que se sume el ruido.
- **De-énfasis (receptor):** es el filtro inverso. Restaura el espectro original de la voz y, al atenuar las altas frecuencias, atenúa también el ruido que entró allí.

Con un cero y un polo separados una década se logran 20 dB de énfasis. Por ejemplo, para el pre-énfasis:

$$
H_{pre}(s) = \frac{1 + s/\omega_z}{1 + s/\omega_p}, \qquad \omega_z = 2\pi\cdot 300,\quad \omega_p = 2\pi\cdot 3000
$$

El de-énfasis es $1/H_{pre}(s)$: el polo pasa a 300 Hz y el cero a 3 kHz.

## 4. Filtros analógicos

### 4.1 Tipos y especificaciones

Con funciones de segundo orden $D(s) = s^2 + b_1 s + b_0$, el numerador define el tipo de filtro:

| Tipo | Numerador $N(s)$ | Ceros |
| --- | --- | --- |
| Pasabajos (LP) | $a_0$ | Ninguno finito |
| Pasaaltos (HP) | $a_2 s^2$ | Dos en $s = 0$ |
| Pasabanda (BP) | $a_1 s$ | Uno en $s = 0$ |
| Banda rechazada (notch, BS) | $a_2 s^2 + a_0$ | En $\pm j\sqrt{a_0/a_2}$ |
| Pasatodo (all-pass) | $s^2 - b_1 s + b_0$ | Espejo de los polos, en el semiplano derecho |

Un filtro real se especifica con:

- **Banda de paso** ($\omega < \omega_p$): la ganancia no puede caer más de $A_p$ dB (rizado máximo).
- **Banda de rechazo** ($\omega > \omega_s$): la atenuación debe ser al menos $A_s$ dB.
- **Banda de transición** entre $\omega_p$ y $\omega_s$.
- El **factor de rizado** $\varepsilon$ se relaciona con el rizado en dB como $A_p = 10\log_{10}(1+\varepsilon^2)$. Con $\varepsilon = 1$, $A_p = 3$ dB.

El filtro ideal (ganancia constante en la banda de paso, cero en la de rechazo, fase lineal) no es realizable. $\lvert H(j\omega)\rvert^2$ es una función racional de $\omega^2$, así que no puede tener tramos constantes, discontinuidades ni caídas a tasa constante. Las aproximaciones buscan el mejor compromiso.

### 4.2 Aproximaciones clásicas

| Aproximación | Banda de paso | Banda de rechazo | Transición para un orden dado | Retardo de grupo |
| --- | --- | --- | --- | --- |
| Butterworth | Máximamente plana, monótona | Monótona | Media | Moderadamente variable |
| Chebyshev tipo I | Rizado de igual amplitud | Monótona | Más abrupta que Butterworth | Muy variable cerca del corte |
| Chebyshev tipo II (inversa) | Monótona | Rizado de igual amplitud | Más abrupta que Butterworth | Mejor que tipo I |
| Elíptica (Cauer) | Rizado | Rizado | La más abrupta | La peor |
| Bessel | Monótona, caída suave | Monótona | La más lenta | Máximamente plano (fase casi lineal) |

**Butterworth.** Su magnitud cuadrada es

$$
\lvert H(j\omega)\rvert^2 = \frac{1}{1 + \varepsilon^2\,(\omega/\omega_c)^{2n}}
$$

Para $\omega \gg \omega_c$ cae $20n$ dB por década. El orden mínimo que cumple $A_p$ en $\omega_p$ y $A_s$ en $\omega_s$ es

$$
n \ge \frac{\log_{10}\!\left[\dfrac{10^{A_s/10}-1}{10^{A_p/10}-1}\right]}{2\log_{10}(\omega_s/\omega_p)}
$$

y se redondea hacia arriba. Los polos del prototipo normalizado ($\omega_c = 1$, $\varepsilon = 1$) están sobre un círculo de radio 1, igualmente espaciados en el semiplano izquierdo.

**Bessel** se escoge cuando importa conservar la forma de onda (pulsos, ECG, datos), porque todas las componentes de la banda de paso se retrasan casi lo mismo y casi no hay sobrepaso en la respuesta al escalón.

En MATLAB: `buttord`/`butter`, `cheb1ord`/`cheby1`, `cheb2ord`/`cheby2`, `ellipord`/`ellip`, `besself`; con la opción `'s'` el diseño es analógico.

### 4.3 Desnormalización y transformaciones de frecuencia

Se diseña un prototipo pasabajos normalizado ($\omega_p = 1$) y luego se sustituye $s$:

| De pasabajos a | Sustitución | Orden |
| --- | --- | --- |
| Pasabajos con corte $\omega_c$ | $s \to s/\omega_c$ | Igual |
| Pasaaltos | $s \to \omega_p/s$ | Igual |
| Pasabanda | $s \to \dfrac{s^2 + \omega_{p1}\omega_{p2}}{(\omega_{p2}-\omega_{p1})\,s}$ | El doble |
| Banda rechazada | $s \to \dfrac{(\omega_{p2}-\omega_{p1})\,s}{s^2 + \omega_{p1}\omega_{p2}}$ | El doble |

En MATLAB: `lp2lp`, `lp2hp`, `lp2bp`, `lp2bs`, o directamente `butter(n, Wn, 'high'|'bandpass'|'stop', 's')`.

### 4.4 Sistemas de segundo orden

$$
H(s) = \frac{\omega_0^2}{s^2 + 2\xi\omega_0 s + \omega_0^2} = \frac{\omega_0^2}{s^2 + \dfrac{\omega_0}{Q}s + \omega_0^2},\qquad \xi = \frac{1}{2Q}
$$

$$
s_{1,2} = -\xi\omega_0 \pm j\omega_0\sqrt{1-\xi^2}
$$

| Caso | $\xi$ | $Q$ | Polos | Respuesta al escalón |
| --- | --- | --- | --- | --- |
| Oscilatorio | 0 | ∞ | $\pm j\omega_0$ | Oscilación sostenida |
| Subamortiguado | $0<\xi<1$ | $>0{,}5$ | Complejos conjugados | Oscila y se asienta, con sobrepaso |
| Críticamente amortiguado | 1 | 0,5 | Real doble en $-\omega_0$ | La más rápida sin sobrepaso |
| Sobreamortiguado | $>1$ | $<0{,}5$ | Dos reales distintos | Lenta, sin sobrepaso |

Para el caso subamortiguado:

$$
M_p = e^{-\pi\xi/\sqrt{1-\xi^2}} \qquad\qquad t_s(2\,\%) \approx \frac{4}{\xi\omega_0}
$$

Un Butterworth de segundo orden tiene $Q = 1/\sqrt{2} \approx 0{,}707$. En un pasabanda, $Q = \omega_0/BW$, con $BW$ el ancho de banda entre los puntos de −3 dB.

**Implementación pasiva (RLC serie, salida en el condensador):** $\omega_0 = 1/\sqrt{LC}$, $\xi = \dfrac{R}{2L\omega_0}$, $Q = \dfrac{\omega_0 L}{R}$.

**Implementaciones activas:**

- **Sallen-Key.** La más popular. El operacional trabaja como amplificador de ganancia fija, así que depende poco de sus limitaciones, y los valores de R y C son parecidos. Su desventaja es que $f_c$ y $Q$ son sensibles a la ganancia, sobre todo con $Q$ alto, y son difíciles de sintonizar por separado.
- **Retroalimentación múltiple (MFB).** Invierte la fase (+180°), depende más del operacional y se usa con $Q$ bajos. La dispersión de valores de los componentes es mayor.
- **Bicuadráticos (biquad, por ejemplo Ackerberg-Mossberg).** Usan varios operacionales (integradores). Permiten ajustar $\omega_0$ y $Q$ de forma casi independiente y entregan varias salidas (LP, BP, HP).

Un filtro de orden alto se implementa como **cascada de secciones de segundo orden**, más una de primer orden si el orden es impar. Cada sección realiza un par de polos con su propio $Q$.

### 4.5 Ruido térmico

Toda resistencia a temperatura $T$ genera ruido blanco gaussiano por el movimiento térmico de los electrones (Johnson-Nyquist). Su valor rms en un ancho de banda $B$ es

$$
v_n = \sqrt{4kTRB}, \qquad k = 1{,}38\times10^{-23}\ \text{J/K}
$$

El ruido crece con la resistencia, la temperatura y el ancho de banda. Por eso conviene limitar la banda con filtros.

## 5. Muestreo y reconstrucción

### 5.1 Teorema del muestreo

El muestreo uniforme toma $x[n] = x(nT_s)$, con $f_s = 1/T_s$. En frecuencia, muestrear equivale a **repetir el espectro** de la señal en múltiplos de $f_s$:

$$
X_s(f) = \frac{1}{T_s}\sum_{k=-\infty}^{\infty} X(f - k f_s)
$$

- **Señal de banda base** de ancho $B$: las réplicas no se superponen si $f_s \ge 2B$ (criterio de Nyquist). $f_s/2$ es la **frecuencia de Nyquist**.
- Si una componente está por encima de $f_s/2$, aparece "doblada" en $f_a = \lvert f - k f_s\rvert$, con el $k$ que deje $f_a$ entre 0 y $f_s/2$. Eso es el **aliasing**, y no se puede deshacer después de muestrear.
- **Señal pasabanda** entre $f_1$ y $f_2$, con $B = f_2 - f_1$: puede muestrearse a $f_s = 2f_2/m$, con $m$ la parte entera de $f_2/B$. Las réplicas caen en los huecos. Esto se usa en receptores y en medición (submuestreo).

### 5.2 Tipos de muestreo

| Tipo | Cómo es | Comentario |
| --- | --- | --- |
| Instantáneo (impulsivo) | Multiplica por un tren de impulsos | Modelo matemático; no es físicamente realizable |
| Natural | Multiplica por un tren de pulsos de ancho finito; la muestra sigue la forma de la señal durante el pulso | Las réplicas se ponderan por la envolvente sinc del pulso |
| Con retención (S/H) | Toma el valor al inicio del pulso y lo mantiene, normalmente en un condensador | El más usado. Equivale a impulsos seguidos de un retenedor de orden cero |

El **retenedor de orden cero** tiene respuesta en magnitud

$$
\lvert H_{ZOH}(f)\rvert = \left\lvert \frac{\sin(\pi f/f_s)}{\pi f/f_s} \right\rvert
$$

que en $f_s/2$ vale $2/\pi$ (−3,9 dB). El filtro de reconstrucción puede compensar esa caída con una forma $x/\sin x$.

### 5.3 Filtro antialias

Se ubica **antes** del muestreador y es analógico, normalmente pasabajos (a veces pasabanda). En su diseño intervienen seis frecuencias:

| Frecuencia | Significado |
| --- | --- |
| $f_{SIGNAL}$ | Ancho de banda de la señal de interés |
| $f_{LSB}$ | Hasta dónde el error de ganancia del filtro es menor que el permitido en LSB |
| $f_C$ | Frecuencia de corte (−3 dB) del filtro, típicamente 2 a 10 veces $f_{LSB}$ |
| $f_{PEAK}$ | Máxima frecuencia a la que el operacional entrega su excursión completa |
| $f_S$ | Frecuencia de muestreo del ADC |
| $f_{GBW}$ | Producto ganancia-ancho de banda del operacional |

$$
E_{dB} = 20\log_{10}\frac{2^N - \text{err}}{2^N} \qquad f_{GBW} \ge 100\cdot G\cdot Q\cdot f_C \qquad f_{PEAK} = \frac{SR}{\pi V_{pp}}
$$

Reglas prácticas para $f_S$: más del doble de $f_C$ (idealmente más de 10 veces), mayor que $f_{PEAK}$, o la que deje el aliasing por debajo del nivel aceptable de ruido.

## 6. Cuantización y conversión A/D

### 6.1 Cuantización uniforme

Un cuantizador de $N$ bits con escala completa $FS$ tiene $2^N$ niveles y paso

$$
\text{LSB} = \frac{FS}{2^N}
$$

El error de cuantización se modela como ruido uniforme entre $-\text{LSB}/2$ y $+\text{LSB}/2$, de potencia $\text{LSB}^2/12$. Para una señal con factor de cresta $FC$ cuyo pico coincide con la escala completa:

$$
SNR_{dB} = 6{,}02N + 4{,}77 - 20\log_{10}FC
$$

Para un seno ($FC = \sqrt{2}$) queda la fórmula conocida

$$
SNR_{dB} = 6{,}02N + 1{,}76
$$

Cada bit adicional aporta unos 6 dB. Una señal con factor de cresta alto, como la voz, necesita más bits para la misma SNR.

### 6.2 El conversor del Arduino UNO (ATmega328P)

- ADC de aproximaciones sucesivas de 10 bits, con multiplexor de 8 canales y referencia seleccionable (por ejemplo AVCC). Unas 15 000 muestras por segundo a resolución completa; el reloj del ADC se fija con un preescalador.
- **Modo libre (free running):** cada conversión arranca al terminar la anterior; la tasa depende del reloj del ADC.
- **Disparo por temporizador:** la conversión arranca con un evento del Timer0 (comparación con OCR0A). Así la tasa de muestreo es exacta y constante, que es lo que exige el procesamiento de señales.
- El resultado queda en ADCL y ADCH; se lee primero ADCL.

### 6.3 Temporizadores e interrupciones

- Timer0 y Timer2 son de 8 bits; Timer1 es de 16 bits. Modos: normal, CTC, Fast PWM, PWM de fase correcta y (Timer1) fase y frecuencia correcta.
- En **CTC** el contador va de 0 a OCRnA y se reinicia. La frecuencia de los eventos es

$$
f = \frac{f_{clk}}{N_{pre}\,(1 + \text{OCRnA})}
$$

con $f_{clk} = 16$ MHz y $N_{pre}$ el preescalador (1, 8, 64, 256, 1024).

- **Interrupciones frente a sondeo (polling):** con interrupciones, una rutina (ISR) atiende el evento apenas ocurre, y el programa principal queda libre. El bit I del registro SREG las habilita globalmente.
- Las variables compartidas entre la ISR y `loop()` se declaran `volatile`, para que el compilador las lea de memoria en cada acceso. `volatile` no hace atómicas las operaciones de varios bytes.

## 7. Conversión D/A con PWM

Una señal PWM tiene período $T$ y ancho de pulso $D$. Su **ciclo útil** es $C = D/T$ y su valor medio es

$$
\bar{v} = C\cdot V_{max}
$$

Variando el ciclo útil con cada muestra se codifica la señal en el valor medio. Un **filtro pasabajos** recupera ese valor medio y elimina la portadora en $f_{PWM}$ y sus armónicos. El filtro debe dejar pasar la banda de la señal y atenuar mucho en $f_{PWM}$, así que conviene que $f_{PWM}$ sea mucho mayor que el ancho de banda de la señal. Un filtro de mayor orden atenúa más la portadora.

| Modo | Rampa | Frecuencia | Comentario |
| --- | --- | --- | --- |
| Fast PWM | Simple (diente de sierra) | $f_{clk}/(N\,(1+TOP))$ | El pulso siempre empieza al inicio del período; su centro se corre con el ciclo útil (desfase) |
| Fase correcta | Doble (triangular) | $f_{clk}/(2N\cdot TOP)$ | Pulsos centrados en el período; la mitad de frecuencia para el mismo TOP |
| Fase y frecuencia correcta (Timer1) | Doble | $f_{clk}/(2N\cdot TOP)$ | TOP en ICR1, se actualiza sin glitches |

La **resolución** es $\log_2(TOP+1)$ bits. Con el Timer1 se puede usar ICR1 como TOP para escoger 8, 9 o 10 bits (TOP = 255, 511, 1023). **Más resolución implica menor frecuencia de portadora:** es el compromiso central del PWM como conversor D/A.

## 8. Sobremuestreo y modulación sigma-delta

### 8.1 Sobremuestreo directo

Si se muestrea a $f_s = OSR\cdot 2B$, la potencia del ruido de cuantización se reparte hasta $f_s/2$ y solo la fracción $1/OSR$ queda en la banda útil. Con un filtro digital y diezmado se elimina el resto:

$$
\Delta SNR = 10\log_{10}(OSR)
$$

Son 3 dB (medio bit) por cada vez que se duplica la tasa. Funciona solo si el error de cuantización no está correlacionado con la señal (por ejemplo, si hay algo de ruido).

### 8.2 Codificación diferencial

La señal de audio tiene muestras muy correlacionadas. Cuantizar la **diferencia** entre la muestra actual y una predicción (la anterior) reduce la varianza de lo que se cuantiza. Para que el error no se acumule, el cuantizador se coloca dentro de un lazo de realimentación.

### 8.3 Modulador sigma-delta

Un integrador, un cuantizador de 1 bit y una realimentación de la salida. El lazo obliga a que el **promedio de la salida siga a la entrada**. En el modelo discreto de primer orden:

$$
Y(z) = z^{-1}X(z) + (1 - z^{-1})E(z)
$$

- La señal pasa sin cambios, solo retrasada (STF = $z^{-1}$).
- El ruido de cuantización pasa por $1 - z^{-1}$, un **pasaaltos**: se empuja hacia altas frecuencias (**conformación del ruido**), fuera de la banda útil.
- Un filtro pasabajos y un diezmador digitales eliminan ese ruido y entregan muestras de muchos bits a la tasa final.

| Técnica | Mejora por octava de sobremuestreo |
| --- | --- |
| Sobremuestreo directo (PCM, PWM) | 3 dB |
| Sigma-delta de primer orden | 9 dB |
| Sigma-delta de orden $n$ | $6n + 3$ dB |

Los ADC de audio y los micrófonos MEMS digitales (como el INMP441) usan un modulador sigma-delta seguido de un filtro de diezmado. Como DAC, una salida sigma-delta de 1 bit seguida de un filtro analógico logra más resolución que un PWM a la misma frecuencia de reloj.

## 9. Filtros digitales

### 9.1 Sistemas discretos

Un SLIT discreto causal se describe con una ecuación en diferencias y su transformada Z:

$$
y[n] = \sum_{k=0}^{M} b_k\,x[n-k] - \sum_{k=1}^{N} a_k\,y[n-k] \qquad\qquad H(z) = \frac{\sum b_k z^{-k}}{1 + \sum a_k z^{-k}}
$$

- La respuesta en frecuencia es $H(e^{j\omega})$, con $\omega = 2\pi f/f_s$ en radianes por muestra. Es periódica con período $2\pi$ y basta estudiarla entre 0 y $\pi$ (0 a $f_s/2$).
- **Estabilidad:** un sistema causal es estable si y solo si todos sus polos están **dentro del círculo unitario**, $\lvert p_k\rvert < 1$.
- Un polo cerca del círculo unitario en el ángulo $\theta$ produce un pico en $\omega = \theta$; un cero sobre el círculo anula esa frecuencia.

### 9.2 Filtros ideales y fase lineal

El pasabajos ideal tiene respuesta al impulso $h[n] = \dfrac{\sin(\omega_c n)}{\pi n}$: es **no causal** y **no absolutamente sumable**, así que no se puede implementar. Sirve como punto de partida para aproximar.

Un filtro sin distorsión de fase retrasa todas las componentes por igual: su fase es lineal, $\theta(\omega) = -n_0\omega$. El **retardo de grupo**

$$
\tau_g(\omega) = -\frac{d\theta(\omega)}{d\omega}
$$

es el retardo, en muestras, que sufre la envolvente de una componente de frecuencia $\omega$. Con fase lineal es constante.

### 9.3 Filtros FIR

$$
y[n] = \sum_{k=0}^{M-1} b_k\,x[n-k], \qquad h[n] = b_n
$$

- Sin realimentación: solo tienen polos en $z = 0$, así que **siempre son estables**.
- **Fase lineal** si los coeficientes son simétricos, $h[n] = h[M-1-n]$, o antisimétricos. El retardo de grupo es constante e igual a $(M-1)/2$ muestras, el centro de simetría.
- Los ceros de un FIR de fase lineal aparecen en grupos: si $z_1$ es cero, también lo son $1/z_1$, $z_1^*$ y $1/z_1^*$.
- Con longitud par y simetría par, $H(z)$ tiene un cero en $z = -1$ (en $f_s/2$): ese tipo no sirve para pasaaltos.
- Necesitan muchos más coeficientes que un IIR para la misma selectividad.

### 9.4 Diseño FIR por ventanas

1. Se escribe la respuesta ideal $H_d(\omega)$ y se calcula $h_d[n]$, desplazada $\alpha = (M-1)/2$ para que sea simétrica. Para un pasabajos:

    $$h_d[n] = \frac{\sin(\omega_c(n-\alpha))}{\pi(n-\alpha)}$$

2. Se trunca a $M$ coeficientes multiplicando por una ventana $w[n]$: $h[n] = h_d[n]\,w[n]$.
3. Multiplicar en el tiempo es **convolucionar en frecuencia**: $H(\omega) = H_d(\omega) * W(\omega)$. El lóbulo principal de $W$ ensancha la transición; los lóbulos laterales producen rizado (fenómeno de Gibbs).

| Ventana | Lóbulo lateral de la ventana | Atenuación aproximada del filtro | Ancho de transición $\Delta f/f_s$ |
| --- | --- | --- | --- |
| Rectangular | −13 dB | 21 dB | $0{,}9/M$ |
| Hann | −31 dB | 44 dB | $3{,}1/M$ |
| Hamming | −42 dB | 53 dB | $3{,}3/M$ |
| Blackman | −57 dB | 74 dB | $5{,}5/M$ |
| Kaiser | Ajustable con $\beta$ | Ajustable | Ajustable |

La ventana fija la atenuación; la longitud $M$ fija el ancho de la transición. Aumentar $M$ con ventana rectangular angosta la transición pero no reduce el pico de rizado (≈ 9 %). En MATLAB: `fir1`, `fir2`, `filterDesigner`, `freqz`, `grpdelay`, `zplane`.

### 9.5 Filtros IIR

- Tienen realimentación (polos fuera del origen). Con pocos coeficientes logran transiciones abruptas y resonancias.
- Pueden volverse inestables si un polo sale del círculo unitario, por diseño o al cuantizar coeficientes.
- No tienen fase lineal.
- Se diseñan a partir de prototipos analógicos (Butterworth, Chebyshev, elíptico) con `butter`, `cheby1`, `cheby2`, `ellip` en modo digital, o ubicando polos y ceros a mano.

**Diseño por polos y ceros.** Un par de polos en $re^{\pm j\theta}$ produce una resonancia en $f_0 = \theta f_s/(2\pi)$, con ancho de banda aproximado $(1-r)f_s/\pi$ para $r$ cercano a 1:

$$
H(z) = \frac{1}{1 - 2r\cos\theta\, z^{-1} + r^2 z^{-2}}
$$

Ceros en $e^{\pm j\theta}$ (sobre el círculo) producen un **notch** que anula esa frecuencia. Con $r = 1$ los polos quedan sobre el círculo: la respuesta al impulso no decae y se obtiene un **oscilador digital** de frecuencia $\theta f_s/(2\pi)$.

### 9.6 Estructuras de realización

| Estructura | Retardos | Comentario |
| --- | --- | --- |
| FIR forma directa (línea de retardo, transversal) | $M-1$ | $M$ multiplicaciones |
| FIR de fase lineal plegada | $M-1$ | Se suman primero las muestras que comparten coeficiente: unas $M/2$ multiplicaciones |
| IIR forma directa I | $M + N$ | Ceros y polos por separado |
| IIR forma directa II (canónica) | $\max(M, N)$ | Polos primero, comparten la línea de retardo |
| Transpuestas | Iguales | Teorema de transposición: invertir todas las ramas e intercambiar entrada y salida no cambia $H(z)$ |
| Cascada de secciones de segundo orden (SOS) | — | Lo usual para IIR de orden alto |

Las formas directas de orden alto son muy sensibles a la cuantización: un error pequeño en un coeficiente del denominador puede mover mucho los polos. En una cascada SOS cada par de polos depende solo de dos coeficientes. MATLAB describe cada sección como una fila $[b_0\ b_1\ b_2\ a_0\ a_1\ a_2]$ más una ganancia $g$; hay que revisar con *Show filter structure* dónde se aplica $g$ y con qué signo entran los $a_k$.

### 9.7 Implementación en un microcontrolador

- **Buffer circular:** en lugar de desplazar las $M$ muestras pasadas en cada instante, se guarda la nueva sobre la más antigua y se recorre el arreglo con un índice que da la vuelta. El costo de memoria es el mismo y se evitan $M$ copias por muestra.
- **Coeficientes enteros:** se escalan por $2^F$ y se redondean. La salida se devuelve a la escala de la entrada con un corrimiento `>> F`. Si la suma de los coeficientes escalados es $2^F$, la ganancia DC es 1.
- **Tipos y casting:** en el Arduino UNO `int` es de 16 bits. Los productos y el acumulador deben calcularse en 32 bits, convirtiendo los operandos **antes** de multiplicar: `(int32_t)a * (int32_t)b`.
- **IIR en forma directa II:** $w_0 = x - a_1 w_1 - a_2 w_2$, $y = b_0 w_0 + b_1 w_1 + b_2 w_2$. Luego los estados se actualizan del más viejo al más nuevo: primero $w_2 \leftarrow w_1$ y después $w_1 \leftarrow w_0$.
- **Una estructura por sección** (coeficientes y estados) permite tener varios filtros y encadenar secciones SOS sin mezclar estados.
- **Verificación:** respuesta al impulso, al escalón y a senoides de varias frecuencias, comparadas muestra a muestra con la simulación; tiempo de ejecución con `micros()`.

## 10. Punto fijo

### 10.1 Idea central

El procesador guarda **enteros**. El programador decide qué factor de escala representa cada entero. Si el entero almacenado es $r$ y se reservan $F$ bits fraccionarios:

$$
x = \frac{r}{2^F} = r\cdot 2^{-F}, \qquad \text{LSB} = 2^{-F}
$$

El punto binario no ocupa memoria: es una regla de interpretación. Por ejemplo, el entero $r = 22 = 10110_2$ con $F = 3$ representa $10.110_2 = 22/8 = 2{,}75$.

### 10.2 Formatos y rangos

- $W$: bits totales; $F$ o $QF$: bits fraccionarios; $QI$: bits enteros sin contar el signo.
- Con signo (complemento a dos): $W = 1 + QI + QF$, y el bit más significativo pesa $-2^{W-1-F}$.

| Formato | Mínimo | Máximo | LSB |
| --- | --- | --- | --- |
| Sin signo, $W$, $F$ | 0 | $(2^W-1)/2^F$ | $2^{-F}$ |
| Con signo, $W$, $F$ | $-2^{W-1}/2^F$ | $(2^{W-1}-1)/2^F$ | $2^{-F}$ |

Ejemplo: con signo, $W = 6$, $F = 2$ es Q3.2, con rango de −8 a 7,75 y LSB 0,25. El rango con signo no es simétrico: falta un LSB en el lado positivo.

**La notación Q cambia entre autores:** unos cuentan el signo dentro de la parte entera y otros no, así que "Q1.15" puede significar cosas distintas. Lo seguro es declarar siempre **signed, W y F**. En MATLAB: `numerictype(signo, W, F)`.

Más bits fraccionarios dan pasos más finos, pero con $W$ fijo reducen el rango.

### 10.3 Codificar, redondear y desbordar

Para codificar se multiplica por $2^F$; si el resultado no es entero, hay que redondear. Ejemplo con $F = 3$: $0{,}6\cdot 8 = 4{,}8$.

| Método | Entero guardado | Valor | Error |
| --- | --- | --- | --- |
| Hacia abajo (floor) | 4 | 0,5 | −0,1 |
| Al más cercano | 5 | 0,625 | +0,025 |
| Hacia cero | 4 | 0,5 | −0,1 |

El método de redondeo forma parte de la especificación del filtro. Redondear siempre hacia abajo introduce un sesgo (error medio de −LSB/2); al más cercano no.

Cuando un resultado no cabe en el formato hay **overflow**:

- **Saturación:** se guarda el extremo más cercano (el máximo positivo o el mínimo negativo). El error queda acotado.
- **Wrap:** se conservan solo los $W$ bits bajos; equivale a operar módulo $2^W$. Un resultado positivo grande puede leerse como negativo, un error enorme que en audio suena como un golpe.

### 10.4 Tamaños de los tipos en C

En el Arduino UNO (ATmega328P): `char`/`int8_t` 8 bits, `int`/`int16_t` 16 bits, `long`/`int32_t` 32 bits, `long long`/`int64_t` 64 bits y `float` de 32 bits en IEEE 754. El estándar de C permite que `int` cambie entre plataformas: para exigir un ancho concreto se usa `<stdint.h>`. `sizeof` devuelve bytes, no bits.

### 10.5 Operaciones

- **Multiplicación:** las escalas también se multiplican.

    $$\frac{r_a}{2^{F_a}}\cdot\frac{r_b}{2^{F_b}} = \frac{r_a r_b}{2^{F_a+F_b}} \quad\Rightarrow\quad W_p = W_a + W_b,\quad F_p = F_a + F_b$$

- **Suma de dos números** con la misma escala: un bit más en el peor caso. Si las escalas son distintas, primero se alinean los puntos binarios.
- **Acumulación de $N$ productos** iguales: $W_{acc} = W_p + \lceil\log_2 N\rceil$ (bits de guarda), $F_{acc} = F_p$.
- **Reescalar** la salida: se corre a la derecha $F_{acc} - F_y$ bits. Esa conversión necesita una política de redondeo y de overflow.

Ejemplo de cadena FIR: entrada y coeficientes con signo $(12, 11)$, 64 taps. Producto $(24, 22)$, acumulador $(24 + 6, 22) = (30, 22)$. Para una salida $(12, 11)$ se descartan $22 - 11 = 11$ bits fraccionarios.

### 10.6 Dos significados de "normalizar"

1. **Reescalar un número:** cambiar de $F$, por ejemplo de 22 a 11. Es una operación de formato.
2. **Normalizar la ganancia del filtro:** escoger coeficientes que den la ganancia deseada. En un pasabajos, $H(0) = \sum_k h[k]$.

Cuantizar los coeficientes cambia la ganancia DC. Ejemplo: $h = [0{,}3\ \ 0{,}4\ \ 0{,}3]$ suma 1, pero con $F = 2$ (paso 0,25) queda $\hat{h} = [0{,}25\ \ 0{,}5\ \ 0{,}25]$, que también suma 1; con $F = 3$ queda $[0{,}25\ \ 0{,}375\ \ 0{,}25]$, que suma 0,875. Siempre hay que revisar las dos ganancias, la ideal y la cuantizada.

La cuantización de coeficientes también se ve como un ruido en la respuesta en frecuencia. En el laboratorio se escoge el menor ancho de palabra que mantiene ese ruido por debajo de un umbral, por ejemplo −50 o −60 dB.

## 11. Análisis espectral: DFT, FFT, ventanas y THD

### 11.1 DFT y FFT

$$
X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}, \qquad k = 0, \dots, N-1
$$

- El bin $k$ corresponde a $f_k = k f_s/N$. La **resolución en frecuencia** es $\Delta f = f_s/N$, y la ventana dura $N/f_s$ segundos.
- Para una señal real, $X[N-k] = X^*[k]$: basta con los bins 0 a $N/2$.
- La DFT directa cuesta $O(N^2)$ operaciones; la FFT, $O(N\log_2 N)$. Con $N = 1024$ son cerca de un millón frente a unas diez mil.

### 11.2 Leakage y ventanas

La DFT supone que el bloque de $N$ muestras se repite periódicamente. Si el bloque no contiene un número entero de ciclos, aparecen discontinuidades en los bordes y la energía de un tono se reparte en muchos bins: es el **leakage** (fuga espectral). Multiplicar el bloque por una ventana que va suavemente a cero en los extremos reduce los lóbulos laterales, a costa de ensanchar el lóbulo principal.

| Ventana | Primer lóbulo lateral | Ganancia coherente (promedio de $w$) |
| --- | --- | --- |
| Rectangular | −13 dB | 1 |
| Hann | −31 dB | 0,5 |
| Hamming | −42 dB | 0,54 |

Para leer la amplitud de un tono hay que compensar la ventana:

$$
A_k = \frac{2\,\lvert X[k]\rvert}{N\cdot\bar{w}}
$$

Si el tono cae justo en un bin, incluso la ventana rectangular muestra un pico limpio. Las diferencias entre ventanas se ven con tonos que caen entre dos bins.

### 11.3 Distorsión armónica total (THD)

$$
THD(\%) = 100\cdot\frac{\sqrt{V_2^2 + V_3^2 + \cdots + V_n^2}}{V_1}
$$

Los armónicos se suman en potencia (raíz de la suma de cuadrados). Para medirla con FFT: muestrear varios ciclos (por ejemplo 10 de 60 Hz a 1 kHz o más), aplicar una ventana, calcular $\lvert X[k]\rvert$, compensar la ganancia de la ventana y aplicar la fórmula. La THD importa por las pérdidas en transformadores y motores, la interferencia y normas como IEEE 519.

### 11.4 STFT y espectrograma

La transformada de Fourier de tiempo corto aplica la DFT a bloques sucesivos con ventana y salto $R$. El espectrograma es su magnitud al cuadrado. Una ventana larga da buena resolución en frecuencia y mala en tiempo; una corta, lo contrario.

## 12. Señales aleatorias y filtro de Wiener

### 12.1 Repaso de probabilidad

- **Media** $\mu = E[X]$, **varianza** $\sigma^2 = E[X^2] - \mu^2$.
- **Covarianza** $\sigma_{XY} = E[XY] - \mu_X\mu_Y$. Si es cero, las variables no están correlacionadas. Independencia implica no correlación, pero no al revés.
- **Distribuciones** frecuentes: uniforme ($\sigma^2 = (b-a)^2/12$, el modelo del error de cuantización), normal (el ruido térmico) y exponencial.
- Un proceso es **estacionario en sentido amplio** si su media es constante y su autocorrelación depende solo de la diferencia de tiempos, $\gamma_{xx}(m) = E[x(n)x(n-m)]$.
- La **densidad espectral de potencia** es la transformada de Fourier de la autocorrelación (Wiener-Khinchin). El **ruido blanco** tiene autocorrelación $\sigma^2\delta(m)$ y densidad espectral plana.
- A la salida de un SLIT: $S_{yy}(f) = \lvert H(f)\rvert^2 S_{xx}(f)$.

### 12.2 Filtro de Wiener FIR

Se busca el FIR $h[0], \dots, h[M-1]$ que, a partir de una entrada $x[n]$ (por ejemplo señal más ruido), estime una señal deseada $d[n]$ con el menor error cuadrático medio:

$$
J = E\left[\lvert e[n]\rvert^2\right], \qquad e[n] = d[n] - \sum_{k=0}^{M-1} h[k]\,x[n-k]
$$

- Si $d[n] = s[n]$ es **filtrado**; si $d[n] = s[n+D]$, **predicción**; si $d[n] = s[n-D]$, **suavizado**.
- **Principio de ortogonalidad:** en el óptimo, el error no está correlacionado con ninguna de las entradas usadas, $E[x[n-l]\,e^*[n]] = 0$ para $l = 0, \dots, M-1$.
- De ahí salen las **ecuaciones de Wiener-Hopf**:

    $$\sum_{k=0}^{M-1} h[k]\,\gamma_{xx}(l-k) = \gamma_{dx}(l), \qquad \Gamma_M\,\mathbf{h} = \boldsymbol{\gamma}_d \;\Rightarrow\; \mathbf{h}_{opt} = \Gamma_M^{-1}\boldsymbol{\gamma}_d$$

- $\Gamma_M$ es la matriz de autocorrelación de la entrada: **Toeplitz** (diagonales constantes) y hermitiana. Por eso puede resolverse eficientemente con el algoritmo de Levinson-Durbin.
- Si la señal y el ruido no están correlacionados, $\gamma_{xx} = \gamma_{ss} + \gamma_{ww}$ y $\gamma_{dx} = \gamma_{ss}$.

## 13. Fórmulas clave

| Tema | Fórmula |
| --- | --- |
| Decibeles | $20\log_{10}(\text{amplitud})$, $10\log_{10}(\text{potencia})$ |
| Polo simple | −3 dB y −45° en $\omega_c$; −20 dB/década |
| Segundo orden | $\xi = 1/(2Q)$; $M_p = e^{-\pi\xi/\sqrt{1-\xi^2}}$; −40 dB/década |
| Butterworth | $\lvert H\rvert^2 = 1/(1+\varepsilon^2\omega^{2n})$; $A_p = 10\log_{10}(1+\varepsilon^2)$ |
| Nyquist | $f_s \ge 2B$; alias en $\lvert f - kf_s\rvert$ |
| Muestreo pasabanda | $f_s = 2f_2/m$, $m = \lfloor f_2/B\rfloor$ |
| Retenedor de orden cero | $\lvert\operatorname{sinc}(f/f_s)\rvert$; −3,9 dB en $f_s/2$ |
| Cuantización | $\text{LSB} = FS/2^N$; ruido $\text{LSB}^2/12$; $SNR = 6{,}02N + 1{,}76$ dB (seno) |
| Timer en CTC | $f = f_{clk}/(N\,(1+\text{OCR}))$ |
| PWM | $\bar{v} = C\,V_{max}$; resolución $\log_2(TOP+1)$; Fast: $f_{clk}/(N(1+TOP))$; fase correcta: $f_{clk}/(2N\,TOP)$ |
| Sobremuestreo | Directo: 3 dB/octava; sigma-delta de orden $n$: $6n+3$ dB/octava |
| Frecuencia digital | $\omega = 2\pi f/f_s$ |
| FIR de fase lineal | $h[n] = \pm h[M-1-n]$; retardo $(M-1)/2$ muestras |
| Estabilidad IIR | Polos con $\lvert p\rvert < 1$ |
| Resonador digital | Polos en $re^{\pm j\theta}$; $f_0 = \theta f_s/(2\pi)$; $BW \approx (1-r)f_s/\pi$ |
| Punto fijo | $x = r/2^F$; producto: $W_a+W_b$, $F_a+F_b$; acumulador: $+\lceil\log_2 N\rceil$ bits |
| DFT | $\Delta f = f_s/N$; bin $k \leftrightarrow kf_s/N$; FFT $O(N\log_2 N)$ |
| Amplitud con ventana | $A_k = 2\lvert X[k]\rvert/(N\bar{w})$ |
| THD | $100\sqrt{\sum_{k\ge2}V_k^2}/V_1$ |
| Ruido térmico | $v_n = \sqrt{4kTRB}$ |
| Wiener | $\Gamma_M\mathbf{h} = \boldsymbol{\gamma}_d$ |
