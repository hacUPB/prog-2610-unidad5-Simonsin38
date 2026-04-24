from pathlib import Path

# Construimos una ruta hacia una carpeta específica
ruta_carpeta = Path("mis_documentos/finanzas")
# Creamos la carpeta si no existe
ruta_carpeta.mkdir(parents=True, exist_ok=True)

# Apuntamos a un archivo dentro de esa carpeta
ruta_archivo = ruta_carpeta / "reporte.txt"

with open(ruta_archivo, "a", encoding = "utf-8") as f:
    f.write("\n Hoy es un buen día.")