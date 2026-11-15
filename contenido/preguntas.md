# Banco de preguntas de repaso

Intente responder cada pregunta por escrito o en voz alta **antes** de desplegar la respuesta. Las preguntas de cálculo se pueden resolver a mano. Si una respuesta le sorprende, vuelva a la sección correspondiente del [resumen](resumen.html).

**El examen final cubre los temas 1 a 10.** Los temas 11 (análisis espectral y THD) y 12 (señales aleatorias y Wiener) son **opcionales**: practíquelos solo si quiere profundizar.

## 1. Respuesta en frecuencia y Bode

**1.** ¿Por qué la respuesta en frecuencia $H(j\omega)$ basta para calcular la respuesta en estado estable de un SLIT ante cualquier señal, y no solo ante senoides?

??? respuesta "Ver respuesta"
    En un SLIT, una senoide de entrada produce a la salida una senoide de la misma frecuencia, solo escalada por $\lvert H(j\omega)\rvert$ y desfasada $\angle H(j\omega)$. Cualquier señal se puede descomponer en una suma (o integral) de senoides mediante Fourier. Por linealidad, la salida es la suma de las respuestas a cada componente, y cada una queda determinada por $H(j\omega)$ en su frecuencia.

**2.** Un amplificador tiene una ganancia de −26 dB a cierta frecuencia. ¿Por qué factor se multiplica la amplitud de la señal? ¿Y su potencia?

??? respuesta "Ver respuesta"
    Amplitud: $10^{-26/20} \approx 0{,}050$, es decir la señal queda en una vigésima parte. Potencia: $10^{-26/10} \approx 0{,}0025$, el cuadrado del factor de amplitud. Un atajo útil: −20 dB es un factor 0,1 y −6 dB es la mitad; −26 dB es 0,1 × 0,5 = 0,05.

**3.** Describa el diagrama de Bode asintótico de magnitud de $H(s) = \dfrac{10\,(s + 10)}{s + 1000}$.

??? respuesta "Ver respuesta"
    En baja frecuencia $H(0) = 10\cdot 10/1000 = 0{,}1$, es decir −20 dB. En $\omega = 10$ rad/s el cero empieza a subir la magnitud a +20 dB/década. En $\omega = 1000$ rad/s el polo compensa al cero y la magnitud vuelve a ser plana. Entre 10 y 1000 rad/s hay dos décadas, así que la magnitud sube 40 dB: de −20 dB a +20 dB. Es un filtro que realza las altas frecuencias, como un pre-énfasis.

**4.** Usando la interpretación geométrica de polos y ceros, explique por qué un cero muy cercano al eje $j\omega$ produce un hundimiento en la magnitud.

??? respuesta "Ver respuesta"
    $\lvert H(j\omega)\rvert$ es proporcional al producto de las distancias desde el punto $j\omega$ hasta cada cero, dividido por el producto de las distancias hasta cada polo. Cuando $j\omega$ pasa junto a un cero muy cercano al eje, la distancia a ese cero se vuelve muy pequeña y la magnitud cae casi a cero. Además, al pasar junto al cero esa distancia cambia de dirección muy rápido, por eso la fase cambia bruscamente. Con un polo pasa lo contrario: la magnitud crece (resonancia).

**5.** Un pasaaltos de primer orden tiene $f_c = 300$ Hz. ¿Cuál es su ganancia aproximada en 30 Hz y en 3 kHz? ¿Cuál es su fase en 300 Hz?

??? respuesta "Ver respuesta"
    30 Hz está una década por debajo del corte: la asíntota de +20 dB/década da −20 dB (el valor exacto es −20,04 dB). 3 kHz está una década por encima: prácticamente 0 dB (exacto, −0,04 dB). En la frecuencia de corte la magnitud es −3 dB y la fase de un cero sobre un polo en el origen da +45° (el pasaaltos adelanta la fase de +90° en baja frecuencia a 0° en alta).

## 2. Voz, ruido y énfasis

**6.** ¿Qué diferencia hay entre los sonidos sonoros y los no sonoros de la voz, y cómo se distinguen en un espectrograma?

??? respuesta "Ver respuesta"
    Los sonoros (vocales) se producen con vibración de las cuerdas vocales: son cuasiperiódicos y su espectro tiene armónicos de la frecuencia fundamental $f_0$. En el espectrograma se ven como líneas horizontales paralelas y espaciadas $f_0$, con zonas más intensas (formantes) que forma el tracto vocal. Los no sonoros (consonantes como /s/ o /f/) se producen por turbulencia: no son periódicos, su energía está dispersa, sobre todo en altas frecuencias, y en el espectrograma aparecen como manchas difusas sin líneas.

**7.** Al calcular un espectrograma se escoge la longitud de la ventana. ¿Qué cambia si se usa una ventana de 20 ms en lugar de una de 80 ms?

??? respuesta "Ver respuesta"
    La resolución en frecuencia es aproximadamente el inverso de la duración de la ventana. Con 80 ms es de unos 12,5 Hz: se separan bien los armónicos, pero los cambios rápidos se borran en el tiempo. Con 20 ms es de unos 50 Hz: se ven mejor los eventos rápidos (inicios de sílabas, consonantes), pero los armónicos cercanos se mezclan. No se puede tener a la vez resolución perfecta en tiempo y en frecuencia.

**8.** Se quiere un pre-énfasis de primer orden que realce 20 dB entre 300 Hz y 3 kHz. ¿Dónde se ubican el cero y el polo? ¿Y en el de-énfasis?

??? respuesta "Ver respuesta"
    Pre-énfasis: $H(s) = (1 + s/\omega_z)/(1 + s/\omega_p)$ con el **cero en 300 Hz** y el **polo en 3 kHz**. Entre ambos la magnitud sube a +20 dB/década durante una década: 20 dB. Por debajo de 300 Hz la ganancia es 0 dB y por encima de 3 kHz queda plana en +20 dB. El de-énfasis es el inverso exacto: polo en 300 Hz y cero en 3 kHz. Así el producto de los dos es 1 y la voz se recupera sin distorsión.

**9.** En la práctica de detección de sexo por el tono de voz se usaron dos pasabanda de segundo orden centrados cerca de 119 Hz y 207 Hz. ¿Por qué esta decisión nunca será perfecta, y qué parámetro del filtro hay que escoger con cuidado?

??? respuesta "Ver respuesta"
    Las distribuciones de la frecuencia fundamental de hombres y mujeres se superponen: hay hombres con voz aguda y mujeres con voz grave, y además $f_0$ varía dentro de una misma frase. Por eso cualquier umbral tendrá errores. En el filtro hay que escoger bien el factor de calidad $Q = \omega_0/BW$: un $Q$ muy alto deja pasar una banda tan estrecha que pierde voces que se alejan un poco de la media; un $Q$ muy bajo deja que cada filtro responda también a la otra población.

## 3. Filtros analógicos

**10.** En la especificación de un filtro pasabajos aparecen $\omega_p$, $\omega_s$, $A_p$ y $A_s$. ¿Qué significa cada uno?

??? respuesta "Ver respuesta"
    $\omega_p$ es el borde de la banda de paso: hasta allí la ganancia no puede caer más de $A_p$ dB (el rizado máximo permitido). $\omega_s$ es el borde de la banda de rechazo: desde allí la atenuación debe ser de al menos $A_s$ dB. Entre $\omega_p$ y $\omega_s$ está la banda de transición, donde no se exige nada. Cuanto más estrecha la transición, mayor $A_s$ y menor $A_p$, más alto es el orden necesario.

**11.** ¿Por qué un filtro con respuesta perfectamente rectangular (ganancia 1 hasta $\omega_c$ y 0 después) no se puede construir con resistencias, condensadores, bobinas y amplificadores?

??? respuesta "Ver respuesta"
    Esos circuitos tienen funciones de transferencia racionales, y $\lvert H(j\omega)\rvert^2$ resulta una función racional y continua de $\omega^2$. Una función así no puede tener tramos exactamente constantes, ni saltos, ni ser exactamente cero en un intervalo. Además, el filtro ideal tiene una respuesta al impulso tipo sinc que empieza antes de $t = 0$: no es causal. Las aproximaciones (Butterworth, Chebyshev, etc.) buscan acercarse con un orden finito.

**12.** Calcule el orden mínimo de un Butterworth pasabajos que tenga como mucho 1 dB de caída en 1 kHz y al menos 40 dB de atenuación en 3 kHz.

??? respuesta "Ver respuesta"

    $$n \ge \frac{\log_{10}\!\left[\dfrac{10^{4}-1}{10^{0{,}1}-1}\right]}{2\log_{10}(3)} = \frac{\log_{10}(38\,622)}{0{,}954} = \frac{4{,}587}{0{,}954} \approx 4{,}81$$

    Se redondea hacia arriba: **n = 5**. Comprobación rápida: para $\omega \gg \omega_c$ un Butterworth de orden 5 cae 100 dB/década; entre 1 y 3 kHz hay casi media década, lo que da unos 48 dB, consistente con lo pedido.

**13.** Para la especificación de la pregunta anterior, ¿un Chebyshev tipo I necesitaría un orden mayor o menor? ¿Qué se sacrifica?

??? respuesta "Ver respuesta"
    Menor. El Chebyshev I aprovecha todo el rizado permitido en la banda de paso (1 dB) para caer más rápido en la transición, así que con menos orden alcanza los 40 dB. A cambio, la banda de paso tiene rizado y el retardo de grupo varía mucho cerca del corte: más distorsión de fase y más sobrepaso en la respuesta al escalón.

**14.** ¿Qué aproximación escogería para filtrar una señal de ECG o un tren de pulsos digitales, y por qué?

??? respuesta "Ver respuesta"
    Bessel. Su retardo de grupo es casi constante en la banda de paso (fase casi lineal), así que todas las componentes de la señal se retrasan lo mismo y la forma de onda se conserva, con muy poco sobrepaso. En un ECG eso evita deformar el complejo QRS y en pulsos evita oscilaciones. El costo es una transición lenta: para la misma atenuación necesita más orden que otras aproximaciones.

**15.** Un filtro tiene un factor de rizado $\varepsilon = 0{,}5$. ¿Cuál es el rizado en la banda de paso, en dB?

??? respuesta "Ver respuesta"
    $A_p = 10\log_{10}(1 + \varepsilon^2) = 10\log_{10}(1{,}25) \approx 0{,}97$ dB. Es decir, la ganancia puede bajar casi 1 dB respecto al máximo dentro de la banda de paso. Con $\varepsilon = 1$ serían 3 dB.

**16.** Un sistema de segundo orden tiene polos en $s = -300 \pm j400$ rad/s. Halle $\omega_0$, $\xi$ y $Q$, clasifíquelo y estime su sobrepaso ante un escalón.

??? respuesta "Ver respuesta"
    $\omega_0$ es la distancia de los polos al origen: $\sqrt{300^2 + 400^2} = 500$ rad/s. La parte real es $-\xi\omega_0$, así que $\xi = 300/500 = 0{,}6$ y $Q = 1/(2\xi) \approx 0{,}83$. Como $0 < \xi < 1$, es **subamortiguado**. Sobrepaso: $M_p = e^{-\pi\cdot 0{,}6/0{,}8} \approx 0{,}095$, cerca del 9,5 %.

**17.** ¿Cómo es la función de transferencia de un filtro notch de segundo orden para eliminar 60 Hz, y qué controla el ancho de la muesca?

??? respuesta "Ver respuesta"

    $$H(s) = \frac{s^2 + \omega_0^2}{s^2 + \dfrac{\omega_0}{Q}s + \omega_0^2}, \qquad \omega_0 = 2\pi\cdot 60$$

    Los ceros están sobre el eje imaginario en $\pm j\omega_0$, así que la ganancia en 60 Hz es exactamente cero. Los polos están cerca de los ceros. El factor de calidad $Q$ controla el ancho: con $Q$ alto los polos quedan muy cerca de los ceros y la muesca es estrecha, afectando poco a las frecuencias vecinas.

**18.** Un Butterworth de orden 6 se va a construir con secciones Sallen-Key. ¿Cuántas secciones hacen falta y por qué no se construye como un solo circuito de orden 6?

??? respuesta "Ver respuesta"
    Tres secciones de segundo orden, cada una con un par de polos conjugados del Butterworth y su propio $Q$ (para orden 6 son aproximadamente 0,52; 0,71 y 1,93). Un circuito de orden 6 en una sola etapa sería extremadamente sensible a las tolerancias de los componentes. En cascada, cada sección se diseña y ajusta por separado, y los errores de una no se propagan a los polos de las otras.

**19.** Un RLC serie con salida en el condensador tiene R = 100 Ω, L = 10 mH y C = 1 µF. Halle $\omega_0$, $f_0$ y $Q$.

??? respuesta "Ver respuesta"
    $\omega_0 = 1/\sqrt{LC} = 1/\sqrt{10^{-2}\cdot 10^{-6}} = 10^4$ rad/s, así que $f_0 = 10^4/(2\pi) \approx 1{,}59$ kHz. $Q = \omega_0 L/R = 10^4\cdot 0{,}01/100 = 1$ (equivale a $\xi = 0{,}5$, subamortiguado con un pequeño pico de resonancia).

**20.** ¿Cuál es el voltaje de ruido térmico rms de una resistencia de 10 kΩ a 300 K en un ancho de banda de 20 kHz? ¿Qué puede hacer el diseñador para reducirlo?

??? respuesta "Ver respuesta"
    $v_n = \sqrt{4kTRB} = \sqrt{4\cdot 1{,}38\times10^{-23}\cdot 300\cdot 10^4\cdot 2\times10^4} \approx 1{,}8$ µV rms. Para reducirlo: usar resistencias más pequeñas, limitar el ancho de banda con filtros al mínimo que necesita la señal y, en casos extremos, enfriar el circuito.

## 4. Muestreo y reconstrucción

**21.** Una señal tiene componentes en 1 kHz y en 7 kHz y se muestrea a 8 kHz sin filtro antialias. ¿Qué se observa después de muestrear?

??? respuesta "Ver respuesta"
    La frecuencia de Nyquist es 4 kHz. La componente de 7 kHz se dobla a $\lvert 7 - 8\rvert = 1$ kHz: cae exactamente sobre la componente legítima de 1 kHz. Después de muestrear solo se ve un tono de 1 kHz cuya amplitud y fase dependen de la suma de los dos, y es imposible separarlos. Por eso el filtro antialias debe actuar antes de muestrear.

**22.** Se muestrea a 10 kHz un tono de 13 kHz. ¿A qué frecuencia aparece?

??? respuesta "Ver respuesta"
    Se busca $\lvert 13 - k\cdot 10\rvert$ entre 0 y 5 kHz: con $k = 1$ da 3 kHz. El tono de 13 kHz aparece como un tono falso de **3 kHz**.

**23.** Una señal de FI ocupa de 450 a 460 kHz. ¿Cuál es la frecuencia de muestreo mínima teórica que evita el solapamiento según el criterio pasabanda?

??? respuesta "Ver respuesta"
    $B = 10$ kHz, $m = \lfloor 460/10\rfloor = 46$ y $f_s = 2\cdot 460/46 = 20$ kHz. Es decir, basta $2B$ porque la banda cabe justo en una zona de Nyquist. Muestrear con el criterio de banda base exigiría más de 920 kHz. En la práctica se deja un margen, porque una banda tan justa no tolera ninguna transición del filtro.

**24.** ¿Cuánto atenúa un retenedor de orden cero (S/H) una componente en $f_s/2$, y por qué importa?

??? respuesta "Ver respuesta"
    Su magnitud es $\lvert\operatorname{sinc}(f/f_s)\rvert$. En $f_s/2$ vale $\sin(\pi/2)/(\pi/2) = 2/\pi \approx 0{,}64$, es decir −3,9 dB. Las altas frecuencias de la banda útil salen atenuadas en la reconstrucción. Si importa, el filtro de reconstrucción (o un filtro digital previo) se diseña con un realce de forma $x/\sin x$ que compense esa caída.

**25.** Compare el espectro de una señal muestreada en forma natural con el de una muestreada con retención.

??? respuesta "Ver respuesta"
    En el muestreo natural cada réplica del espectro conserva la forma del espectro original; solo su amplitud cambia según la envolvente sinc del pulso. Con retención, el espectro completo (réplicas y banda base) queda multiplicado por la sinc del retenedor, así que **la propia banda útil se distorsiona** y aparece la atenuación hacia $f_s/2$. Por eso solo el S/H necesita compensación en el filtro de reconstrucción.

**26.** Para un ADC de 10 bits se tolera un error de ganancia de 1 LSB en la banda de la señal. ¿Cuál es el error máximo del filtro antialias en dB? ¿Qué tipo de aproximación favorece este requisito?

??? respuesta "Ver respuesta"
    $E_{dB} = 20\log_{10}\dfrac{1024-1}{1024} \approx -8{,}5$ mdB (milésimas de dB). Es una exigencia de planitud muy estricta en la banda de la señal, así que favorece aproximaciones máximamente planas (Butterworth) y obliga a poner la frecuencia de corte bastante por encima de la banda de la señal.

**27.** Un operacional tiene un slew rate de 0,5 V/µs y debe entregar 10 V pico a pico. ¿Cuál es su $f_{PEAK}$?

??? respuesta "Ver respuesta"
    $f_{PEAK} = SR/(\pi V_{pp}) = 0{,}5\times10^6/(\pi\cdot 10) \approx 15{,}9$ kHz. Por encima de esa frecuencia el operacional no puede seguir una senoide de 10 V pico a pico sin distorsionarla, así que limita la banda útil del filtro activo y es un criterio para escoger $f_s$.

**28.** La voz telefónica ocupa 300–3400 Hz. ¿Por qué se muestrea a 8 kHz y no a 6,8 kHz, que ya cumple Nyquist?

??? respuesta "Ver respuesta"
    Con 6,8 kHz el filtro antialias tendría que pasar 3400 Hz y rechazar todo desde 3400 Hz: una transición de ancho cero, que requeriría orden infinito. A 8 kHz la frecuencia de Nyquist es 4 kHz y queda una banda de transición de 600 Hz, que un filtro analógico de orden razonable puede cubrir.

## 5. Cuantización y conversión A/D

**29.** ¿Por qué el error de cuantización se modela como un ruido uniforme de potencia $\text{LSB}^2/12$, y cuándo deja de ser válido ese modelo?

??? respuesta "Ver respuesta"
    Si la señal es "activa" (cambia mucho de un nivel a otro), el error en cada muestra está en cualquier punto entre −LSB/2 y +LSB/2 con igual probabilidad. La varianza de una distribución uniforme de ancho $\Delta$ es $\Delta^2/12$. El modelo falla cuando la señal es muy pequeña (comparable a 1 LSB), constante o periódica y sincronizada con el muestreo: entonces el error queda correlacionado con la señal y aparece como distorsión armónica, no como ruido.

**30.** ¿Cuántos bits necesita un ADC para lograr al menos 70 dB de SNR con un seno a escala completa?

??? respuesta "Ver respuesta"
    $6{,}02N + 1{,}76 \ge 70 \Rightarrow N \ge 11{,}34$. Se necesitan **12 bits**, que dan unos 74 dB.

**31.** Una señal de voz tiene factor de cresta 10 (20 dB) y su pico se ajusta a la escala completa del ADC. ¿Cuántos bits hacen falta para una SNR de 60 dB? Compare con un seno.

??? respuesta "Ver respuesta"
    $SNR = 6{,}02N + 4{,}77 - 20\log_{10}(10) = 6{,}02N - 15{,}23 \ge 60 \Rightarrow N \ge 12{,}5$: **13 bits**. Un seno necesitaría solo $N \ge (60 - 1{,}76)/6{,}02 = 9{,}7$, es decir 10 bits. La diferencia de 3 bits viene de que la voz tiene su potencia muy por debajo de su pico.

**32.** ¿Por qué en procesamiento de señales se prefiere disparar el ADC con un temporizador en lugar de leerlo en `loop()` con `analogRead()`?

??? respuesta "Ver respuesta"
    Toda la teoría (DFT, filtros digitales, frecuencias en radianes por muestra) supone muestras tomadas a intervalos exactamente iguales. En `loop()` el instante de cada lectura depende de lo que tarde el resto del código, así que la tasa varía (jitter) y no se conoce con precisión. Con el disparo por temporizador, el hardware arranca cada conversión a una tasa fija, independiente del programa.

**33.** Con el Timer0 del Arduino UNO en modo CTC y preescalador 64, ¿qué valor de OCR0A da interrupciones a 2 kHz?

??? respuesta "Ver respuesta"
    $1 + \text{OCR0A} = 16\times10^6/(64\cdot 2000) = 125$, así que **OCR0A = 124**. El "+1" aparece porque el contador cuenta desde 0 hasta OCR0A inclusive.

**34.** ¿Por qué el resultado del ADC del ATmega328P se lee primero en ADCL y después en ADCH?

??? respuesta "Ver respuesta"
    El resultado de 10 bits no cabe en un registro de 8 bits y queda repartido en dos. Al leer ADCL, el hardware bloquea la actualización de los registros hasta que se lea ADCH. Así los dos bytes corresponden a la misma conversión. Si se leyera ADCH primero, una conversión nueva podría terminar entre las dos lecturas y mezclar bytes de muestras distintas.

**35.** ¿Por qué una variable que se modifica dentro de una ISR y se lee en `loop()` debe declararse `volatile`? ¿Basta eso para leer sin riesgo una variable de 16 bits?

??? respuesta "Ver respuesta"
    Sin `volatile`, el compilador puede suponer que la variable no cambia dentro de `loop()` y guardar una copia en un registro, así que nunca vería el valor nuevo que escribe la ISR. `volatile` obliga a leerla de memoria en cada acceso. Pero no basta para una variable de 16 bits en un procesador de 8 bits: la lectura toma dos instrucciones y la ISR puede ocurrir entre ellas. Para leerla sin riesgo hay que deshabilitar las interrupciones un instante (sección crítica).

## 6. Conversión D/A con PWM

**36.** Describa el espectro de una señal PWM con ciclo útil variable y explique qué debe cumplir el filtro de reconstrucción.

??? respuesta "Ver respuesta"
    El espectro tiene la señal útil en banda base (el valor medio que sigue al ciclo útil) más componentes alrededor de la frecuencia de la portadora $f_{PWM}$ y sus múltiplos. El filtro pasabajos debe dejar pasar la banda de la señal sin atenuarla y atenuar mucho la portadora. Esto solo es fácil si $f_{PWM}$ está muy por encima del ancho de banda de la señal.

**37.** Con el Timer1 a 16 MHz, preescalador 1 y TOP = 511, ¿qué resolución y qué frecuencia de portadora tiene un Fast PWM? ¿Y uno de fase correcta?

??? respuesta "Ver respuesta"
    Resolución: $\log_2(511 + 1) = 9$ bits en ambos casos. Fast PWM: $16\times10^6/512 = 31{,}25$ kHz. Fase correcta: $16\times10^6/(2\cdot 511) \approx 15{,}7$ kHz, cerca de la mitad, porque el contador sube y baja en cada período.

**38.** Una señal de 4 kHz de ancho de banda se reconstruye desde un PWM de 31,25 kHz con un filtro RC de un polo en 4 kHz. ¿Cuánto se atenúa la portadora? ¿Y con un filtro de dos polos en 4 kHz?

??? respuesta "Ver respuesta"
    De 4 a 31,25 kHz hay $\log_{10}(31{,}25/4) \approx 0{,}89$ décadas. Con un polo: unos $20\cdot 0{,}89 \approx 18$ dB, una atenuación pobre que deja un rizado visible. Con dos polos: unos 36 dB. Para mejorar hay que subir el orden del filtro o la frecuencia del PWM (a costa de resolución).

**39.** ¿Por qué en el Timer1 conviene usar ICR1 como TOP para el PWM?

??? respuesta "Ver respuesta"
    Con ICR1 como TOP se escoge libremente el período del contador, y con él la resolución ($\log_2(TOP+1)$) y la frecuencia de la portadora, mientras OCR1A u OCR1B quedan libres para fijar el ciclo útil de cada muestra. Así se puede ajustar la frecuencia del PWM a la tasa de muestreo del sistema.

## 7. Sobremuestreo y sigma-delta

**40.** Un ADC de 8 bits se sobremuestrea 16 veces y luego se filtra y diezma. ¿Cuántos bits efectivos se ganan? ¿Qué condición debe cumplirse?

??? respuesta "Ver respuesta"
    La mejora es $10\log_{10}(16) \approx 12$ dB, unos 2 bits: la resolución efectiva queda cerca de 10 bits. Funciona solo si el error de cuantización se comporta como ruido no correlacionado con la señal. Si la señal es muy limpia y lenta, puede hacer falta agregar un poco de ruido (dither) para que el promedio gane resolución.

**41.** Escriba la relación entre la entrada, el ruido de cuantización y la salida de un modulador sigma-delta discreto de primer orden, e interprétela.

??? respuesta "Ver respuesta"

    $$Y(z) = z^{-1}X(z) + (1 - z^{-1})E(z)$$

    La señal pasa intacta, solo retrasada una muestra. El ruido de cuantización $E$ pasa por $1 - z^{-1}$, que es un pasaaltos con un cero en $z = 1$ (en DC): en bajas frecuencias el ruido casi desaparece y se concentra en altas frecuencias. Esa conformación del ruido es lo que permite que un filtro pasabajos posterior recupere la señal con mucha más resolución que la del cuantizador.

**42.** La entrada de un modulador sigma-delta de 1 bit con niveles ±1 vale 0,5 (constante). ¿Qué proporción de unos aparece en la salida?

??? respuesta "Ver respuesta"
    El promedio de la salida debe igualar la entrada: si $p$ es la proporción de +1, entonces $p\cdot(+1) + (1-p)\cdot(-1) = 0{,}5$, de donde $p = 0{,}75$. Tres de cada cuatro bits son +1. Un filtro pasabajos que promedie esa secuencia entrega 0,5.

**43.** ¿Qué ventaja tiene la codificación diferencial sobre cuantizar directamente la señal, y por qué el cuantizador se pone dentro de un lazo de realimentación?

??? respuesta "Ver respuesta"
    La señal de audio está muy correlacionada: una muestra se parece mucho a la anterior. La diferencia entre ellas tiene mucha menos varianza que la señal, así que con los mismos bits se cuantiza con menos error. Si el cuantizador estuviera fuera del lazo, el receptor acumularía (integraría) los errores de cuantización y la reconstrucción se iría alejando. Dentro del lazo, la predicción se hace con la señal ya cuantizada, igual que en el receptor, y los errores no se acumulan.

**44.** El micrófono digital INMP441 entrega audio de 24 bits por I2S. ¿Cómo logra esa resolución si internamente usa un cuantizador de muy pocos bits?

??? respuesta "Ver respuesta"
    Usa un modulador sigma-delta que trabaja a una tasa muy superior a la de salida (sobremuestreo) y conforma el ruido de cuantización hacia altas frecuencias. Un filtro digital interno de diezmado elimina ese ruido fuera de banda y baja la tasa hasta la del reloj WS, entregando muestras de muchos bits. Ese mismo filtro de diezmado actúa como antialias, así que el usuario no necesita un filtro analógico antes del micrófono.

## 8. Filtros digitales

**45.** Con $f_s = 8$ kHz, ¿a qué frecuencia digital $\omega$ corresponde 1 kHz? ¿Por qué basta estudiar la respuesta de un filtro digital entre 0 y $\pi$?

??? respuesta "Ver respuesta"
    $\omega = 2\pi\cdot 1000/8000 = \pi/4$ rad/muestra. La respuesta en frecuencia de un sistema discreto es periódica con período $2\pi$ (las frecuencias $f$ y $f + f_s$ dan las mismas muestras), y para coeficientes reales es simétrica: $\lvert H(e^{-j\omega})\rvert = \lvert H(e^{j\omega})\rvert$. Por eso toda la información está entre 0 y $\pi$, es decir entre 0 y $f_s/2$.

**46.** Analice el filtro $y[n] = 0{,}9\,y[n-1] + 0{,}1\,x[n]$: tipo, polo, estabilidad, ganancia en DC y comportamiento.

??? respuesta "Ver respuesta"
    Es un IIR de primer orden, $H(z) = 0{,}1/(1 - 0{,}9z^{-1})$, con un polo en $z = 0{,}9$, dentro del círculo unitario: estable. En DC ($z = 1$): $0{,}1/0{,}1 = 1$. En $f_s/2$ ($z = -1$): $0{,}1/1{,}9 \approx 0{,}05$. Es un pasabajos, el equivalente discreto de un RC, con una "constante de tiempo" de unas 10 muestras (la respuesta al impulso decae como $0{,}9^n$).

**47.** Para el promediador de 4 muestras $y[n] = \frac{1}{4}(x[n] + x[n-1] + x[n-2] + x[n-3])$, encuentre sus ceros y su retardo de grupo.

??? respuesta "Ver respuesta"
    $H(z) = \frac{1}{4}(1 + z^{-1} + z^{-2} + z^{-3})$. Las raíces de $1 + z + z^2 + z^3 = (1+z)(1+z^2)$ son $z = -1$ y $z = \pm j$: ceros en $f_s/2$ y en $f_s/4$. Es un pasabajos sencillo que anula esas dos frecuencias. Sus coeficientes son simétricos, así que tiene fase lineal con retardo $(4-1)/2 = 1{,}5$ muestras.

**48.** ¿Por qué un FIR simétrico con número **par** de coeficientes no puede usarse como pasaaltos?

??? respuesta "Ver respuesta"
    Con longitud par y simetría par, al evaluar $H(z)$ en $z = -1$ los términos se cancelan por parejas: $h[k](-1)^k$ y $h[M-1-k](-1)^{M-1-k}$ tienen signos opuestos porque $M - 1$ es impar. Por tanto $H(-1) = 0$ siempre: la ganancia en $f_s/2$ es cero. Un pasaaltos necesita ganancia máxima precisamente allí. Se usa entonces longitud impar o simetría impar con la estructura adecuada.

**49.** Un FIR de fase lineal con coeficientes reales tiene un cero en $z = 0{,}5\,e^{j\pi/3}$. ¿Qué otros ceros tiene obligatoriamente?

??? respuesta "Ver respuesta"
    Por coeficientes reales, el conjugado $0{,}5\,e^{-j\pi/3}$. Por fase lineal, los recíprocos de ambos: $2\,e^{j\pi/3}$ y $2\,e^{-j\pi/3}$. Son cuatro ceros que forman un grupo simétrico respecto al círculo unitario y al eje real.

**50.** Se necesita un FIR pasabajos con al menos 50 dB de atenuación y una transición de 500 Hz, con $f_s = 8$ kHz. ¿Qué ventana escogería y qué longitud aproximada?

??? respuesta "Ver respuesta"
    Hann da unos 44 dB: no alcanza. Hamming da unos 53 dB: sirve. Su transición es $\Delta f/f_s \approx 3{,}3/M$, así que $M \approx 3{,}3\cdot 8000/500 \approx 53$ coeficientes. Blackman también cumpliría, pero con una transición más ancha necesitaría unos 88 coeficientes. Kaiser permite ajustar exactamente la atenuación con $\beta$.

**51.** En el diseño FIR con ventana rectangular, ¿qué pasa con el rizado si se aumenta mucho la longitud $M$?

??? respuesta "Ver respuesta"
    La transición se hace más estrecha (proporcional a $1/M$), pero el pico del rizado junto al borde no baja: se queda cerca del 9 % (unos 21 dB de atenuación). Es el fenómeno de Gibbs: el rizado lo fija la forma de la ventana (sus lóbulos laterales), no su longitud. Para reducirlo hay que cambiar de ventana.

**52.** Diseñe un resonador digital con frecuencia central 1 kHz, $f_s = 8$ kHz y radio de polos $r = 0{,}95$. Escriba su denominador y estime su ancho de banda.

??? respuesta "Ver respuesta"
    Ángulo de los polos: $\theta = 2\pi\cdot 1000/8000 = \pi/4$. Denominador: $1 - 2r\cos\theta\,z^{-1} + r^2z^{-2} = 1 - 1{,}3435\,z^{-1} + 0{,}9025\,z^{-2}$. Ancho de banda aproximado: $(1 - r)f_s/\pi = 0{,}05\cdot 8000/\pi \approx 127$ Hz. Cuanto más cerca de 1 esté $r$, más estrecho y alto es el pico.

**53.** Proponga la ubicación de polos y ceros de un notch digital que elimine 60 Hz con $f_s = 1$ kHz.

??? respuesta "Ver respuesta"
    Ceros sobre el círculo unitario en $e^{\pm j\theta}$ con $\theta = 2\pi\cdot 60/1000 \approx 0{,}377$ rad (21,6°): anulan exactamente 60 Hz. Polos en el mismo ángulo con radio un poco menor que 1, por ejemplo $r = 0{,}95$, para que la muesca sea estrecha y la ganancia vuelva a 1 lejos de 60 Hz. Numerador $1 - 2\cos\theta\,z^{-1} + z^{-2} \approx 1 - 1{,}860\,z^{-1} + z^{-2}$; el denominador es igual con $r$ y $r^2$.

**54.** ¿Qué ventaja tiene implementar un IIR de orden 8 como cascada de cuatro secciones de segundo orden en lugar de en forma directa?

??? respuesta "Ver respuesta"
    En forma directa, cada polo depende de los ocho coeficientes del denominador, y un error mínimo de cuantización en uno de ellos puede mover mucho los polos (incluso sacarlos del círculo unitario). En cascada, cada par de polos depende solo de dos coeficientes, así que la sensibilidad es mucho menor. Además cada sección se puede escalar para evitar desbordes y verificar por separado.

**55.** Un FIR de fase lineal tiene 101 coeficientes. ¿Cuántas multiplicaciones por muestra necesita en forma directa y en forma plegada (aprovechando la simetría)?

??? respuesta "Ver respuesta"
    Forma directa: 101 multiplicaciones. Forma plegada: se suman primero las 50 parejas de muestras que comparten coeficiente y se multiplica cada suma una vez, más el coeficiente central: 51 multiplicaciones. Las sumas siguen siendo unas 100.

## 9. Implementación en microcontrolador

**56.** ¿Por qué un FIR en un microcontrolador usa un buffer circular en lugar de desplazar todo el arreglo de muestras en cada instante?

??? respuesta "Ver respuesta"
    Desplazar el arreglo exige copiar $M-1$ valores por cada muestra nueva, un trabajo inútil que crece con la longitud del filtro. Con un buffer circular, la muestra nueva sobrescribe la más antigua y un índice que da la vuelta indica dónde empieza la historia. La memoria es la misma y se evitan todas las copias.

**57.** Un FIR tiene coeficientes enteros escalados por $2^7$ que suman 128, y la entrada es la lectura de un ADC de 10 bits sin signo (0 a 1023). ¿Qué corrimiento lleva la salida, qué pasa con el nivel DC de 512 y qué tipo debe tener el acumulador?

??? respuesta "Ver respuesta"
    La salida se corre `>> 7`, porque los coeficientes tienen $F = 7$. Como la suma de los coeficientes es $2^7$, la ganancia DC es 1: un nivel constante de 512 sale como 512 después del transitorio. El acumulador debe ser de 32 bits (`int32_t`/`long`): la suma de los coeficientes en valor absoluto es al menos 128, así que con una entrada de 1023 el acumulador llega por lo menos a $1023\cdot 128 \approx 131\,000$, muy por encima de los 32 767 que caben en un `int` de 16 bits.

**58.** ¿Por qué es más delicado implementar un IIR en punto fijo que un FIR?

??? respuesta "Ver respuesta"
    En el IIR la salida se realimenta: los errores de redondeo vuelven a entrar y se acumulan, pueden aparecer oscilaciones pequeñas permanentes (ciclos límite) y los estados pueden desbordarse. Además, cuantizar los coeficientes del denominador mueve los polos, y si quedan cerca del círculo unitario pueden salir de él y volver el filtro inestable. Un FIR no tiene realimentación: el error no se acumula y nunca se vuelve inestable.

**59.** MATLAB entrega una sección SOS como $[b_0\ b_1\ b_2\ a_0\ a_1\ a_2]$ con una ganancia $g$. ¿Qué dos cosas hay que verificar antes de pasar esos números a un código en C?

??? respuesta "Ver respuesta"
    Primero, con qué signo entran $a_1$ y $a_2$ en la ecuación que implementa el código: MATLAB los entrega como en $A(z) = 1 + a_1z^{-1} + a_2z^{-2}$, así que la ecuación en diferencias los resta. Si el código ya tiene el signo menos, se copian tal cual. Segundo, dónde se aplica la ganancia $g$: a la entrada o a la salida de la sección. Ambas cosas se ven en *Show filter structure* y se verifican comparando la respuesta al impulso del código con la de MATLAB.

**60.** ¿Cómo comprobaría que la implementación de un filtro en el Arduino es correcta?

??? respuesta "Ver respuesta"
    Aplicando entradas conocidas y comparando muestra a muestra con la simulación: un impulso (debe reproducir los coeficientes en un FIR), un escalón (debe llegar a la ganancia DC) y cosenos de varias frecuencias (deben salir con la amplitud que indica $\lvert H\rvert$). Si hay diferencias, se revisan casting, corrimientos, signos y el manejo del buffer. También se mide el tiempo de ejecución con `micros()` para confirmar que cabe en el período de muestreo.

## 10. Punto fijo

**61.** Un formato sin signo tiene $W = 6$ y $F = 2$. ¿Cuál es su rango y su LSB? ¿Qué número representa el entero 45?

??? respuesta "Ver respuesta"
    LSB $= 2^{-2} = 0{,}25$. Rango: de 0 a $(2^6 - 1)/4 = 63/4 = 15{,}75$. El entero 45 representa $45/4 = 11{,}25$ (en binario $1011.01_2$).

**62.** Para un formato con signo de $W = 12$ y $F = 8$, ¿cuántos bits enteros $QI$ tiene, cuál es su rango y su LSB?

??? respuesta "Ver respuesta"
    $QI = 12 - 1 - 8 = 3$: es Q3.8. LSB $= 2^{-8} \approx 0{,}0039$. Rango: de $-2^{11}/2^8 = -8$ hasta $(2^{11}-1)/2^8 \approx 7{,}996$.

**63.** Codifique $x = -0{,}4$ en un formato con signo de $W = 8$ y $F = 6$, redondeando al más cercano. ¿Qué entero y qué palabra binaria se guardan, y qué valor representan?

??? respuesta "Ver respuesta"
    $-0{,}4\cdot 2^6 = -25{,}6 \to r = -26$. En complemento a dos de 8 bits: $256 - 26 = 230 = 11100110_2$, que con $F = 6$ se lee $11.100110_2$. Representa $-26/64 = -0{,}40625$, con un error de −0,00625.

**64.** Se multiplica un número con signo $(12, 8)$ por otro con signo $(10, 9)$, y luego se acumulan 100 de esos productos. ¿Qué formatos tienen el producto y el acumulador?

??? respuesta "Ver respuesta"
    Producto: $W = 12 + 10 = 22$ y $F = 8 + 9 = 17$, es decir $(22, 17)$. Acumulador: se añaden $\lceil\log_2 100\rceil = 7$ bits de guarda, así que $(29, 17)$. Cabe en un `int32_t`.

**65.** En un filtro de audio, ¿qué política de overflow es preferible, saturación o wrap? ¿Por qué?

??? respuesta "Ver respuesta"
    Saturación. Si la salida se pasa del máximo, la saturación la recorta al valor extremo: hay distorsión, pero el error es acotado. Con wrap, un valor positivo grande se convierte en uno negativo grande, un salto de casi toda la escala que se oye como un chasquido fuerte. La excepción son sumas intermedias en complemento a dos que al final vuelven al rango: allí el wrap no causa error en el resultado final.

**66.** ¿Por qué redondear siempre hacia abajo (truncar en complemento a dos) introduce un error sistemático, y cómo se evita?

??? respuesta "Ver respuesta"
    Hacia abajo, el error siempre es negativo, entre −1 LSB y 0, con promedio −LSB/2: es un sesgo, un pequeño nivel DC que en un filtro se acumula y en un IIR puede crecer. Redondeando al más cercano, el error queda entre −LSB/2 y +LSB/2 con promedio cero. En código se logra sumando la mitad del LSB de salida antes del corrimiento: `(acc + (1 << (s - 1))) >> s`.

**67.** ¿Por qué no conviene escribir código de procesamiento suponiendo que `int` tiene 32 bits? ¿Qué se usa en su lugar?

??? respuesta "Ver respuesta"
    El estándar de C solo garantiza un mínimo para `int`: en el Arduino UNO es de 16 bits y en un PC o en la Pico es de 32. Un código que suma productos en `int` funciona en el PC y se desborda en el UNO. Se usan los tipos de ancho fijo de `<stdint.h>` (`int16_t`, `int32_t`, `int64_t`), y si hace falta se verifica con `static_assert(sizeof(int32_t) == 4, ...)`, recordando que `sizeof` cuenta bytes.

## 11. Análisis espectral y THD (OPCIONAL)

!!! nota "Tema opcional"
    Este tema complementa el curso, pero **no entra en el examen final**. El examen cubre hasta el tema 10.

**68.** Con $f_s = 8$ kHz y $N = 1024$, ¿cuál es la resolución en frecuencia, cuánto dura la ventana y en qué bin aparece un tono de 1 kHz?

??? respuesta "Ver respuesta"
    $\Delta f = 8000/1024 = 7{,}8125$ Hz. La ventana dura $1024/8000 = 128$ ms. El tono de 1 kHz cae en $k = 1000/7{,}8125 = 128$, exactamente un bin.

**69.** En la situación anterior, ¿qué se ve si el tono es de 1004 Hz con ventana rectangular? ¿Y con ventana Hann?

??? respuesta "Ver respuesta"
    1004 Hz equivale a $k \approx 128{,}5$: cae entre dos bins. El bloque no contiene un número entero de ciclos y hay leakage. Con ventana rectangular el pico se reparte entre los bins 128 y 129 y aparecen lóbulos laterales altos (desde −13 dB) que se extienden por todo el espectro. Con Hann los lóbulos laterales bajan a −31 dB y caen rápido, así que el espectro lejos del tono queda limpio, a cambio de un pico un poco más ancho.

**70.** Con ventana Hann, un tono a escala completa aparece con una amplitud de 0,5 en lugar de 1 si se usa $2\lvert X[k]\rvert/N$. ¿Por qué, y cómo se corrige?

??? respuesta "Ver respuesta"
    La ventana Hann multiplica la señal por valores entre 0 y 1 cuyo promedio es 0,5: se pierde la mitad de la amplitud (ganancia coherente). Se corrige dividiendo por el promedio de la ventana: $A_k = 2\lvert X[k]\rvert/(N\bar{w})$ con $\bar{w} = 0{,}5$. Para Hamming $\bar{w} = 0{,}54$.

**71.** Una tensión tiene fundamental de 2 V, segundo armónico de 0,1 V y tercero de 0,2 V. ¿Cuál es su THD?

??? respuesta "Ver respuesta"
    $THD = 100\cdot\sqrt{0{,}1^2 + 0{,}2^2}/2 = 100\cdot\sqrt{0{,}05}/2 \approx 11{,}2\,\%$. Los armónicos se suman en potencia (raíz de la suma de cuadrados), no en amplitud.

**72.** Al medir THD en la red de 60 Hz se recomienda capturar un número entero de ciclos (por ejemplo 10). ¿Por qué?

??? respuesta "Ver respuesta"
    Si el bloque contiene un número entero de ciclos de la fundamental, la fundamental y todos sus armónicos caen exactamente en bins de la DFT ($\Delta f$ es divisor de 60 Hz) y no hay leakage: cada armónico se lee en un solo bin. Así la medida es más exacta y los armónicos pequeños no quedan tapados por las fugas de la fundamental. Como en la práctica la frecuencia de la red varía un poco, se combina con una ventana.

**73.** ¿Cuántas operaciones aproximadas ahorra la FFT frente a la DFT directa para $N = 1024$?

??? respuesta "Ver respuesta"
    DFT directa: $N^2 \approx 1{,}05$ millones de multiplicaciones complejas. FFT: del orden de $N\log_2N = 1024\cdot 10 \approx 10\,240$. Es unas 100 veces menos, y la ventaja crece con $N$.

## 12. Señales aleatorias y Wiener (OPCIONAL)

!!! nota "Tema opcional"
    Este tema complementa el curso, pero **no entra en el examen final**. El examen cubre hasta el tema 10.

**74.** ¿Qué significa que un proceso aleatorio sea estacionario en sentido amplio? Dé un ejemplo de una señal que no lo sea.

??? respuesta "Ver respuesta"
    Su media es constante en el tiempo y su autocorrelación $E[x(n)x(n-m)]$ depende solo del desfase $m$, no del instante $n$. El ruido térmico de una resistencia a temperatura constante lo es. Una frase hablada no lo es: su potencia y su espectro cambian de una sílaba a otra (por eso se analiza con ventanas cortas, donde se puede suponer estacionaria).

**75.** ¿Cómo son la autocorrelación y la densidad espectral de potencia del ruido blanco?

??? respuesta "Ver respuesta"
    La autocorrelación es un impulso, $\gamma(m) = \sigma^2\delta(m)$: muestras distintas no están correlacionadas. Por Wiener-Khinchin, su densidad espectral es la transformada de esa autocorrelación: una constante, $\sigma^2$ en todas las frecuencias. "Blanco" alude a que contiene todas las frecuencias por igual, como la luz blanca.

**76.** ¿Qué información estadística se necesita para calcular un filtro de Wiener FIR, y por qué su sistema de ecuaciones se puede resolver eficientemente?

??? respuesta "Ver respuesta"
    Se necesitan la autocorrelación de la entrada, $\gamma_{xx}(m)$, para $m = 0, \dots, M-1$, y la correlación cruzada entre la señal deseada y la entrada, $\gamma_{dx}(l)$. Con ellas se plantean las ecuaciones de Wiener-Hopf, $\Gamma_M\mathbf{h} = \boldsymbol{\gamma}_d$. La matriz $\Gamma_M$ es Toeplitz (sus diagonales son constantes) y hermitiana, y por eso se puede resolver con el algoritmo de Levinson-Durbin sin invertirla de forma general.

**77.** ¿Es lo mismo que dos variables aleatorias no estén correlacionadas que sean independientes?

??? respuesta "Ver respuesta"
    No. Independencia ($f(x,y) = g(x)h(y)$) implica no correlación, pero no al revés. Ejemplo: si $X$ es uniforme entre −1 y 1 y $Y = X^2$, la covarianza es cero ($E[X^3] = 0$), pero $Y$ depende totalmente de $X$. La no correlación solo dice que no hay relación lineal. Para variables gaussianas conjuntas, en cambio, las dos cosas sí coinciden.
