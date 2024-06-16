# Ejercicio
# En una pizzería se venden 4 tipos de pizzas:

# Margarita - $6000
# Pepperoni - $7000
# Cuatro Quesos - $8000
# Hawaiana - $7500
# La pizzería te ha solicitado que desarrolles una pequeña aplicación en Python para tomar el pedido de un cliente. 
# El cliente puede ir agregando pizzas a través de un menú uno por uno con solo seleccionar la opción (1 a 4). 
# La aplicación debe mostrar en un menú los tipos de pizza que agregará el usuario. Esto se debe repetir hasta que el usuario decida que su pedido está completo.

# Luego de ello, debes preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá ingresarlo. 
# Si el código ingresado es “pizzalover”, debe realizar un 15% de descuento al total del pedido; 
# en caso contrario, enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú tecleando “X”.

# Una vez realizados los pasos anteriores, debes mostrar el detalle del pedido contabilizando el total de productos y la cantidad de cada uno de ellos, y si aplica o no el descuento.

# Puntos a implementar
# Mostrar un menú para seleccionar los tipos de pizza.
# Permitir al usuario agregar múltiples ítems a su pedido.
# Calcular el total del pedido.
# Preguntar por un código de descuento y aplicarlo si es válido.
# Mostrar un resumen del pedido final.

valor_pmargarita = 6000
valor_ppepperoni = 7000
valor_pcuatroquesos = 8000
valor_phawaiana = 7500


while True: 
    cantidad_pm = 0
    cantidad_pp = 0
    cantidad_pcq = 0
    cantidad_ph = 0
    total = 0
    print("Bienvenido a pizzas mj, a continuación le mostraremos el menú")
    while True:
        op = int(input("""
            1. Pizza Margarita
            2. Pizza Pepperoni
            3. Pizza Cuatro Quesos
            4. Pizza Hawaiana
            0. Continuar
            
            Seleccionar opción: """))
        if op >= 0 and op < 5:
            if op == 1:
                cantidad_pm += 1
                cantidad = int(input("Cuantas desea agregar?: "))
                cantidad_pm *= cantidad
                print(f"Usted agrego {cantidad_pm} Pizza Margarita")
                valor_pmargarita *= cantidad
                total += valor_pmargarita
            elif op == 2:
                cantidad_pp += 1
                cantidad = int(input("Cuantas desea agregar?: "))
                cantidad_pp *= cantidad
                print(f"Usted agrego {cantidad_pp} Pizza Pepperoni")
                valor_ppepperoni *= cantidad
                total += valor_ppepperoni
            elif op == 3:
                cantidad_pcq += 1
                cantidad = int(input("Cuantas desea agregar?: "))
                cantidad_pcq *= cantidad
                print(f"Usted agrego {cantidad_pcq} Pizza Cuatro Quesos")
                valor_pcuatroquesos += cantidad_pcq
                total += valor_pcuatroquesos
            elif op == 4:
                cantidad_ph += 1
                cantidad = int(input("Cuantas desea agregar?: "))
                cantidad_ph *= cantidad
                print(f"Usted agrego {cantidad_ph} Pizza Hawaiana")
                valor_phawaiana *= cantidad
                total += valor_phawaiana
            else:
                break
        else:
            print("Opción invalida, por favor ingrese otra opción")

    while True:
        op = input("Tiene codigo de descuento? s/n: ")
        if op == "s" and op.isalpha():
            while True:
                codigo = input("Ingrese su codigo de descuento: ")
                if codigo == "pizzalover" and codigo.isalpha():
                    descuento = total * 15 // 100
                    print(f"""
                    Cantidad de Pizza Margarita: {cantidad_pm}
                    Cantidad de Pizza Pepperoni: {cantidad_pp}
                    Cantidad de Pizza Cuatro Quesos: {cantidad_pcq}
                    Cantidad de Pizza Hawaiana: {cantidad_ph}
                    Descuento: {descuento}
                    Total: {total - descuento}
                            """)
                    break
                else:
                    op = input("Codigo incorrecto, presione s para reingresarlo o n para volver al menu: ")
                    if op == "s" and op.isalpha():
                        pass
                    elif op == "n" and op.isalpha():
                        break
            break
        elif op == "n" and op.isalpha():
            print(f"""
                Cantidad de Pizza Margarita: {cantidad_pm}
                Cantidad de Pizza Pepperoni: {cantidad_pp}
                Cantidad de Pizza Cuatro Quesos: {cantidad_pcq}
                Cantidad de Pizza Hawaiana: {cantidad_ph}
                Descuento: 0
                Total: {total}
                        """)
            break
    op = input("Desea realizar otro pedido? s/n: ")
    if op == "s" and op.isalpha():
        pass
    elif op == "n" and op.isalpha():
        break



