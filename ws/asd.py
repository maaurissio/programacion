categoria = ['herramientas', 'materiales', 'electricidad']
def registrar_prod(producto:list):
    while True:
        cat = input('ingrese categoria: ')
        if cat in categoria:
            break
        else:
            print("ingresa otra wea")
    while True:
        nombre = input('Ingrese nombre: ')
        if nombre != '' and nombre.isalpha():
            break
    while True:
        cant_stock = input('Cantidad: ')
        if cant_stock.isnumeric() and int(cant_stock)> 0:
            break

    while True:
        precio = input('Ingrese precio: ')
        if precio.isnumeric() and int(precio) > 0:
            break
    agregar = {'Categoria': cat,
               'Nombre': nombre,
               'Stock': cant_stock,
               'Precio': precio}
    producto.append(agregar) 
    return categoria

registrar_prod(list)