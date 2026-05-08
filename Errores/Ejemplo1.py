try:
    valor = int(input("Ingrese un valor numérico: "))
    resultado = 10 / valor
except ValueError:
    print("El valor ingresado no es un número.")
except ZeroDivisionError:
    print("El valor ingresado no puede ser 0.")
else:
    print(f"Resultado = {resultado}")
finally:
    print("Hola")



