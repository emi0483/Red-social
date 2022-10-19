users=[]

def signin(): #Registro
    '''
    Registrar el usuario (Guardar datos como contraseña, nombre de usuario y gustos).
                    
    '''
    ban=False
    while ban==False:
        user_name=input("Ingrese su nombre de usuario: ")
        if verificar_username(user_name)==True:
            ban1=True
            ngus=0
            name=input("Nombre: ")
            lastname=input("Apellido: ")
            age=input("Edad: ")
            passw=input("Contraseña: ")
            valpassw=input("Contraseña nuevamente: ")
            while (ban1==True):
                if (valpassword(passw,valpassw)==True):
                    ngus=0
                    gustos=[]
                    while ngus<3:
                        gusto=input("¿Que te gustaría ver?: ")
                        ngus+=1
                        gustos.append(gusto)
                    ban1=False
                    ban=True
    add_username_pass(user_name,passw)
    #filling_userData(user_name,name,lastname,passw,valpassw,age,friends,gustos)
    return 
    
def filling_userData(username,name,lastname,passw,valpassw,age,friends,gustos):
    file=open("userData.txt",'a')
    file.write(username)
    file.write(":")
    for i in friends:
        file.write(i)
        file.write(",")
    file.write("\n")
    file.write("{")
    for j in gustos:
        file.write(j)
        file.write(",")

def add_username_pass(username, passw):#Esta función recibe la lista de usuarios users y el retorno username de la funcion 
    '''
    Añadir el nombre de usuario a una lista.
                    
    '''
    file=open("users.txt",'a')
    file.write("\n")
    file.write(username)
    file.write(";")
    file.write(passw)
    file.write("\n")
    return
    '''
    Evalúa el nombre de usuario y verifica si existe o no, en caso de que no pida usar uno nuevo.
                    
    '''
    #Esta función recibe el nombre de username que desea usar un nuevo usuario y verifica que no esté siendo usado por alguien más.

def verificar_username(user_name): #Esta función recibe el nombre de username que desea usar un nuevo usuario y verifica que no esté siendo usado por alguien más.
    while user_name.isalpha() == False: #Comprobación de texto 
        user_name=input("Ingrese su nombre de usuario: ")
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
    username=[]
    for z in user_name:
        username.append(z)
    ban=False
    file=open("users.txt","r")
    while ban==False:
        for i in file:
            word=[]
            for j in i:
                if j!=";":
                    word.append(j)
                else:
                    break
            if username==word:
                print("El nombre de usuario ya existe. Intente con uno distinto. ")
                user_name=input("Ingrese su nombre de usuario: ")
                username=[]
                for z in user_name:
                    username.append(z)   
        ban=True
        print("Nombre de usuario válido. Bienvenid@ a REDIX")
    return True
    

def valpassword(passw,valpassw): #Validacion de contraseñar para sign in
    ban=False
    while (ban==False):
        while (passw!=valpassw):
            print ("No válida.")
            passw=input("Contraseña: ")
            valpassw=input("Verificar contraseña: ")
        print("Contraseña válida.")
        ban=True
    return True

def verificar_username_login(user_name): #Esta función recibe el nombre de username que desea usar un nuevo usuario y verifica que no esté siendo usado por alguien más.
    while user_name.isalpha() == False: #Comprobación de texto 
        user_name=input("Ingrese su nombre de usuario: ")
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
    username=[]
    for z in user_name:
        username.append(z)
    ban=False
    file=open("users.txt","r")
    while ban==False:
        for i in file:
            word=[]
            for j in i:
                if j!=";":
                    word.append(j)
                else:
                    break
            if username==word:
                ban=True
                break
        print("El nombre de usuario no está registrado. Verifique e intente nuevamente. ")
        user_name=input("Ingrese su nombre de usuario: ")
        username=[]
        for z in user_name:
            username.append(z)
    return True

def login(): #Ingresar
    user_name=input("Ingrese su nombre de usuario: ")
    verificar_username_login(user_name)
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
            #verusuarios()
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

def gustosencomun(gustos): #Compara los gustos del usuario y lo recomienda como amigos si son similares
    signin()
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
