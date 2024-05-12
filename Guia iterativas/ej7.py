# Hacer un programa para calcular el valor de la suma de los N primeros enteros. Por ejemplo si N es
# 5 la suma es 15 ( 1 + 2 + 3 + 4 + 5 = 15)

from os import system
system("cls")

n = int(input("Ingrese un número: "))
suma = 0
for i in range(n + 1):
    suma += i

print(n) 
print(suma)