print("******TEST*******")
contactos=[]

f=open('datos.txt','r')
while True:
    linea=f.readline()
    if not linea:
        break
    #persona=linea.replace('\n','').split(',')
    persona=linea.split(',')
    persona[3]=persona[3].replace('\n','')
    contactos.append(persona)


