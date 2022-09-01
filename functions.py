import main.py

def signin(): #Registro
    '''
    Funcion con el objetivo de hacer el registro de usuarios.
    Los procesos realizados adentro de esta funcion son:
        - Pedirle al cliente que ponga su usuario y con esta toma opciones si:
            1. Hace parte de los usuarios ya registrados y por tanto no es posible registrarlo.
                1.1 Preguntar al usuario si desea acceder al menu de ingresor.
            2. No hace parte de los usarios registrados.
                2.1 El usuario ingresado no cumple con las caracteristicas solicitadas.
                2.2 El usuario ingresado es correcto.
                    2.2.1 Pedir la contraseña al usuario y al verificarla esta sea la misma
                    2.2.2 Pedir la lista de gustos del usuario
                        Pedir al usuario
                2.3 Almacenar la informacion.
                    
    '''
    
    print ("Bienvenid@ a Redix. En este Porfavor llena el formulario para realizar tu registro.")
    
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    user_name=input("Ingrese su nombre de usuario: ")
    
    #USAR PARA VALIDAR SI ES UN NUMERO O NO, ADEMAS DE QUE LOGRA VERIFICAR TAMBIEN SIMBOLOS COSAS QUE LAS 
        # FUNCIONES is.. no nos permiten.
    #ban=False
    #while not ban:
        #try:
            #num1 = int(input("\nEnter a number: "))
            #ban=True
        #except ValueError:
            #print ("The entry is not an int number. Please try again")
            
    #total = num1 + 100
    #print("The result is ", total)
    
    while user_name.isalpha() == False: #Comprobacion de texto 
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
        user_name=input("Ingrese su nombre de usuario: ")
    
    name=input("Nombre: ")
    lastname=input("Apellido: ")
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    age=input("Edad:")
    
    numg = int(input("Inserte el numero de gustos que desea ingresar"))
    gustos= []
    print("Ingrese por favor su(s) ", {numg},"gusto(s): ")
    for i range(numg):
        gusto = input(Cuentanos uno de tus gustos)
        gustos.append(gusto)

    user_name=("Nombre de usuario (los números y los caracteres especiales no están permitidos): ")
    passw=("Contraseña: ")
    valpassw=("Contraseña nuevamente: ")
    
def valpassword(passw,valpassw): #Validacion de contraseñar para Log in
    if passw!=valpassw:
        print("Las contraseñas no coinciden. Verifique.")
    
def login(): #Ingresar
    
    '''
    Esta funcion nos permite realizar el inicio de sesion de un usuario
    
    '''
    #Buscar que el username ingresado no exista en la base de datos
    #Si este no ha sido ingresadopedir la contraseña
    #Si ya esta registrado pedir la clave
    #Verificar si la clave coincide
    #Si la clave coincide acceder al menu

def menu(): #Aqui podremos ver todo el menu de la redsocial que se activa despues de iniciar sesion
     verusuarios()
     listaamigos()
     solipendientes()
     #Ver amigoss recomendados por gustos
        
def verusuarios(): #Lista de los nombres de los usuarios registrados en la red social
    pass

def enviarsolicitudesdeamistad(): #Envio de solicitudes a base de lista de amigos
    pass

def listaamigos():
    pass

def solipendientes():#Muestra las solicitudes de amistad y permite aceptarlas o rechazarlas
    pass

def gustosencomun(): #Compara los gustos del usuario y lo recomienda como amigos si son similares
    pass

def vermensajes():
    pass

def enviarmensajes(): #Permite enviar imagenes a tus amigos
    pass

def cerrarsesion(): #Cierra sesion y guarda informacion
    pass
