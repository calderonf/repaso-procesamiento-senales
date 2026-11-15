# Repaso para el examen final – Procesamiento de Señales

**Sitio publicado: https://calderonf.github.io/repaso-procesamiento-senales/**

Sitio web de estudio para el curso de Procesamiento de Señales. Tiene tres páginas:

| Página | Enlace | Contenido |
| --- | --- | --- |
| Inicio | [index.html](https://calderonf.github.io/repaso-procesamiento-senales/) | Presentación y forma de estudiar |
| Resumen | [resumen.html](https://calderonf.github.io/repaso-procesamiento-senales/resumen.html) | La teoría del curso resumida por unidades, con una tabla final de fórmulas clave |
| Preguntas | [preguntas.html](https://calderonf.github.io/repaso-procesamiento-senales/preguntas.html) | 77 preguntas abiertas con la respuesta explicada en un desplegable |

Las fórmulas se muestran con MathJax, que se carga desde internet, así que el sitio necesita conexión para verlas bien.

## Publicación

El sitio se publica con GitHub Pages desde la rama `main`, carpeta `/ (root)` (*Settings → Pages*). El archivo vacío `.nojekyll` le indica a GitHub que publique los HTML tal cual, sin procesarlos con Jekyll; no lo borre. Cada `git push` a `main` actualiza el sitio en uno o dos minutos.

## Modificar el contenido

El texto está en Markdown en la carpeta `contenido/`:

| Archivo | Página |
| --- | --- |
| `contenido/index.md` | Inicio |
| `contenido/resumen.md` | Resumen |
| `contenido/preguntas.md` | Preguntas |

Las páginas HTML de la raíz se generan a partir de esos archivos: no las edite a mano, porque `build.py` las sobrescribe. Después de editar, regenere las páginas y suba los cambios:

```bash
pip install markdown pymdown-extensions
python build.py
git add . && git commit -m "Actualiza material" && git push
```

### Formato de una pregunta

```markdown
**78.** Texto de la pregunta, con fórmulas como $f_s = 2B$.

??? respuesta "Ver respuesta"
    Texto de la respuesta, con cuatro espacios de sangría.

    Una fórmula centrada va sola en su línea, con una línea en blanco antes y después:

    $$H(z) = \frac{1}{1 - 0{,}9z^{-1}}$$
```

- `$...$` es una fórmula dentro del texto y `$$...$$` una fórmula centrada.
- Dentro de una tabla no use `|x|` para el valor absoluto, porque la barra separa columnas: escriba `\lvert x\rvert`.
- En una lista, las fórmulas centradas deben tener cuatro espacios de sangría.

## Estructura

```text
.
├── index.html, resumen.html, preguntas.html   páginas generadas (las que publica GitHub Pages)
├── contenido/                                  textos en Markdown (lo que se edita)
├── assets/estilo.css                           estilos (incluye modo oscuro e impresión)
├── assets/sitio.js                             botones para abrir y cerrar todas las respuestas
├── assets/plantilla.html                       plantilla común de las páginas
├── build.py                                    convierte Markdown en HTML
├── .nojekyll                                   le indica a GitHub Pages que publique los HTML tal cual
└── LICENSE                                     licencia CC0 1.0
```

Al imprimir la página de preguntas (o guardarla como PDF) todas las respuestas salen abiertas.

## Licencia

El contenido se publica bajo [CC0 1.0 Universal](LICENSE): cualquiera puede copiarlo, modificarlo y redistribuirlo sin pedir permiso.
