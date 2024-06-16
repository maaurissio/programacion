# Desarrollar un algoritmo que simule el proceso de reserva de pasajes de buses para una empresa
# de transporte en Chile. El programa debe comenzar solicitando al usuario su nombre y si es cliente
# frecuente de la empresa (True/False).
# Luego, debe preguntar al usuario su destino preferido entre las siguientes opciones:
#       1. Santiago 8.000
#       2. Valparaíso 10.000
#       3. Concepción 12.000
# Una vez seleccionado el destino, el programa debe preguntar al usuario la fecha de viaje y de
# retorno. Después, debe preguntar si el usuario desea agregar servicios adicionales a su reserva,
# como seguro de viaje o asientos premium. Si la respuesta es afirmativa, el programa debe mostrar
# las siguientes opciones:
#       1. Seguro de viaje - $5.500
#       2. Asiento premium - $2.500
# El usuario debe seleccionar los servicios extras deseados y la cantidad en caso de aplicar.
# Finalmente, el programa debe mostrar un resumen de la reserva con el nombre del pasajero,
# destino, fechas, servicios adicionales seleccionados y el costo total.

costo_total = 0
santiago = 8000
valparaiso = 10000
concepcion = 12000
valor_seguro = 5500
valor_asiento = 2500

print("Bienvenido a marcianeke transportes")
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre != "" or len(nombre) > 3:
        break
    else:
        print("Ingrese un nombre valido")
op = int(input("""
    ¿Cual es su destino preferido entre estas 3 opciones?
      1. Santiago: 8.000
      2. Valparaiso: 10.000
      3. Concepcion: 12.000
        """))
while op <= 0 or op >3:
    print("Escoga una opción valida")
    op = int(input("""
    ¿Cual es su destino preferido entre estas 3 opciones?
      1. Santiago: 8.000
      2. Valparaiso: 10.000
      3. Concepcion: 12.000
        """))
if op == 1:
    print("Usted escogio santiago como su destino")
    destino = "Santiago"
    costo_total += santiago
elif op == 2:
    print("Usted escogio Valparaiso como su destino")
    destino = "Valparaiso"
    costo_total += valparaiso
elif op == 3:
    print("Usted escogio Concepción como su destino")
    destino = "Concepción"
    costo_total += concepcion
    
fechaviaje = input("Ingrese la fecha de viaje: ")
fecharetorno = input("Ingrese la fecha de retorno: ")

servad = (input("¿Desea agregar servicios adicionales a su reserva?, como seguro de viaje o asientos premium, s/n: "))

seguroviaje = 0
asientoprem = 0

while servad == "s":
    op = int(input("""
    El valor de los servicios adicionales es de:
                   1. Seguro de viaje : 5.500
                   2. Asiento premium: 2.500   
                """))
    if op == 1:
        print("Usted selecciono el seguro de viaje.")
        seguroviaje += 1
        costo_total += valor_seguro
    elif op == 2:
        print("Usted selecciono un Asiento premium")
        asientoprem += 1
        costo_total += valor_asiento
    op = input("¿Desea agregar mas servicios? s/n: ")
    if op == "n":
        break

print(f"""
    Nombre pasajero: {nombre}
    Destino de viaje: {destino}
    Fecha de ida: {fechaviaje}
    Fecha de retorno: {fecharetorno}
    Servicios adicionales: 
        - Seguro de viaje: {seguroviaje}
        - Asiento premium: {asientoprem}
    Costo total: {costo_total}
""")