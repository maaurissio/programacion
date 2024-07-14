from os import system
system("cls")

def guardar_ficha():
    while True:
        rut = input("Ingrese su rut: ")
        if len(rut) == 9:
            break
        else:
            print("Ingrese un rut valido.")
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre != "":
            break
        else:
            print("Ingrese un nombre valido.")
    while True:
        apellido = input("Ingrese su apellido: ")
        if nombre != "":
            break
        else:
            print("Ingrese un apellido valido.")
    while True:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18 and edad != "":
            break
        else:
            print("Ingrese una edad valida.")
    while True:
        civil = input("Ingrese su estado civil (C = CASADO, S = SOLTERO, V = VIUDO): ")
        if len(civil) == 1:
            if civil == "c" or civil == "C":
                civil = "Casado"
                break
            elif civil == "s" or civil == "S":
                civil = "Soltero"
                break
            elif civil == "v" or civil == "V":
                civil = "Viudo"
                break
        else:
            print("Ingrese un estado civil valido")
    while True:
        fecha = input("Ingrese su fecha de afiliacion: ")
        if fecha != "":
            break
        else:
            print("Ingrese una fecha valida.")
    while True:
        correo = input("Ingrese su correo electronico: ")
        arroba = correo.count("@")
        if arroba == 1 and correo != "":
            break
        else:
            print("Ingrese un correo con solo un arroba.")


while True:
    try:
        op = input("""
    1.- Guardar afiliado
    2.- Buscar afiliado
    3.- Imprimir certificado
    0.- Salir\nEliga opción: """)
        match op:
            case "1":
                guardar_ficha()
            case "2":
                pass
            case "3":
                pass
            case "0":
                print("Saliendo...")
                break
            case other:
                print("Ingresa una opcion valida")
    except ValueError:
        print("Opcion invalida")