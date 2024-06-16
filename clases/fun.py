import os

def cargar_datos(mes):      #Carga de datos
    mes = []
    f = open('clases/datos/datosmes.csv', 'r')
    f.readline()
    while True:
        linea = f.readline()
        if not linea:
            break
        datos = linea.split(';')
        if len(datos) >= 3:
            datos[3] = datos[3].replace('\n', '')
        mes.append(datos)
    f.close()
    return mes

# def cargardatos(mes):
#     f = open('clases/datos/datosmes.csv', 'r')
#     f.readline()
#     for linea in f:
#         dias = linea.replace('\n', '').split(';')
#         mes.append(dias)


def fecha_mayor_temperatura(mes):   #Fecha del día con mayor temperatura
    os.system("cls")
    temperatura = []
    for dia in mes:
        temp_maxima = dia[2].replace(',', '.')
        temp_maxima = float(temp_maxima)
        temperatura.append(temp_maxima)
    mayor = max(temperatura)
    indice = temperatura.index(mayor)
    fecha = mes[indice][0]
    print(f"La fecha que presento la mayor temperatura fue {fecha} con una temperatura de {mayor}")

def dia_mas_frio(mes):      #Día más frío del mes
    os.system("cls")
    temperatura = []
    for dia in mes:
        temp_min = dia[1].replace(',', '.')
        temp_min = float(temp_min)
        temperatura.append(temp_min)
    menor_temp = min(temperatura)
    indice = temperatura.index(menor_temp)
    dia_mas_frio = mes[indice][0].split('/')[0]
    print(f"El dia mas frio del mes fue el {dia_mas_frio} con una temperatura de {menor_temp}")

def dia_mas_agua(mes):      #Día con más agua caída
    os.system("cls")
    mas_agua = []
    for dia in mes:
        agua_caida = dia[3].replace(',', '.')
        agua_caida = float(agua_caida)
        mas_agua.append(agua_caida)
    mayor_caida = max(mas_agua)
    indice = mas_agua.index(mayor_caida)
    dia_mas_agua = mes[indice][0].split('/')[0]
    print(f"El dia con mas agua caida fue {dia_mas_agua}, con una caida de {mayor_caida}")

def total_agua_caida(mes):  #Total de agua caída en el mes
    os.system("cls")
    total = []
    for dia in mes:
        agua_caida = dia[3].replace(',', '.')
        agua_caida = float(agua_caida)
        total.append(agua_caida)
    total_caida = sum(total)
    print(f"El agua caida total es de {total_caida}")

def prom_temp_min(mes):    #Promedio de temperaturas mínimas
    os.system("cls")
    promedio = []
    for dia in mes:
        temp_min = dia[1].replace(',', '.')
        temp_min = float(temp_min)
        promedio.append(temp_min)
    promedio_min = (sum(promedio) / len(promedio))
    print(f"El promedio de temperaturas minimas es {promedio_min}")

def prom_temp_max(mes):     #Promedio de Temperaturas máximas
    os.system("cls")
    promedio = []
    for dia in mes:
        temp_max = dia[2].replace(',', '.')
        temp_max = float(temp_max)
        promedio.append(temp_max)
    promedio_max = (sum(promedio) / len(promedio))
    print(f"El promedio de temperaturas maximas es {promedio_max}")

def dia_inf(mes):  # Días del mes con temperaturas inferiores a 1 grado
    os.system("cls")
    dias = []
    for indice, dia in enumerate(mes):
        inf = dia[1].replace(',', '.')
        inf = float(inf)
        if inf < 1:
            dia_mes = int(mes[indice][0].split('/')[0])
            dias.append(dia_mes)
    print(f"Los días del mes con temperaturas inferiores a 1 grado son: {dias}")