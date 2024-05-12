# Crear un programa que lea N vocales (una por una), Después imprimir la información como se
# muestra en la tabla de abajo. Esta tabla ejemplifica que se ingresaron 51 vocales, en donde 10
# eran A, 6 E, etc. Vocal CANTIDAD A :10 E:6 I:18 O:9 U:8
from os import system
system("cls")

# a = 0
# e = 0
# i = 0
# o = 0
# u = 0
# vocal = ""
# while vocal != "0":
#     vocal = input("Ingrese una vocal o presione 0 para salir: ")
#     if vocal == "a":
#         a += 1
#     elif vocal == "e":
#         e += 1
#     elif vocal == "i":
#         i += 1
#     elif vocal == "o":
#         o += 1
#     elif vocal == "u":
#         u += 1

# print(f"""
#     Cantidad de vocales:
#     A:{a}
#     E:{e}
#     I:{i}
#     O:{o}
#     U:{u}
# """)

a = 0
e = 0
i = 0
o = 0
u = 0

cuantas = int(input("Cuantas vocales quiere leer: "))
for i in range(cuantas):
    vocal = input("Ingrese una vocal: ").lower()
    if vocal in "aeiou":
        if vocal == "a":
            a += 1
        elif vocal == "e":
            e += 1
        elif vocal == "i":
            i += 1
        elif vocal == "o":
            o += 1
        elif vocal == "u":
            u += 1
    else:
        print("No es una vocal")

print(f"""
#     Cantidad de vocales:
#     A:{a}
#     E:{e}
#     I:{i}
#     O:{o}
#     U:{u}
# """)