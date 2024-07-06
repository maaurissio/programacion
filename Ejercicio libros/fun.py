from os import system
import random

# libros = [{
#     "ID": 1,
#     "Titulo": "Star Wars",
#     "Autor": "Vicente Colicheo",
#     "Genero": "Accion",
#     "Año publicacion": 1975,
#     "Ejemplares disponibles": 90000
# },{
#     "ID": 2,
#     "Titulo": "Harry Potter",
#     "Autor": "Bryan Jara",
#     "Genero": "Sexual",
#     "Año publicacion": 1986,
#     "Ejemplares disponibles": 1
# }]

libros = []

def agregar_libro():
    system("cls")
    id = random.randint(1, 100)
    while True:
        titulo = input("Ingrese el titulo del libro: ")
        if all(c.isalpha() or c.isspace() for c in titulo):
            break
        else:
            print("Ingrese un titulo valido")
    while True:
        autor = input("Ingrese el nombre del autor: ")
        if all(c.isalpha() or c.isspace() for c in autor):
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        genero = input("Ingrese el genero del libro: ")
        if genero.isalpha():
            break
        else:
            print("Ingrese un genero valido")
    while True:
        publicacion = input("Ingrese el año de publicacion del libro: ")
        if publicacion.isnumeric() and len(publicacion) == 4:
            break
        else:
            print("Ingrese un año de publicacion valido")
    while True:
        disponibles = input("Ingrese el numero de ejemplares disponibles: ")
        if disponibles.isnumeric() and disponibles != "0":
            break
        else:
            print("Ingrese un numero valido o mayor a 0")
    libro = {
        "ID": id,
        "Titulo": titulo,
        "Autor": autor,
        "Genero": genero,
        "Año publicacion": publicacion,
        "Ejemplares disponibles": disponibles
    }
    libros.append(libro)

def eliminar_libro():
    system("cls")
    libro_eliminar = input("Ingrese el ID del libro que quiere eliminar: ")
    for i, libro in enumerate(libros):
        if libro["ID"] == libro_eliminar:
            del libros[i]
            print(f"Libro {libro_eliminar} ha sido eliminado con exito")
            return
    print(f"Libro {libro_eliminar} no encontrado o no valido")

def modificar_libro():
    system("cls")
    libro_modificar = input("Ingrese el ID del libro que quiere modificar: ")
    for libro in libros:
        if libro["ID"] == libro_modificar:
            libro.update({
                "ID": int(input("Ingrese el nuevo ID: ")),
                "Titulo": input("Ingrese el nuevo titulo: "),
                "Autor": input("Ingrese el nuevo autor: "),
                "Genero": input("Ingrese el nuevo genero: "),
                "Año publicacion": input("Ingrese el nuevo año de publicacion: "),
                "Ejemplares disponibles": input("Ingrese el nuevo ejemplares: ")
            })
            return
    print(f"Libro {libro_modificar} no encontrado o no valido")            

def buscar_libro():
    system("cls")
    libro_buscar = input("Ingrese el titulo del libro que quiere buscar: ")
    for libro in libros:
        if libro["Titulo"] == libro_buscar:
            print(f"""
ID: {libro["ID"]}
Titulo: {libro["Titulo"]}
Autor: {libro["Autor"]}
Genero: {libro["Genero"]}
Año publicacion: {libro["Año publicacion"]}
Ejemplares disponibles: {libro["Ejemplares disponibles"]}""")

def guardar_datos():
    archivo = open("DatosLibro.txt", "w", encoding="utf-8")
    for libro in libros:
        archivo.write(f"ID: {libro["ID"]}\nTitulo: {libro["Titulo"]}\nAutor: {libro["Autor"]}\nGenero: {libro["Genero"]}\nAño Publicación: {libro["Año publicacion"]}\nEjemplares Disponibles: {libro["Ejemplares disponibles"]}\n\n")
    archivo.close()

def cargar_libros(datos):
    libros = []
    libro_actual = {}
    archivo = open(datos, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        clave, valor = linea.split(": ")
        if clave == "ID":
            if libro_actual:
                libros.append(libro_actual)
                libro_actual = {}
            libro_actual[clave] = int(valor)
        else:
            libro_actual[clave] = valor
    if libro_actual:
        libros.append(libro_actual)
    return libros
