from os import system
import random
import statistics
from fun import *
system("cls")

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez",
                "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = {}

while True:
    op = input("""
1.- Asignar sueldos aleatorios
2.- Clasificar sueldos
3.- Ver estadisticas
4.- Reporte de sueldos
5.- Salir del programa
               
Eliga opcion: """)
    match op:
        case "1":
            asignar_sueldos()
        case "2":
            clasificar_sueldos()
        case "3":
            estadisticas()
        case "4":
            reporte()
        case "5":
            print("""
Finalizando programa...
Desarrollado por Mauricio Gajardo
RUT 21.588.043-5
""")
            break
        case other:
            print("Ingrese una opcio valida")

#https://github.com/maaurissio/et