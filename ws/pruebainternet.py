import speedtest

def prueba():
    try:
        st = speedtest.Speedtest()
        print("Probando velocidad de internet...")
        velocidad_descarga = st.download() / 1000000
        velocidad_subida = st.upload() / 1000000
        print("Velocidad de descarga: {:.2f} Mbps".format(velocidad_descarga))
        print("Velocidad de descarga: {:.2f} Mbps".format(velocidad_subida))
    except speedtest.SpeedtestException as e:
        print(f"Se ha producido un error durante la prueba: {str(e)}")

prueba()