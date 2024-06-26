from os import system
system("cls")

trabajadores = []

def cargar_trabajadores(trabajadores):
    with open('trabajadores.csv', 'r', encoding='utf-8') as archivo:
        next(archivo)  # Salta la primera línea del archivo
        for linea in archivo:
            trabajadores.append(linea.strip().split(','))
    return trabajadores

while True:
    print(trabajadores)
    trabajadores = cargar_trabajadores(trabajadores)
    print(trabajadores)
    print("""
1. Calcular sueldo
2. Mostrar resumen
3. Generar archivo de liquidación
0. Salir
""")
    op = input('\nIngrese opcion: ')
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "0":
            break
        case other:
            print("Opcion no valida")