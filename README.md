# Repaso para el examen final – Procesamiento de Señales

Sitio web de estudio para el curso de Procesamiento de Señales. Tiene tres páginas:

- **Inicio** (`index.html`): presentación y forma de estudiar.
- **Resumen** (`resumen.html`): la teoría del curso resumida por unidades, con una tabla final de fórmulas clave.
- **Preguntas** (`preguntas.html`): 77 preguntas abiertas con la respuesta explicada en un desplegable.

Las fórmulas se muestran con MathJax, que se carga desde internet, así que el sitio necesita conexión para verlas bien.

## Publicar en GitHub Pages

1. Cree un repositorio nuevo en GitHub, por ejemplo `repaso-procesamiento-senales`. Puede ser público o, si su cuenta lo permite, privado con Pages.
2. Suba **todo** el contenido de esta carpeta a la raíz del repositorio, incluido el archivo oculto `.nojekyll`. Desde la terminal:

   ```bash
   git init
   git add .
   git commit -m "Material de repaso"
   git branch -M main
   git remote add origin https://github.com/<usuario>/repaso-procesamiento-senales.git
   git push -u origin main
   ```

   También puede arrastrar los archivos en la página del repositorio (*Add file → Upload files*). En ese caso cree `.nojekyll` a mano con *Add file → Create new file*, vacío.
3. En el repositorio vaya a **Settings → Pages**. En *Build and deployment* escoja *Deploy from a branch*, la rama `main` y la carpeta `/ (root)`. Guarde.
4. En uno o dos minutos el sitio queda en `https://<usuario>.github.io/repaso-procesamiento-senales/`.

## Modificar el contenido

El texto está en Markdown en la carpeta `contenido/`:

| Archivo | Página |
| --- | --- |
| `contenido/index.md` | Inicio |
| `contenido/resumen.md` | Resumen |
| `contenido/preguntas.md` | Preguntas |

Después de editar, regenere las páginas HTML y suba los cambios:

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
└── .nojekyll                                   le indica a GitHub Pages que publique los HTML tal cual
```

Al imprimir la página de preguntas (o guardarla como PDF) todas las respuestas salen abiertas.
