def signin(valido): #Registro
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
    
    
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    user_name=input("Ingrese su nombre de usuario: ")
    bususer = open('users.txt', "r")
    datos = bususer.read().split(":")
    for user_name in datos:
        while user_name!=datos:
            break
        
        
    users.close()
    


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
    
    while user_name.isalpha() == False: #Comprobación de texto 
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
        user_name=input("Ingrese su nombre de usuario: ")
    name=input("Nombre: ")
    lastname=input("Apellido: ")
    age=input("Edad:")
    
    numg = int(input("Inserte el numero de gustos que desea ingresar"))
    gustos= []
    print("Ingrese por favor su(s) ", {numg},"gusto(s): ")
    for i in range(numg):
        gusto = input("Cuentanos uno de tus gustos: ")
        gustos.append(gusto)

    user_name=("Nombre de usuario (los números y los caracteres especiales no están permitidos): ")
    while user_name!="": #Mientras el campo del user_name no esté vacío
         #verificar si el nombre de usuario no está siendo usado por alguien más
         #Usa la funcion verificar_username, que retorna True si el user name puede ser usar y False si no.
         #El programa continua si y solo si la funcion verificar_username retorna True, es decir, si y solo si el nombre de usuario es válido.
         #verusuarios  es la función que almacena los nuevos nombres de usuario en la lista verusuarios (tienen el mismo nombre)
         while verificar_username(verusuarios)==True:
            passw=("Contraseña: ")
            valpassw=("Contraseña nuevamente: ")
            userinfo=[name, lastname,age,gustos[0-i],user_name,passw]
            return userinfo[0-i]
            


    

def UserName(): #Toma de la lista de la infomación de cada usuario el username escogido y retorna este username.
    username=signin.userinfo[5]
    return username
    
def valpassword(passw,valpassw): #Validacion de contraseñar para Log in
    if passw!=valpassw:
        print("Las contraseñas no coinciden. Verifique.")
:
    
    
def login(): #Ingresar
    user_name=input("Ingrese su nombre de usuario:")
    for user in users:

    passw=input("Ingrese su contraseña: ")
    '''
    Esta funcion nos permite realizar el inicio de sesion de un usuario
    
    '''
    #Buscar que el username ingresado no exista en la base de datos
    #Si este no ha sido ingresadopedir la contraseña
    #Si ya esta registrado pedir la clave
    #Verificar si la clave coincide
    #Si la clave coincide acceder al menu

def menu(): #Aqui podremos ver todo el menu de la redsocial que se activa despues de iniciar sesion
    bandera= False
    print("Hola ", user, " a Redix. Selecione el número de la operación que desea realizar: ")
    print("¿Que deseas hacer hoy? ")
    print("(1) Ver usuarios registrados") 
    print("(2) Enviar  solicitudes de amistad")
    print("(3) Ver solicitudes de amistad pendientes") 
    print("(4) Ver mis mensajes")
    print("(5) Enviar mensaje a un amigo")
    print("(6) Ver amigos recomendados")
    print("(7) Cerrar sesion")
    opciones=int(input())
    while bandera == False:
        if opciones==1:
            fn.verusuarios()
            bandera=True
        elif opciones==2:
            fn.enviarsolicitudesdeamistad()
            bandera=True
        elif opciones ==3:
            fn.solipendientes()
            bandera=True
        elif opciones ==4:
            fn.vermensajes()
            bandera=True
        elif opciones ==5:
            fn.enviarmensajes()
            bandera=True
        elif opciones ==6:
            fn.gustonencomun()
            bandera=True
        elif opciones == 7:
            fn.cerrarsesion()
            bandera=True
        elif opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6 and opcion!=7:
                print ("Opción no válida! Intenta de nuevo con de las opciones válidas porfavor! ")
                print("Hola ", user, " a Redix. Selecione el número de la operación que desea realizar: ")
                print("¿Que deseas hacer hoy? ")
                print("(1) Ver usuarios registrados") 
                print("(2) Enviar  solicitudes de amistad")
                print("(3) Ver solicitudes de amistad pendientes") 
                print("(4) Ver mis mensajes")
                print("(5) Enviar mensaje a un amigo")
                print("(6) Ver amigos recomendados")
                print("(7) Cerrar sesion")
                opciones=int(input())
     
        
def verusuarios(): #Lista de los nombres de los usuarios registrados en la red social
    users=[]
    #Almacena en la lista los nuevos usernames
    #Retorna la lista de los nombres de usuario actualizada
    return users

def verificar_username(verusuarios): 
    #Recibe como argumento la lista donde se almancenan todos los nombres de usuario registrados
    #Esta función recibe el nombre de username que desea usar un nuevo usuario y verifica que no esté siendo usado por alguien más.
    newusername=UserName()
    for i in verusuarios:
        if newusername==verusuarios[i]:
            print("El nombre de usuario ingresado ya existe, porfavor intente con uno diferente. ")
            valido=False
        else:
            valido=True 
    return valido   


def enviarsolicitudesdeamistad(): #Envio de solicitudes a base de lista de amigos
    pass

def listaamigos(): #Informacion almacenada en la lista de amigos
    listaamigos=[]
    return listaamigos[0-i]

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
