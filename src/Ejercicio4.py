nombre_archivo = input("Nombra tu nuevo archivo (ej: diario): ")

# Contexto de escritura
with open(f".\\Información\\{nombre_archivo}.txt", 'w+', encoding = "uft-8") as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0)
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())
#  Contexto de lectura
# with open(".\\Información\\" + nombre_archivo + ".txt", 'r') as archivo:
#     print("\n--- Leyendo tu archivo ---")
#     print(archivo.read())