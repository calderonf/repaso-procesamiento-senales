# Repaso para el examen final

Material de estudio de **Procesamiento de Señales**. Aquí encuentra un resumen de la teoría de todo el curso y un banco de preguntas abiertas con la respuesta escondida, para practicar antes del examen.

<div class="tarjetas" markdown="1">

<a class="tarjeta" href="resumen.html" markdown="1">
<span class="tarjeta-titulo">Resumen teórico</span>
<span class="tarjeta-texto">Las ideas y fórmulas de cada unidad: filtros analógicos, muestreo, conversión A/D y D/A, sigma-delta, filtros digitales, punto fijo, FFT y Wiener.</span>
</a>

<a class="tarjeta" href="preguntas.html" markdown="1">
<span class="tarjeta-titulo">Banco de preguntas</span>
<span class="tarjeta-texto">77 preguntas conceptuales y de cálculo, organizadas por tema. Cada una tiene su respuesta explicada en un desplegable.</span>
</a>

</div>

## Cómo estudiar

1. Lea una sección del resumen y trate de explicarla en voz alta sin mirar.
2. Vaya a las preguntas del mismo tema y respóndalas por escrito **antes** de abrir la respuesta.
3. Compare su respuesta con la explicación. Si falló, vuelva al resumen y repita la pregunta al día siguiente.
4. Las preguntas de cálculo se pueden resolver a mano: practíquelas sin calculadora cuando sea posible.

## Temas del curso

| Unidad | Temas |
| --- | --- |
| Filtros analógicos | Respuesta en frecuencia y Bode; voz, ruido y pre/de-énfasis; Butterworth, Chebyshev, elíptico y Bessel; sistemas de segundo orden; Sallen-Key, MFB y biquad; transformaciones de frecuencia; ruido térmico |
| Conversión A/D y D/A | Muestreo y aliasing; muestreo pasabanda; sample and hold; filtro antialias; cuantización y SNR; ADC, temporizadores e interrupciones del ATmega328P; D/A con PWM |
| Sobremuestreo | Sobremuestreo directo; codificación diferencial; modulación sigma-delta |
| Filtros digitales | Ecuaciones en diferencias y transformada Z; FIR, fase lineal y diseño por ventanas; IIR, polos y ceros, estabilidad y osciladores; estructuras de realización; implementación en C |
| Punto fijo | Formatos con y sin signo; notación Q; redondeo y overflow; tamaños de producto y acumulador; normalización y ganancia DC |
| Análisis espectral | DFT y FFT; leakage y ventanas; medición de THD |
| Filtrado óptimo | Procesos aleatorios, autocorrelación y densidad espectral; filtro de Wiener |
