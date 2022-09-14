users=[]

def signin(): #Registro
    '''
    Registrar el usuario (Guardar datos como contraseña, nombre de usuario y gustos).
                    
    '''
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    user_name=input("Ingrese su nombre de usuario: ")
    verificar_username()
    while verificar_username()==False:
        user_name=input("Ingrese su nombre de usuario: ")
    return

    while user_name.isalpha() == False: #Comprobación de texto 
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
        user_name=input("Ingrese su nombre de usuario: ")
    verificar_username()
    if verificar_username()==True:
        print ("Nombre de usuario válido. Bienvenid@ a Redix @",user_name)
    name=input("Nombre: ")
    lastname=input("Apellido: ")
    age=input("Edad:")
    numg = int(input("Inserte el numero de gustos que desea ingresar"))
    gustos= []
    print("Ingrese por favor su(s) ", {numg},"gusto(s): ")
    for i in range(numg):
        gusto = input("Cuentanos uno de tus gustos: ")
        gustos.append(gusto)
        passw=("Contraseña: ")
        valpassw=("Contraseña nuevamente: ")
        userinfo=[name, lastname,age,map(gustos),user_name,passw] #La función 'map()' permite mostrar todos los elemetos al interior de una lista.
        print(map(userinfo))
        return map(userinfo)

def add_username(users,username):#Esta función recibe la lista de usuarios users y el retorno username de la funcion 
    '''
    Añadir el nombre de usuario a una lista.
                    
    '''
    users.append(username)
    return
        
def verificar_username(): 
    '''
    Evalúa el nombre de usuario y verifica si existe o no, en caso de que no pida usar uno nuevo.
                    
    '''
    #Esta función recibe el nombre de username que desea usar un nuevo usuario y verifica que no esté siendo usado por alguien más.
    valido=False
    username=input("Ingrese su nombre de usuario: ")
    for i in users:
        while valido!=False:
            if username==i:
                print("El nombre de usuario ingresado ya existe, intente con uno distinto. ")
                username=input("Ingrese su nombre de usuario: ")
    valido=True
    users.append(username)
    return valido         
    
    

def valpassword(passw,valpassw): #Validacion de contraseñar para Log in
    '''
    Valida que la contraseñas sean iguales para realizar el registro y también el ingreso.

    '''
    if passw!=valpassw:
        print("Las contraseñas no coinciden. Verifique.")    

def UserName(): #Toma de la lista de la infomación de cada usuario el username escogido y retorna este username.
    '''
    Busca la información del documento donde se guarda la información del username escogido.
    '''
    username=signin.userinfo[5]
    return username

def login(): #Ingresar
    user_name=input("Ingrese su nombre de usuario:")
    for user in users:
        verificar_username()
    passw=input("Ingrese su contraseña: ")
    
    #Buscar que el username ingresado no exista en la base de datos
    #Si este no ha sido ingresadopedir la contraseña
    #Si ya esta registrado pedir la clave
    #Verificar si la clave coincide
    #Si la clave coincide acceder al menu

def menu(user): #Aqui podremos ver todo el menu de la redsocial que se activa despues de iniciar sesion
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
            verusuarios()
            bandera=True
        elif opciones==2:
            enviarsolicitudesdeamistad()
            bandera=True
        elif opciones ==3:
            solipendientes()
            bandera=True
        elif opciones ==4:
            vermensajes()
            bandera=True
        elif opciones ==5:
            enviarmensajes()
            bandera=True
        elif opciones ==6:
            gustosencomun()
            bandera=True
        elif opciones == 7:
            cerrarsesion()
            bandera=True
        elif opciones!=1 and opciones!=2 and opciones!=3 and opciones!=4 and opciones!=5 and opciones!=6 and opciones!=7:
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
     

def enviarsolicitudesdeamistad(): #Envio de solicitudes a base de lista de amigos
    pass

def listaamigos(): #Informacion almacenada en la lista de amigos
    listaamigos=[]
    return listaamigos[:-1]

def solipendientes():#Muestra las solicitudes de amistad y permite aceptarlas o rechazarlas
    pass

def gustosencomun(): #Compara los gustos del usuario y lo recomienda como amigos si son similares
    signin()
    gustos=signin.userinfo[3]
    for i in gustos:
        return

def vermensajes():
    pass

def enviarmensajes(): #Permite enviar imagenes a tus amigos
    pass
        
def cerrarsesion(): #Cierra sesion y guarda informacion
# Escribe un mensaje en un fichero

    verisalida = int(input("¿Esta seguro que desea cerrar sesion? \n 1.Si, deseo cerrar sesion. \n 2.No. deseo continuar con mi sesion abierta."))
    if verisalida == 1:
        cierre = open('users.txt', "r")
        
        print ("Fin de la sesion \n Gracias por usar Redix")
        cierre.close()
    elif verisalida == 2:
        if verisalida !=1 and verisalida!=2:
            verisalida= int(input("¿Esta seguro que desea cerrar?"))
                          
