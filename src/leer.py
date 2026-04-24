fp = open(".\\Información\\Ejercicio1.txt", "r", encoding ="utf-8")
datos_1 = fp.readlines()
print("Primera Lectura: ", datos_1[0])

datos_2 = fp.read()
print("Segunda lectura: ", datos_2)
fp.close()