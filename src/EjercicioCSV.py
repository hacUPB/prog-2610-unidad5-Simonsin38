import csv
edadtot = 0
contador_edad = 0
with open(".\\Archivos\\EjercicioCSV.csv", "r") as file:
    lector = csv.reader(file, delimiter = ";")
    encabezado = next(lector)
    for edad in lector:
            edadtot += int(edad[1])
            contador_edad += 1
    edadprom = edadtot / contador_edad
    diclector = csv.DictReader(file, delimiter = ";")
    for disionario in diclector:
          print(disionario)
print(f"La edad promedio del grupo de personas es de aproximadamente {round(edadprom)} años")
    