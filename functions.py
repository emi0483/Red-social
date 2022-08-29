def signin():
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    user_name=input("Ingrese su nombre de usuario: ")
    while user_name.isalpha() == False:
        print ("Recuerde que no debe incluir números ni caractéres especiales.")
        user_name=input("Ingrese su nombre de usuario: ")
    
def login():
    print ("Bienvenid@ a Redix. Porfavor llena el formulario para realizar tu registro.")
    name=input("Nombre: ")
    lastname=input("Apellido: ")
    print ("Recuerde que no debe incluir números ni caractéres especiales.")
    age=input("Edad:")
    user_name=("Nombre de usuario (los números y los caracteres especiales no están permitidos): ")
    passw=("Contraseña: ")
    valpassw=("Contraseña nuevamente: ")

def valpassword(passw,valpassw):
    if passw!=valpassw:
        print("Las contraseñas no coinciden. Verifique.")