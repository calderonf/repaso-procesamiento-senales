#!/usr/bin/env python3
"""Genera las páginas HTML del sitio a partir de los archivos Markdown de contenido/.

Uso:
    pip install markdown pymdown-extensions
    python build.py

Las páginas generadas (index.html, resumen.html, preguntas.html) quedan en la
raíz del repositorio, que es lo que publica GitHub Pages.
"""

import html
import re
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent
CONTENIDO = RAIZ / "contenido"
PLANTILLA = (RAIZ / "assets" / "plantilla.html").read_text(encoding="utf-8")

PAGINAS = [
    # (archivo de entrada, archivo de salida, texto del menú, mostrar índice lateral)
    ("index.md", "index.html", "Inicio", False),
    ("resumen.md", "resumen.html", "Resumen", True),
    ("preguntas.md", "preguntas.html", "Preguntas", True),
]

EXTENSIONES = [
    "tables",
    "admonition",
    "attr_list",
    "md_in_html",
    "toc",
    "pymdownx.details",
    "pymdownx.superfences",
    "pymdownx.arithmatex",
]

CONFIG = {
    "toc": {"toc_depth": "2-3"},
    "pymdownx.arithmatex": {"generic": True},
}


def menu(activa):
    enlaces = []
    for _, salida, texto, _ in PAGINAS:
        clase = ' class="activo" aria-current="page"' if salida == activa else ""
        enlaces.append(f'<a href="{salida}"{clase}>{texto}</a>')
    return "\n        ".join(enlaces)


def numerar_respuestas(cuerpo):
    """Agrega un número a cada desplegable para poder enlazarlo."""
    contador = 0

    def reemplazo(m):
        nonlocal contador
        contador += 1
        return f'<details class="respuesta" id="r{contador}">'

    return re.sub(r'<details class="respuesta">', reemplazo, cuerpo), contador


def insertar_tras_intro(cuerpo, bloque):
    """Ubica los botones después del primer párrafo que sigue al título."""
    if not bloque:
        return cuerpo
    fin_titulo = cuerpo.find("</h1>")
    fin_parrafo = cuerpo.find("</p>", fin_titulo)
    if fin_titulo < 0 or fin_parrafo < 0:
        return bloque + cuerpo
    corte = fin_parrafo + len("</p>")
    return cuerpo[:corte] + bloque + cuerpo[corte:]


def construir():
    for entrada, salida, texto, con_indice in PAGINAS:
        md = markdown.Markdown(extensions=EXTENSIONES, extension_configs=CONFIG)
        fuente = (CONTENIDO / entrada).read_text(encoding="utf-8")
        cuerpo = md.convert(fuente)
        cuerpo, n_respuestas = numerar_respuestas(cuerpo)

        titulo = re.search(r"^# (.+)$", fuente, re.MULTILINE).group(1).strip()
        indice = ""
        if con_indice:
            indice = (
                '<nav class="indice" aria-label="Contenido de la página">'
                '<p class="indice-titulo">En esta página</p>'
                f"{md.toc}</nav>"
            )
        herramientas = ""
        if n_respuestas:
            herramientas = (
                '<div class="herramientas">'
                '<button type="button" id="abrir-todas">Mostrar todas las respuestas</button>'
                '<button type="button" id="cerrar-todas">Ocultar todas</button>'
                "</div>"
            )

        pagina = (
            PLANTILLA.replace("{{titulo}}", html.escape(titulo))
            .replace("{{menu}}", menu(salida))
            .replace("{{indice}}", indice)
            .replace("{{herramientas}}", "")
            .replace("{{contenido}}", insertar_tras_intro(cuerpo, herramientas))
            .replace("{{clase}}", "con-indice" if con_indice else "sin-indice")
        )
        (RAIZ / salida).write_text(pagina, encoding="utf-8")
        print(f"{salida}: {len(pagina) // 1024} KB, {n_respuestas} respuestas")


if __name__ == "__main__":
    construir()
