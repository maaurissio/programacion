# Diseñar un programa que lea N números enteros y determine el promedio de ellos.

from os import system
system("cls")

a = int(input("Ingrese cuantos números quiere ingresar: "))

for i in range (a):
    num = int(input("Ingrese un número: "))
print(f"El promedio entre tus números es: {num//a}")