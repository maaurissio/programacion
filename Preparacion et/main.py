from os import system
import random
system("cls")

superheroes = {
    1: ["juan", 2000, 5],
    2: ["pedro", 2000, 5]
}

def agregar_superheroe():
    while True:
        nombre = input("Ingrese nombre del superheroe: ")
        if len(nombre) > 3:
            break
        else:
            print("Ingrese un nombre valido")
    while True:
        aparicion = input("Ingrese año de aparicion del superheroe: ")
        if aparicion.isnumeric() and len(aparicion) == 4:
            aparicion = int(aparicion)
            if aparicion > 1990:
                break
        else:
            print("Ingrese un año de aparicion valido")
    ubicacion = len(superheroes)
    ubicacion += 1
    superheroes[ubicacion] = [nombre, aparicion, 0]
    return

def asignar_popularidad():
    if len(superheroes) == 0:
        print("No hay ninguna wea")
        return
    else:
        popularidad = random.randint(1, 10)
        ubicacion_a_cambiar = int(input("Ingrese la ubicacion del superheroe que quiere darle la popularidad: "))
        if ubicacion_a_cambiar in superheroes:
            for ubicacion, datos in superheroes.items():
                if ubicacion_a_cambiar == ubicacion:
                    datos[2] = popularidad
                    print(f"Al heroe {datos[0]} se le asigno la popularidad de {popularidad}")
        else:
            print("No existe esa wea")

def mas_popular():
    popularidades = []
    max_popular = -1
    nombres = []
    for datos in superheroes.values():
        popularidades.append(datos[2])
    max_popular = max(popularidades)
    for ubicacion, datos in superheroes.items():
        if max_popular == datos[2]:
            nombres.append(datos[0])
    if len(nombres) == 1:
        print(f"El heroe {nombres[0]}, es el que tiene la mayor popularidad con {max_popular}")
    else:
        print(f"Los heroes más populares con una popularidad de {max_popular} son: ")
        for nombre in nombres:
            print(nombre) 

def exportar_csv():
    archivo = open("superheroes.csv", "w")
    archivo.write("ubicacion;nombre;aparicion;popularidad\n")
    for ubicacion, datos in superheroes.items():
        archivo.write(f"{ubicacion};{datos[0]};{datos[1]};{datos[2]}"+"\n")
    archivo.close()

while True:
    print(superheroes)
    op = input("""
1.- Agregar superheroe
2.- Asignar popularidad
3.- Mostrar superheroes con mayor popularidad
4.- Buscar popularidad de superheroe por nombre
5.- Guardar datos en archivo csv
0.- Salir
Eliga una opción: """)
    match op:
        case "1":
            agregar_superheroe()
        case "2":
            asignar_popularidad()
        case "3":
            pass
        case "4":
            mas_popular()
        case "5":
            exportar_csv()
        case "0":
            print("Saliendo...")
            break
        case other:
            system("cls")
            print("Escoga una opcion valida")
            