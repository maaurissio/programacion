from os import system
system("cls")

trabajadores = [{
        "Trabajador": "Mauricio",
        "Cargo": "CEO",
        "Sueldo bruto": 1000000,
        "Desc. Salud": 120000,
        "Desc. AFP": 80000,
        "Liquido a pagar": 800000
    }]

def registrar(trabajadores):
    nombre = input("Ingrese el nombre del trabajador: ")
    cargo = input("Ingrese el cargo: ")
    sueldo_bruto = int(input("Ingrese el sueldo en bruto: "))
    desc_salud = int(input("Ingrese el descuento de la salud: "))
    desc_afp = int(input("Ingrese el descuento de la AFP: "))
    sueldo_liq = sueldo_bruto - (desc_salud - desc_afp)
    trabajador = {
        "Trabajador": nombre,
        "Cargo": cargo,
        "Sueldo bruto": sueldo_bruto,
        "Desc. Salud": desc_salud,
        "Desc. AFP": desc_afp,
        "Liquido a pagar": sueldo_liq
    }
    trabajadores.append(trabajador)

def listar(trabajadores):
    # for trabajador in trabajadores:
    #     print(f"""
    #     Trabajador: {trabajador["Trabajador"]}
    #     Cargo: {trabajador["Cargo"]}
    #     Sueldo bruto: {trabajador["Sueldo bruto"]}
    #     Descuendo Salud: {trabajador["Desc. Salud"]}
    #     Descuento AFP: {trabajador["Desc. AFP"]}
    #     Liquido a pagar: {trabajador["Liquido a pagar"]}
    #     """)
    print("     Trabajador:    Cargo:      Sueldo bruto:      Descuento Salud:      Descuento AFP:      Liquido a pagar: ")
    for trabajador in trabajadores:
        print(f"""
        {trabajador["Trabajador"]}    {trabajador["Cargo"]}    {trabajador["Sueldo bruto"]}    {trabajador["Desc. Salud"]}    {trabajador["Desc. AFP"]}    {trabajador["Liquido a pagar"]}
    """)
while True:
    print("""
    1.- Registrar Trabajador
    2.- Listar todos los trabajadores
    3.- Imprimir plantilla de sueldos
    0.- Salir
    """)
    op = input("Ingrese opcion: ")
    match op:
        case "1":
            registrar(trabajadores)
        case "2":
            listar(trabajadores)
        case "3":
            pass
        case "0":
            break
        case other:
            print("Opcion no valida")