import os

# Configuración
BASE_DIR = "../../../facultad/TDA/docs/guias"  # Ruta local donde se encuentran las guías
ARCHIVO_SALIDA = "tda.html"
CARPETAS = {
    "grafos": "Introducción a Grafos",
    "bt_pd": "Backtracking, Programación Dinámica",
    "greedy": "Greedy",
    "bfs-dijkstra-agm": "BFS, Dijkstra, AGM",
    "dyc": "Divide and Conquer",
    "flujos": "Flujos"

}

head_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TDA - Ejercicios</title>
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
        .materia {
            margin: 1.5rem 0;
        }
        .materia-titulo {
            font-weight: 500;
            color: #2c3e50;
            margin-bottom: 1rem;
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
    <h1>Técnicas de Diseño de Algoritmos</h1>
"""

footer_html = """<a href="index.html" class="volver">← Volver a materias</a>
</body>
</html>"""

def obtener_archivos_locales(carpeta):
    dir_path = os.path.join(BASE_DIR, carpeta)
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return os.listdir(dir_path)
    else:
        print(f"No se pudo acceder a la carpeta local: {carpeta}")
        return []

def generar_html():
    partes = [head_html]

    for carpeta, titulo in CARPETAS.items():
        partes.append(f'<div class="materia">')
        partes.append(f'    <div class="materia-titulo">{titulo}</div>')

        subcarpetas = obtener_archivos_locales(carpeta)
        
        subcarpetas = sorted([s for s in subcarpetas if s.isdigit() and "unfinished" not in s], key=int)
        
        for subcarpeta in subcarpetas:
            subcarpeta_path = os.path.join(BASE_DIR, carpeta, subcarpeta)
            
            ejercicios = obtener_archivos_locales(os.path.join(carpeta, subcarpeta))
            
            ejercicios = [e for e in ejercicios if e.endswith('.html')]
            
            ejercicios = sorted(ejercicios, key=lambda e: int(e.replace('.html', '')))

            for ejercicio in ejercicios:
                ejercicio_path = os.path.join(subcarpeta_path, ejercicio)
                if os.path.isfile(ejercicio_path):
                    url = f"https://beekkles.github.io/TDA/guias/{carpeta}/{subcarpeta}/{ejercicio}"
                    nombre = ejercicio.replace('.html', '')
                    partes.append(f'    <div class="item"><a href="{url}">Ejercicio {nombre}</a></div>')

        partes.append(f'</div>')

    partes.append(footer_html)

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(partes))
    print(f"Archivo generado: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    generar_html()
