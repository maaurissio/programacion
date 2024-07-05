from os import system
from funciones import registrar_trabajador, listar_trabajador, imprimir_planilla
system("cls")

while True:
    print('''
    1. Registrar trabajador
    2. Listar los todos los trabajadores
    3. Imprimir planilla de sueldos
    4. Salir del Programa
''')
    op = input("Seleccione una ")
    match op:
        case "1":
            registrar_trabajador()
        case "2":
            system("cls")
            listar_trabajador()
        case "3":
            imprimir_planilla()
        case "4":
            break
        case other:
            print("Opción ingresada no valida, intente nuevamente...")