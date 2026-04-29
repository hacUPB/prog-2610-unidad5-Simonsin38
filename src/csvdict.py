import csv
with open(".\\Archivos\\Libro1.csv", "r") as file:
    lector = csv.DictReader(file, delimiter = ";")
    for fila in lector:
        modelo = fila["Modelo"]
        peso = fila["Peso"]
        print(f"El avión {modelo} pesa {peso}kg")
