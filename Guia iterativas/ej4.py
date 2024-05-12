# Crear un programa que lea un Número 5 dígitos e indique cuantos ceros lo componen. El número
# no puede comenzar por cero.

from os import system
system("cls")

num = int(input("Ingrese un número de 5 digitos: "))
ceros = 0

if num > 10000 and num < 99999:
    for i in range(1, 5):
        digito = num % 10
        if digito == 0:
            ceros += 1
        num = (num - digito)/10
else:
    print("Ta malo")
print(f"La cantidad de ceros es: {ceros}")