'''

1. Leer el nuevo archivo
2. Leer todo el archivo en forma de lista
3. Imprimir la primera letra de cada línea

'''

ej = open(".\\Información\\Texto_Aleatorio.txt", "r", encoding ="utf-8")
lista = ej.readlines()
ej.close()
print(lista)
for i in lista:
    print(i[0])



