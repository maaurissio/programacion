from os import system
import random
system("cls")

libros = []

def registro(libros):
    codigo = random.randint(1, 1000)
    titulo = str(input("Ingrese el titulo del libro: "))
    autor = str(input("Ingrese el autor del libro: "))
    genero = str(input("Ingrese el genero del libro: "))
    libros.append([codigo, titulo, autor, genero])
    return

while True:
    print("""
1.- Registrar libro
2.- Listar libros
3.- Buscar libro (Por titulo o autor)
4.- Prestar y devolver libros
5.- Generar reporte de libros prestados
""")
    op = input("Ingrese opcion: ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "0":
            break
        case _:
            print("Opcion no valida")