# 9. Crear un programa que lea varios dígitos hasta que se ingrese un cero. Luego imprimir:
# a. La cantidad de pares
# b. Promedio de impares
# c. El mayor de todos los dígitos

from os import system
system("cls")

par = 0
impar = 0
num_ing = 0
total = []
n = int(input("Ingrese un número para continuar o ingrese 0 para cancelar: \n"))

while n != 0:
    n = int(input("Ingrese un número o ingrese 0 para salir: \n"))
    if n % 2 == 0:
        par += 1
        total.append(n)
    elif n % 2 == 1:
        impar += 1
        total.append(n)
    
num_ing = par + impar
print(f"La cantidad de pares es: {par - 1}")
print(f"La cantidad de impares es: {impar}")
print(f"El promedio de impares es: {num_ing//impar}")
print(f"El mayor de todos los digitos es: {max(total)}")
print(total)
print(num_ing)