from os import system
system("cls")



while True:
    print("""
1. Registrar Pokemon
2. Listar Pokemon
3. Exportar Pokemon
4. Convertir CSV a JSON
0. Salir
""")
    op = input("\nIngrese una opcion: ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "0":
            break
        case other:
            print("Opcion no valida")