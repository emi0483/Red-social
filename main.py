import funciones
import funciones as fn
ban=False
print("Bienvenid@ a Redix. Selecione el número de la operación que desea realizar: ")
print("(1) Registro / Sign In") 
print("(2) Ingreso / Log In ")
opcion=int(input())
while ban==False:
    if opcion==1:
        fn.signin()
        fn.menu()
        ban=True
    elif opcion==2:
        fn.login()
        ban=True
    elif opcion!=1 and opcion!=2:
        print ("Opción no válida! Intenta de nuevo con de las opciones válidas porfavor! ")
        print("Bienvenid@ a Redix. Selecione el número de la operación que desea realizar: ")
        print("(1) Registro / Sign In") 
        print("(2) Ingreso / Log In ")
        opcion=int(input())
