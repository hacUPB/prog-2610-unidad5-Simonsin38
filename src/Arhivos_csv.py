import csv
peso_total = 0
with open(".\\Archivos\\Libro1.csv", "r") as csvfile:
    lector = csv.reader(csvfile, delimiter = ";")
    encabezado = next(lector)
    for fila in lector:
        peso_total += int(fila[4])
        print(fila[4])
print(f"{peso_total}kg")