import os
tarjeta = {
    'Cupo total': 800000,
    'Deuda': 0,
    'Saldo Disponible': 800000
}

compras = 0

def comprar(tarjeta):
    os.system("cls")
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        compra = int(input("Ingrese el valor del producto: "))
        cupo = tarjeta['Saldo Disponible']
        if compra*1.03 > cupo or compra <= 0:
            print("Ingrese un valor valido")
        else:
            tarjeta['Deuda'] += (compra * 1.03)
            tarjeta['Saldo Disponible'] -= (compra * 1.03)
            print(f"La compra de {nombre} fue realizada con exito")
            return tarjeta, compras

def pago_deuda(tarjeta):
    os.system("cls")
    deuda = tarjeta['Deuda']
    if deuda == 0:
        print("No hay deudas que pagar")
        return tarjeta
    else:
        print(f"La deuda de su tarjeta es de {deuda}")
        abono = int(input("Ingrese el abono a pagar: "))
        while True:
            if abono > deuda or abono <= 0:
                print("El pago no puede ser mayor o menor a la deuda")
                abono = int(input("Ingrese el abono a pagar: "))
            else:
                tarjeta['Deuda'] -= abono
                return tarjeta

def consulta_detalles(tarjeta):
    os.system("cls")
    print(f"""
    Cupo total: {tarjeta['Cupo total']}
    Deuda: {tarjeta['Deuda']}
    Saldo disponible: {tarjeta['Saldo Disponible']}
""")

def total(compras):
    os.system("cls")
    print(f"Sus compras totales son: {compras}")
    return compras