from os import system
system ("cls")

cabañas = [True,True,True,True,True,True,True,True,True,True]
reservas = []
nombres=[]
valorCabañas=100000
recaudacionn=[]
dias_reservados=[]

def arrendar_cabaña(nombre, cabañas, reservas):
    print("Cabañas disponibles:")
    for i in range(len(cabañas)):
        if cabañas[i]:
            print(f"Cabaña {i+1}")
    cabaña = int(input("Ingrese el numero de la cabaña que desea reservar: ")) -1
    dias_reservados=int(input("Ingrese cuantos dias desea reservar la cabaña: "))
    if cabañas[cabaña]:
        cabañas[cabaña] = False
        reservas.append([nombre, cabaña, dias_reservados])
        dias_reservados.append([dias_reservados])
        print("Reserva exitosa")
    else:
        print("Lo siento, ya está reservada esta cabaña")

def disponibilidad(cabañas):
    for i in range(len(cabañas)):
        if cabañas[i] == True:
            estado = "Disponible"
        else:
            estado = "Reservada a nombre de: ", 
        print(f" {i + 1}: {estado}")

def entregar_cabaña(cabañas):
    reserva_a_eliminar=int(input("Ingrese el numero de la cabaña que desea entregar: "))
    if 1<= reserva_a_eliminar:
        indice_en_reservas = reservas[reserva_a_eliminar-1]
        cabañas = reservas[indice_en_reservas][1]
        cabañas[cabañas]=True

        del reservas[indice_en_reservas]
        print("Reserva entregada con éxito")
    else:
        print("Número de la reserva no es valido!")

def recaudacion(reservas):
    for i in range(len(reservas)):
            print("Se recaudo: ", valorCabañas*dias_reservados)
            recaudacionn.append(valorCabañas)
            print("Recaudacion Total:", recaudacionn)

while True:
    print("""
    1.- Arrendar cabaña
    2.- Ver disponibilidad
    3.- Entregar cabaña
    4.- Ver recaudacion a la fecha

    5.-Salir
    """)
    opcion = int(input("Seleccione una opción: "))
    if opcion==1:
        nombre=(input("Ingrese su nombre: ")) 
        arrendar_cabaña(nombre,cabañas,reservas)
    elif opcion==2:
        disponibilidad(cabañas)
    elif opcion==3:
        entregar_cabaña(nombre,cabañas,reservas)
    elif opcion==4:
        recaudacion(reservas, dias_reservados)
    elif opcion==5:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, vuelva a intentarlo...")