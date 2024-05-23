from os import system
system("cls")
# Supongamos que se requiere desarrollar el control de una máquina de entrega de café automática. 

# La  máquina  debe  permitir  a  una  persona  entregar  una  cantidad  de  dinero  en  monedas  de  10,  50, 
# 100,  200  o  500,  y  billetes  de  1000  y  2000,  escoger  uno  de  los  productos  que  cuestan  $800.  (café 
# negro, café claro, café capuccino), escoger (si es pertinente) un nivel de azúcar entre 0 y 6 entregar 
# el  producto  y  dar  vuelto. La  máquina debe  tener  un  menú  para los  clientes  y  uno  para el 
# administrador de la máquina que puede acceder con la clave “12345” 

# • El dinero que los usuarios introducen se guarda en un recipiente para cada moneda o billete. Debe 
#   especificar con un menú de monedas y billetes cada uno de los tipos que introduce en la máquina 

# 1. 10 
# 2. 50 
# 3. 100 
# 4. 500 
# 5. 1000 
# 6. 2000 

# • Existen estados de error de la máquina, cuando detecta la no existencia de vueltos o no existencia 
#   de ingredientes debe detener su funcionamiento. 

# • El usuario puede en cualquier momento antes de escoger el azúcar cancelar la operación. 
# •  
# • Cada carga de cafe para cada tipo, rinde 100 vasos, una carga de agua y azúcar para 300 vasos, por 
#   lo tanto, la máquina debe controlar los niveles cada ingrediente. 

# • Además, al iniciar la máquina se debe cargar con 50 monedas y billetes para cada tipo de forma que 
#   pueda dar vuelto. La capacidad máxima de cada recipiente de monedas es 400 monedas por lo que 
#   controlar el dinero entrante y saliente 

# o Debe mostrar el detalle del vuelto, por ejemplo, si pago con 2000 
# ▪ 10:0 
# ▪ 50:0 
# ▪ 100:2 
# ▪ 500:2 
# ▪ 1000:0 
# ▪ 2000:0 
# ▪ TOTAL: $1200 

claveultrasecreta = 12345
mon10 = 50
mon50 = 50
mon100 = 50
mon500 = 50
billmil = 50
billdosm = 50
cafe = ""


while True:
    ingreso = input("¿Desea ingresar como cliente o como administrador?\n")
    if ingreso == "cliente" or ingreso == "administrador":
        break
    else:
        print("¡Escriba una opcion correcta!")

if ingreso == "cliente":
    print("""
    ¡Bienvenido a coffe with legs! tenemos el cafe a $800, pero tenemos tres tipos de cafes diferentes, ¡espero lo disfrutes!
    """)
    cafe = input("Tenemos tres diferentes cafes, ¡escoge el que mas te guste! \n 1.Café negro\n 2.Café claro\n 3.Café capuccino\n")
    while True:
        if cafe == "1":
            azucar = input("Usted escogio el café negro, ¿quiere agregarle azucar? s/n\n")
            if azucar == "s":
                nivelazucar = int(input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                while nivelazucar < 1 or nivelazucar > 6:
                    print("Ingrese un nivel de azucar valido.")
                    nivelazucar = int(input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                    if nivelazucar > 1 or nivelazucar < 6:
                        break
            elif azucar == "n":
                break
        
        elif cafe == "2":
            azucar = input("Usted escogio el café claro, ¿quiere agregarle azucar? s/n\n")
            if azucar == "s":
                nivelazucar = (input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                nivelazucar = int(nivelazucar)
                while nivelazucar < 1 or nivelazucar > 6:
                    print("Ingrese un nivel de azucar valido.")
                    nivelazucar = int(input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                    if nivelazucar > 1 or nivelazucar < 6:
                        break
            elif azucar == "n":
                break
        
        elif cafe == "3":
            azucar = input("Usted escogio el café capuccino, ¿quiere agregarle azucar? s/n\n")
            if azucar == "s":
                nivelazucar = int(input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                while nivelazucar < 1 or nivelazucar > 6:
                    print("Ingrese un nivel de azucar valido.")
                    nivelazucar = int(input)("¿Cual es el nivel de azucar que quiere agregarle? entre 1 y 6\n")
                    if nivelazucar > 1 or nivelazucar < 6:
                        break
            elif azucar == "n":
                break
    