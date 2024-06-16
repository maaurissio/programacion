from os import system
system("cls")

asientos = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',], 
            ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
            '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', 
            '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',], 
            ['51', '52', '53', '54', '55', '56', '57', '58', '59', '60', 
            '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', 
            '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', 
            '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', 
            '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']]

def compra():
    print("¿Cuantas entradas quiere comprar? Solo se puede de 1 a 3")
    while True:
        op = int(input("Ingrese cantidad: "))
        if op >= 1 and op <= 3:
                break
        else:
            print("Ingrese una opcion valida")
    print(f"Los asientos disponibles son {asientos}")
    for _ in range(op):
        while True:
            compra = input("Cuales asientos quiere?: ")
            if compra in asientos:
                asiento = asientos.index(compra)
                asientos[asiento] = "X"
                print(f"Asiento {compra} comprado con exito")
                break
            else:
                print("Asiento invalido o no disponible, ingrese otro")


while True:
    print("""Entradas concierto Michael Jam
    1. Compra de entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    0. Ver las ganancias totales
    """)
    op = input("Ingrese opcion: ")
    match op:
        case "1":
            compra()
        case "2":
            pass
        case "3":
            pass
        case "0":
            pass
        case other:
            print("Opcion invalida")