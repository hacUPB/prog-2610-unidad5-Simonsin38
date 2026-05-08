from pathlib import Path
n = 0
e = True
print("¿Desea ingresar una ruta personalizada o entrar al directorio por defecto?")
while n == 0:
   opcion = input("Ingrese 'p' para una personalizada o 'd' para la ruta por defecto: ")
   while e == True:
    if opcion == "p":
       ruta = Path(input("Ingrese la ruta usando doble backslash: "))
       if ruta.exists():
          
    elif opcion == "d":
       ruta = Path(".\\Reto\\Archivos")
        

       
       

    
ruta = input("Ingrese la ruta de la carpeta separada por doble backslash: ")
perro = Path(ruta)


with open(perro, "r") as file:
    paco = file.read()
print(paco)
    
     