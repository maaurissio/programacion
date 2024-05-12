# Crear un programa que permita ver la lista de números enteros desde A hasta B ingresados por el
# usuario, validando que A sea menor a B.
from os import system
system("cls")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a < b:
    for i in range(a,b+1):
        print(i)
else:
    print("El primer numero es menor que el segundo")