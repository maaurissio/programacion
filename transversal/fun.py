from os import system
import random
import statistics
system("cls")

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez",
                "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = {}

def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        key = len(sueldos)
        key += 1
        sueldos[key] = [trabajador, sueldo]
    print("Sueldos asignados con exito!")

def clasificar_sueldos():
    system("cls")
    menor_ocho = {}
    entre_ocho_dosm = {}
    superior_dosm = {}
    total_sueldos = []
    if len(sueldos) == 0:
        print("No se puede clasificar, no hay sueldos asignados")
        return
    else:
        for i, sueldo in sueldos.items():
            if sueldo[1] < 800000:
                key = len(menor_ocho)
                key += 1
                menor_ocho[key] = [sueldo[0], sueldo[1]]
                total_sueldos.append(sueldo[1])
                total_menor_ocho = len(menor_ocho)
            elif sueldo[1] >= 800000 and sueldo[1] <= 2000000:
                key = len(entre_ocho_dosm)
                key += 1
                entre_ocho_dosm[key] = [sueldo[0], sueldo[1]]
                total_sueldos.append(sueldo[1])
                total_entre_ocho_dosm = len(entre_ocho_dosm)
            elif sueldo[1] > 2000000:
                key = len(superior_dosm)
                key += 1
                superior_dosm[key] = [sueldo[0], sueldo[1]]
                total_sueldos.append(sueldo[1])
                total_superior_dosm = len(superior_dosm)
        suma_total = sum(total_sueldos)
        print(f"""
Sueldos menores a $800.000 TOTAL: {total_menor_ocho}              
Nombre empleado  |   Sueldo""")
        for i, sueldo in menor_ocho.items():
            print(f"""
{sueldo[0]} | {sueldo[1]}""")
        print(f"""
Sueldos entre $800.000 y $2.000.000 TOTAL: {total_entre_ocho_dosm}              
Nombre empleado  |   Sueldo""")
        for i, sueldo in entre_ocho_dosm.items():
            print(f"""
{sueldo[0]} | {sueldo[1]}""")
        print(f"""
Sueldos supeiores a $2.000.000 TOTAL: {total_superior_dosm}              
Nombre empleado  |   Sueldo""")
        for i, sueldo in superior_dosm.items():
            print(f"""
{sueldo[0]} | {sueldo[1]}""")
        print(f"TOTAL SUELDOS: ${suma_total}")

def estadisticas():
    system("cls")
    if len(sueldos) == 0:
        print("No se pueden ver las estadisticas, no hay sueldos asignados")
        return
    else:
        total = []
        for i, sueldo in sueldos.items():
            total.append(sueldo[1])
        mas_alto = max(total)
        mas_bajo = min(total)
        prom_sueldos = sum(total) // 10
        media_geo = statistics.geometric_mean(total)
        print(f"""
- Sueldo mas alto: {mas_alto}
- Sueldo mas bajo: {mas_bajo}
- Promedio de sueldos: {prom_sueldos}
- Media Geometrica: {media_geo}
""")

def reporte():
    system("cls")
    if len(sueldos) == 0:
        print("No se puede hacer un reporte, no hay sueldos asignados")
        return
    else:
        datos = {}
        for i, sueldo in sueldos.items():
            salud = sueldo[1] * 7 // 100
            afp = sueldo[1] * 12 // 100
            key = len(datos)
            key += 1
            datos[key] = [sueldo[0], sueldo[1], salud, afp]
        print("Nombre empleado  | Sueldo Base   | Descuento Salud   | Descuento AFP  | Sueldo liquido")
        for i, dato in datos.items():
            print(f"{dato[0]}   | {dato[1]}     | {dato[2]}     | {dato[3]}     | {dato[1] - afp - salud}")
        archivo = open("reporte.csv", "w")
        archivo.write("Nombre empleado;Sueldo Base;Descuento Salud;Descuento AFP;Sueldo liquido\n")
        for i, dato in datos.items():
            archivo.write(f"{dato[0]};{dato[1]};{dato[2]};{dato[3]};{dato[1] - afp - salud}\n")
        archivo.close()