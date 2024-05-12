# Calcular e imprimir el promedio de notas de 3 personas. Cada persona tiene dos notas. Se debe
# imprimir el promedio de cada persona. Al final imprimir el promedio del curso.

from os import system
system("cls")

promedio_curso = 0

for i in range(3):
    print(f"Alumno {i+1}")
    n1 = int(input("Ingrese la primera nota: "))
    n2 = int(input("Ingrese la segunda nota: "))
    promedio = (n1 + n2) // 2
    promedio_curso += promedio

print(f"Promedio del curso: {promedio_curso / 3}")