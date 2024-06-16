from os import system
system("cls")
#persona=[rut, nombre, apellido, correo]
#contactos=[['123', 'Wacoldo', 'Soto', 'wac@ldo.cl'], ['234', 'Diogenes', 'Carrasco', 'di@genes.cl']]
contactos=[] #GLOBAL

def cargardatos(contactos):
    contactos=[]
    f=open('Listas Python/datos.csv','r')
    while True:
        linea=f.readline()
        if not linea:
            break
        #persona=linea.replace('\n','').split(',')
        persona=linea.split(',')
        persona[3]=persona[3].replace('\n','')
        contactos.append(persona)
    f.close()
    return contactos
#FIN CARGAR DATOS

def validar_correo():
    while True:
        correo=input("Ingrese correo: ")
        if '@' in correo and correo.count('@')==1:
            partes=correo.split('@')
            print(partes) 
            usuario=partes[0]
            dominio=partes[1]
            if len(usuario)>0 and '.' in dominio and len(usuario.replace(" ", ""))!=0 and len(dominio)>=3:
                break
            else:
                print("Correo peeeeeenca!!!!")
        else:
            print("Correo super peeeeeenca!!!!")
    return correo
#FIN VALIDAR CORREO

def agregar(contactos, validar_correo):
    while True:
        encontrado=False
        rut=input("Ingrese rut: ")
        for persona in contactos:
            if persona[0]==rut:
                    #print(f"RUT: {persona[0]} NOMBRE: {persona[1]} {persona[2]} E-MAIL: {persona[3]}")
                encontrado=True
                print("EL rut ya está registrado, ingrese otro!!!!!")
                    

        if encontrado==False:
            break
    while True:      
        nombre=input("Ingrese nombre: ")
        if len(nombre)==0:
            print("Debe ingresar un nombre")
        else:
            break

    while True:      
        apellido=input("Ingrese apellido: ")
        if len(apellido)==0:
            print("Debe ingresar un apellido")
        else:
            break
    correo = validar_correo()
    persona=[rut, nombre, apellido, correo]
    #contactos.append(persona)
    f=open('datos.csv','a')
    f.write(f"{rut},{nombre},{apellido},{correo}\n")
    f.close()
    
    print("Persona agregada!!!")
#FIN AGREGAR

def buscar(contactos):
    encontrado=False
    rutbuscado=input("Ingrese rut a buscar: ")
    for persona in contactos:
        if persona[0]==rutbuscado:
            print(f"RUT: {persona[0]} NOMBRE: {persona[1]} {persona[2]} E-MAIL: {persona[3]}")
            encontrado=True
            break

    if encontrado==False:
        print("No encontrado!!!")
#FIN BUSCAR

def eliminar(contactos):
    encontrado=False
    ruttokill=input("Ingrese rut a eliminar: ")
    for persona in contactos:
        if persona[0]==ruttokill:
            print(f"Se pitio a {persona[1]}")
            contactos.remove(persona) #LISTA COMO VARIABLE 
            encontrado=True
            break

    if encontrado==False:
        print("No encontrado!!!")
    print("*****LISTA DESPUES DE ELIMINAR*****")
    print(contactos)
    f=open('datos.csv','w')
    for persona in contactos:
        f.write(f"{persona[0]},{persona[1]},{persona[2]},{persona[3]}\n")
    f.close()
#FIN ELIMINAR

def modificar(contactos):
    pass

def listar(contactos):
    pass

    
while True:
    print(contactos)
    contactos=cargardatos(contactos)
    print(contactos)
    system("cls")
    print(contactos)
    print("REGISTRO DE PERSONAS")
    print("""
1. Agregar Persona
2. Buscar Persona
3. Eliminar Persona
4. Modificar Persona
5. Listar Personas
0. Salir


""")
    
    op=input("Ingrese una opción:" )
    if op=="1":#Agregar
        agregar(contactos, validar_correo)

    elif op=="2":#Buscar
        buscar(contactos)

    elif op=="3":
        eliminar(contactos)
        
    elif op=="4":
        modificar(contactos)
        
    elif op=="5":
        listar(contactos)
    elif op=="0":
        print("Fin del programa....")
        
        break
    else:
        print("Opción no válida")

    input("Presione enter para continuar...")