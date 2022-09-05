import funciones
import funciones as fn
ban=False
print("Bienvenid@ a Redix. Selecione el número de la operación que desea realizar: ")
print("(1) Registro / Sign In") 
print("(2) Ingreso / Log In ")
print("(3) Cerrar programa")
opcion=int(input())
while ban==False:
    if opcion==1:
        fn.signin()
        ban=True
    elif opcion==2:
        fn.login()
        ban=True
    elif opcion==3:
        print("Que tengas bonito dia, Vuelve pronto a Redix" )
        ban=true
    elif opcion!=1 and opcion!=2 and opcion!3:
        print ("Opción no válida! Intenta de nuevo con de las opciones válidas porfavor! ")
        print("Bienvenid@ a Redix. Selecione el número de la operación que desea realizar: ")
        print("(1) Registro / Sign In") 
        print("(2) Ingreso / Log In ")
        print("(3) Cerrar programa")
        opcion=int(input())
user = fn.userName()
