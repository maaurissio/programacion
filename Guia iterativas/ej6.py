# Diseñar un programa que dados 20 números determine el mayor de ellos.
from os import system
system("cls")

nums = []

for i in range (5):
    num = int(input("Ingrese un número: "))
    nums.append(num)

print(f"El número maximo es: {max(nums)}")