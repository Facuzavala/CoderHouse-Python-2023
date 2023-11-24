print("_________________________________________________________________________________")
print("                          Curso Python Coderhouse\n")
print("                  Estas ingresando a la pre-entrega nro 2\n" )
print("                         ¡Bienvenidos al modelo de clientes!\n    ")
print("_________________________________________________________________________________")

#Cree la clase
class Cliente:
#Utilice el constructor
    def __init__(self, nombre, correo, usuario, productos, direccion,categoria):
#Definí los atributos de instancia
        self.nombre=nombre
        self.correo=correo
        self.usuario=usuario
        self.productos=productos
        self.direccion=direccion
        self.categoria=categoria
        
#Utilice metodo __str__
    def __str__(self):
        return f"Sus datos: \nNombre:{self.nombre}\nUsuario:{self.usuario}"
#Utilice metodos con argumento    
    def name_prod(self,nombre_produc):
        print (f"Indique el producto que desea comprar: {nombre_produc}")

    def marca_prod(self,marca_produc):
        print (f"Indique la marca del producto que desea: {marca_produc}")

    def local(self, local_compra):
        print(f"Indique su local de preferencia para realizar la compra: {local_compra}")

    def verifico_email(self,nuevo_email):
        return self.correo == nuevo_email
#Utilice metodos sin argumento    
    def descuento(self):
        if self.categoria == "A":
            print("Por ser categoria A, recibis un descuento del %30 en el total de su compra")
        elif self.categoria == "B":
            print("Por ser categoria B, recibis un descuento del %20 en el total de su compra. Sigue realizando compras para incrementar su categoria")
        elif self.categoria == "C":
            print("Por ser categoria C, recibis un descuento del %15 en el total de su compra. Sigue realizando compras para incrementar su categoria")
        elif self.categoria == "D":
            print("Por ser categoria D, recibis un descuento del %10 en el total de su compra. Sigue realizando compras para incrementar su categoria ")
        else:
            print("¡Debes realizar tu primer compra para obtener una categoria!")

    def comprado(self, nombre, np, mp, tp):
        print (f'El cliente {nombre} se ha comprado un {np} de la marca {mp} en la tienda {tp}.\nLa factura sera enviada a su correo electronico.')

    def atencion(self, calificacion):
        print (f"La atencion recibida la califico con un {calificacion}")

#Cree dos instancias
cliente1 = Cliente("Facundo Zavala", "facu@coder.com", "FZRiver912","Tecnologia", "Mozart 2474", "A")
cliente2 = Cliente("Sandra Vazquez", "Sandri@coder.com", "San65","Hogar", "Montes de Oca 123", "S")

print(cliente1)
cliente1.name_prod("Television")
cliente1.marca_prod("LG")
cliente1.local("Musimundo")
cliente1.descuento()

mail = input("Ingrese su correo electronico para finalizar con la compra: ")
if cliente1.verifico_email(mail):
    print("La compra se realizo correctamente.")
    print("Con su compra reciente, ha subido de categoria. ¡¡¡FELICITACIONES!!!")
else:
    print("El correo electronico introducido es invalido, no se pudo finalizar la compra.")

cliente1.comprado("Facundo", "Televisor", "LG", "Musimundo")
cliente1.atencion(9)

#print(cliente2)
#cliente2.name_prod("Colchon")
#cliente2.marca_prod("Cannon")
#cliente2.local("Cannon")
#cliente2.descuento()

#mail = input("Ingrese su correo electronico para finalizar con la compra: ") 
#if cliente2.verifico_email(mail):
    #print("La compra se realizo correctamente.")
    #print("Con su compra reciente, ha subido de categoria. ¡¡¡FELICITACIONES!!!")
#else:
    #print("El correo electronico introducido es invalido, no se pudo finalizar la compra.")

#cliente2.atencion(7.5)
#cliente2.comprado("Sandra","colchon", "Cannon", "Cannon")
#cliente2.atencion(9)