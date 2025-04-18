import requests
import json

# Configuración
BASE_URL = "https://api.github.com/repos/beekkles/TDA/contents/docs/guias"
ARCHIVO_SALIDA = "tda.html"
CARPETAS = {
    "grafos": "Introducción a Grafos",
    "bt_pd_greedy": "Backtracking, Programación Dinámica y Greedy"
}

head_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TDA - Guías</title>
    <style>
        body {
            font-family: 'Helvetica Neue', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: #fafafa;
            color: #333;
            line-height: 1.5;
        }
        h1 {
            text-align: center;
            font-weight: 300;
            margin-bottom: 2rem;
            color: #444;
        }
        .guia {
            margin: 1.5rem 0;
            padding-left: 1rem;
            border-left: 2px solid #3498db;
        }
        .guia-titulo {
            font-weight: 500;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        .item {
            margin: 0.3rem 0;
            padding-left: 1rem;
        }
        .item a {
            color: #2980b9;
            text-decoration: none;
        }
        .item a:hover {
            text-decoration: underline;
        }
        .volver {
            display: block;
            text-align: center;
            margin-top: 2rem;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <h1>Algoritmos y Estructuras de Datos III</h1>
"""

footer_html = """<a href="index.html" class="volver">← Volver a materias</a>
</body>
</html>"""

# Función para obtener archivos de GitHub usando la API
def obtener_archivos_github(carpeta):
    url = f"{BASE_URL}/{carpeta}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"No se pudo acceder a la carpeta: {carpeta}")
        return []

# Función para generar el HTML
def generar_html():
    partes = [head_html]

    for carpeta, titulo in CARPETAS.items():
        partes.append(f'<div class="materia">')
        partes.append(f'    <div class="materia-titulo">{titulo}</div>')

        guias = obtener_archivos_github(carpeta)
        for guia in guias:
            if guia['type'] == 'dir':  # Si es una carpeta (guía)
                ejercicios = obtener_archivos_github(f"{carpeta}/{guia['name']}")
                if not ejercicios:
                    continue

                partes.append(f'    <div class="guia">')
                partes.append(f'        <div class="guia-titulo">Guía {guia["name"].zfill(2)}</div>')

                for ejercicio in ejercicios:
                    if ejercicio['name'].endswith('.html'):
                        url = ejercicio['html_url']
                        nombre = ejercicio['name'].replace('.html', '')
                        partes.append(f'        <div class="item"><a href="{url}">Ejercicio {nombre}</a></div>')

                partes.append(f'    </div>')

        partes.append(f'</div>')

    partes.append(footer_html)

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(partes))
    print(f"Archivo generado: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    generar_html()
