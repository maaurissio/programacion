from os import system
from fun import *
system("cls")

mes = []

while True:
    mes = cargar_datos(mes)
    print("""
    1. Fecha del día con mayor temperatura. 
    2. Día más frío del mes. 
    3. Día con más agua caída. 
    4. Total de agua caída en el mes. 
    5. Promedio de temperaturas mínimas. 
    6. Promedio de Temperaturas máximas. 
    7. Días del mes con temperaturas inferiores a 1 grado.
    0. Salir.
    """)
    try:
        op = input("Ingrese una opción: ")
        match op:
            case "1":
                fecha_mayor_temperatura(mes)
            case "2":
                dia_mas_frio(mes)
            case "3":
                dia_mas_agua(mes)
            case "4":
                total_agua_caida(mes)
            case "5":
                prom_temp_min(mes)
            case "6":
                prom_temp_max(mes)
            case "7":
                dia_inf(mes)
            case "0":
                print("Saliendo...")
                break
            case other:
                print("Opción no válida")
                input("Presione Enter para continuar...")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por teclado")
        break
