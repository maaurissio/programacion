from os import system
from fun import *
system("cls")

while True:
    print(libros)
    print("""
1.- Agregar libro (titulo, autor, genero, año, ejemplares disponibles)
2.- Eliminar libro (ID)
3.- Modificar libro (id, nuevo id, nuevo titulo, nuevo autor, nuevo genero, nuevo año, nuevos ejemplares)
4.- Buscar libro (ID)
5.- Guardar libros (DatosLibro.txt)
6.- Cargar libros
0.- Salir""")
    op = input("\nEliga opción: ")
    match op:
        case "1":
            agregar_libro()
        case "2":
            eliminar_libro()
        case "3":
            modificar_libro()
        case "4":
            buscar_libro()
        case "5":
            guardar_datos()
        case "6":
            libros = cargar_libros("DatosLibro.txt")
            pass
        case "0":
            print("Saliendo...")
            break
        case other:
            print("Opcion invalida")