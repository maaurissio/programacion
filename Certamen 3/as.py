pedidos = [{
    "ID pedido": 56348,
    "Nombre": "Mauricio",
    "Apellido": "Gajardo",
    "Direccion": "Coronel 1067",
    "Sector": "Concepción",
    "Disp.6lts": 5,
    "Disp.10lts": 2,
    "Disp.20lts": 1
}]

for pedido in pedidos:
    print(f"""
    nombre:{pedido["Nombre"]}
    apellido:{pedido["Apellido"]}
    direccion:{pedido["Direccion"]}
""")

print(pedidos)

def asd(pedidos):
    for pedido in pedidos:
        archivo = open("asd.csv", "w")
        archivo.write("Nombre;Apellido;Direccion\n")
        archivo.write(f"{pedido["Nombre"]};{pedido["Apellido"]};{pedido["Direccion"]}")


def buscar(pedidos):
    id_buscado = int(input("Ingrese un id a buscar: "))
    for pedido in pedidos:
        if id_buscado == pedido["ID pedido"]:
            print(f"""
    nombre:{pedido["Nombre"]}
    apellido:{pedido["Apellido"]}
    direccion:{pedido["Direccion"]}
""")


buscar(pedidos)