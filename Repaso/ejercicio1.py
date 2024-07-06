from os import system
import random
system("cls")

jugadores = [{
                "ID registro": 56975,
                "Nombre": "Mauricio",
                "Año": 2004,
                "Equipo": "Colo Colo",
                "USA": 5,
                "Mexico": 6,
                "Colombia": 3
            }]

def registro_goles(jugadores):
    id = random.randint(1, 100000)
    while True:
        nombre = input("Ingrese el nombre del jugador: ")
        if len(nombre) > 3 and nombre.isalpha():
            break
        else:
            print("Ingrese un nombre valido")
            continue
    while True:
        nacimiento = input("Ingrese el año de nacimiento del jugador: ")
        if nacimiento.isnumeric():
            nacimiento = int(nacimiento)
            if nacimiento >= 1985:
                break
        else:
            print("Ingrese un año de nacimiento igual o mayor a 1985")
    while True:
        equipo = input("Ingrese al equipo que pertenece: ")
        if equipo == "":
            print("Ingrese un nombre valido")
        else:
            break
    while True:
        usa = int(input("Ingrese la cantidad de goles hacia Estados Unidos: "))
        mex = int(input("Ingrese la cantidad de goles hacia Mexico: "))
        col = int(input("Ingrese la cantidad de goles hacia Colombia: "))
        total = usa + mex + col
        if total < 2:
            print("Para ser registrado el total de goles debe ser mayor a 2")
        else:
            jugador = {
                "ID registro": id,
                "Nombre": nombre,
                "Año": nacimiento,
                "Equipo": equipo,
                "USA": usa,
                "Mexico": mex,
                "Colombia": col
            }
            jugadores.append(jugador)
            print("Jugador registrado exitosamente!")
            break

def listar(jugadores):
    print("ID Registro        Jugador         Año Nacimiento          Equipo          USA         Mexico          Colombia")
    for jugador in jugadores:
        print(f"""{jugador["ID registro"]}      {jugador["Nombre"]}     {jugador["Año"]}        {jugador["Equipo"]}         {jugador["USA"]}        {jugador["Mexico"]}        {jugador["Colombia"]}""")


def imprimir_bitacora(jugadores):
    archivo = open("bitacora.csv", "w")
    archivo.write("ID Registro;Jugador;Año Nacimiento;Equipo;USA;Mexico;Colombia")
    for jugador in jugadores:
        archivo.write(f"\n{jugador["ID registro"]};{jugador["Nombre"]};{jugador["Año"]};{jugador["Equipo"]};{jugador["USA"]};{jugador["Mexico"]};{jugador["Colombia"]}")
    archivo.close()

def buscar_id(jugadores):
    id = int(input("Ingrese un id a buscar: "))
    for jugador in jugadores:
        if id == jugador["ID registro"]:
            print(f"""ID Registro        Jugador         Año Nacimiento          Equipo          USA         Mexico          Colombia
{jugador["ID registro"]}      {jugador["Nombre"]}     {jugador["Año"]}        {jugador["Equipo"]}         {jugador["USA"]}        {jugador["Mexico"]}        {jugador["Colombia"]}""")

while True:
    print("""
1.	Registrar bitácora de goles
2.	Listar los todas las bitácoras
3.	Imprimir hoja bitácoras
4.	Buscar una bitácora por ID
0.	Salir del programa""")
    op = input("Ingrese una opcion: ")
    match op:
        case "1":
            registro_goles(jugadores)
        case "2":
            listar(jugadores)
        case "3":
            imprimir_bitacora(jugadores)
        case "4":
            buscar_id(jugadores)
        case "0":
            break
        case other:
            print("Por favor, ingrese una opcion valida")