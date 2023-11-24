#Con esta funcion registro los usuarios y los almaceno
def registrar(nombre,clave):
    
    clientes.update({nombre_usuario : clave_usuario})
    return
#Con esta funcion buscamos que no este registrado
def buscar(nombre):
    ver=clientes.get(nombre)
    return ver

#Con esta funcion recorro la estructura de datos para buscar
def mostrar_todo():
    print("La cantidad de usuarios registrados son:\n ")
    for k, v in clientes.items():
        print(k,v)
    
print("_________________________________________________________________________________")
print("                          Curso Python Coderhouse\n")
print("                  Estas ingresando a la pre-entrega nro 1\n" )
print("                          ¡Bienvenido al sistema!\n    ")
print("_________________________________________________________________________________")

#Creo la estructura, la llamo clientes
clientes={}

#Armo menu de opciones
menu= True
while menu:
    print("\n1: Registrarse")
    print("2: Ingresar")
    print("3: Mostrar estructura (Todos los usuarios y claves)")
    print("4: Cargo la estructura clientes con elementos")
    print("5: Salir\n")
    respuesta= int(input("Ingrese el numero de opcion: "))
    if respuesta == 1:
        nombre_usuario = input("Ingrese un usuario nuevo: ")
        if nombre_usuario in clientes:
            print("Ya se encuentra registrado")
        else:
            clave_usuario = input("Ingrese una clave: ") 
            #llamo a la funcion que cree registar
            registrar(nombre_usuario,clave_usuario)

    elif respuesta == 2:   
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        clave_almacenada=buscar(nombre_usuario)
        clave_usuario = input("Ingrese su clave: ")
        if clave_usuario == clave_almacenada:
            print("Sesion iniciada. ")
        else:
            print("Contraseña incorrecta. ")
    elif respuesta == 3:
        print("mostrar_todo\n")
        mostrar_todo()
    elif respuesta == 4:
        #Cargo con datos genericos los elementos
        clientes={"Facu":"FZavala", "Fran":"Fcoronel","Nacho" : "Imrodriguez","Guille": "GDominguez", "Sole": "Sflores"}
    elif respuesta == 5:
        print("Salir\n\n")
        menu = False
print("¡Hasta la proxima!\n\n") 