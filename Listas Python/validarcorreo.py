correo=input("Ingrese correo: ")
if '@' in correo:
    partes=correo.split('@')
    print(partes) 
    usuario=partes[0]
    dominio=partes[1]
    if len(usuario)>0 and '.' in dominio and len(usuario.replace(" ", ""))!=0 :
        print("Correo válido") 
    else:
        print("Correo peeeeeenca!!!!")
else:
     print("Correo super peeeeeenca!!!!")