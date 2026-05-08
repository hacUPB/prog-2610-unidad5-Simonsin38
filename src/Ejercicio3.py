from random import randint
from collections import Counter

def moda(lista):
    return Counter(lista).most_common(1)[0][0]

lista = []
for i in range(50):
    lista.append(randint(0, 100))

maximo = str(max(lista))
minimo = str(min(lista))
prom = str(sum(lista)/len(lista))
modaa = str(moda(lista))


file_datos = open(".\\Información\\datos.txt", "a", encoding ="utf-8")
file_datos.write("\nEl valor máximo es: " + maximo + "\n")
file_datos.write("El valor mínimo es: " + minimo + "\n")
file_datos.write("El promedio es: " + prom + "\n")
file_datos.write("La moda es: " + modaa + "\n")
file_datos.write(f"Tu lista es: {lista} \n")
file_datos.close()
print("\n Archivo creado con éxito. Revisa tu carpeta.\n")