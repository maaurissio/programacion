import random
import time
import os

def carrera_caballos(nombres_caballos):
    posiciones = {caballo: 0 for caballo in nombres_caballos}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for caballo in nombres_caballos:
            avance = random.randint(1, 5)
            posiciones[caballo] += avance
            print(f"{caballo}: {'-' * posiciones[caballo]}>") 

            if posiciones[caballo] >= 100:
                return caballo
        time.sleep(0.2)  

if __name__ == "__main__":
    nombres_caballos = ["Seba", "Joshua", "Amaro", "Mauri", "Chelo"]
    ganador = carrera_caballos(nombres_caballos)
    print(f"\n¡El ganador es {ganador}!")
