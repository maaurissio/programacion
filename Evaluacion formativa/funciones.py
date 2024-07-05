trabajadores = [["Pato", "Zapata", "CEO", 5000000, 5000000-5000000*0.07, 5000000-5000000*0.12,5000000-5000000*0.19 ]]
cargos = ["CEO", "Analista Programador", "Desarrollador"]

def registrar_trabajador():
    print("Ingrese los datos del trabajador: ")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    cargo = str(input("Cargo: "))
    if cargo not in cargos:
        cargos.append(cargo)
    sueldo_bruto=int(input("Sueldo bruto: "))
    desc_salud = sueldo_bruto*0.07
    desc_afp = sueldo_bruto*0.12
    liq_pagar = sueldo_bruto - desc_salud - desc_afp
    trabajadores.append([nombre, apellido, cargo, sueldo_bruto, desc_salud, desc_afp, liq_pagar])
    return

def listar_trabajador():
        if len(trabajadores) !=0:
            print('''
            Trabajador    Cargo     Sueldo Bruto    Desc. Salud     Desc. AFP       Líquido a pagar
            ''')
            for trabajador in trabajadores:                
                print (f'''  
            {trabajador[0]}          {trabajador[2]}       {trabajador[3]:.1f}        {trabajador[4]:.1f}       {trabajador[5]:.1f}      {trabajador[6]:.1f}
            {trabajador[1]}
            ''')
        else:
            print("No se han registrado trabajadores")

def imprimir_planilla():
    print('''
    1.- Imprimir lista de todos los trabajadores
    2.- Imprimir por cargo
''')
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            file = open("lista_trabajadores.txt", "w")
            file.write("nombre;apellido;cargo;sueldobruto;des.salud;des.afp;liqpagar" + "\n")
            for trabajador in trabajadores:
                file.write(f"{trabajador[0]}" + ";" + f"{trabajador[1]}" + ";" + f"{trabajador[2]}" + ";" +f"{str(trabajador[3])}" + ";" +f"{trabajador[4]}" + ";" + f"{trabajador[5]}" + ";" +f"{trabajador[6]}" + "\n")
        case "2":
            cargo_a_imprimir = input("Ingrese el cargo: ")
            if cargo_a_imprimir in cargos:
                file = open("lista_trabajadores.txt", "w")
                file.write("nombre;apellido;cargo;sueldobruto;des.salud;des.afp;liqpagar" + "\n")
                for trabajador in trabajadores:
                    if cargo_a_imprimir == trabajador[2]:
                        file.write(f"{trabajador[0]}" + ";" + f"{trabajador[1]}" + ";" + f"{trabajador[2]}" + ";" +f"{str(trabajador[3])}" + ";" +f"{trabajador[4]}" + ";" + f"{trabajador[5]}" + ";" +f"{trabajador[6]}" + "\n")
            else:
                print("El cargo seleccionado no se encuentra registrado...")