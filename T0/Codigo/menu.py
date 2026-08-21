from funciones import get_input, Error2, DatosUsuarios
from parametros import MAX_PESO

def Inicio():
    print("** Menú de Inicio **\n")
    print("Selecciona una de las siguientes opciones:\n \n")
    print("[1] Iniciar sesión como usuario")
    print("[2] Registrarse como usuario")
    print("[3] Iniciar sesión como administrador")
    print("[4] Salir del programa \n")

    return()

def Usuario():
    print("** Menú de usuario **\n")
    print("[1] Hacer encomienda")
    print("[2] Revisar estado de encomiendas realizadas")
    print("[3] Realizar reclamos")
    print("[4] Ver el estado de los pedidos personales")
    print("[5] Cerrar sesión\n")

    return()

def Admin():
    print("** Menú de administrador **\n")
    print("[1] Actualizar encomiendas")
    print("[2] Revisar reclamos")
    print("[3] Cerrar sesión\n")
    return()




def Encomiendas(usuarios_registrados: set):
    print(usuarios_registrados)
    print("** Ha seleccionado el menú de encomiendas **\n\n" \
          
    "Se le solicitará los siguientes campos\n \n"
    "- Nombre de articulo\n"
    "- Nombre de receptor\n"
    "- Peso del articulo \n" \
    "- Destino\n \n"
    "Indique el nombre del articulo que va a ingresar \n >> tenga en consideración " \
    "que el nombre no puede tener comas (,)\n\n")
    flag = True
    flag_nombre = True
    flag_receptor = True
    flag_peso = True
    flag_destino = True
    while flag:
        ## ingreso nombre
        while flag_nombre:
            nombre = input("Ingrese nombre del artículo: ")
            if "," in nombre:
                print("Valor ingresado correcto, contiene una coma (,) en el nombre\n")
                respuesta = Error2()
                if respuesta == 2:
                    return(0)
            else:
                flag_nombre = False

        ## ingreso receptor
        while flag_receptor:
            print("\nIngrese el nombre del receptor del articulo \n\n" \
            "El nombre del usuario debe ser el mismo que el registrado en la plataforma\n" \
            "Le solicitamos que si el usuario no está registrado, que cree un usuario nuevo\n\n")

            receptor = input("Ingrese nombre del receptor: ")
            if receptor not in usuarios_registrados:
                print("\nEl receptor no se encuentra ingresado como usuario en la plataforma\n")
                respuesta = Error2()
                if respuesta == 2:
                    return(0)
            else: 
                flag_receptor = False

        ## Ingreso peso
        while flag_peso:
            print("\n\nIngrese el peso del articulo\n" \
            f">> tenga en consideración que el peso máximo permitido es {MAX_PESO}\n\n")
            peso = int(input("Ingrese el peso del articulo: "))
            if peso > MAX_PESO:
                print("\n ¡¡ Alerta !! \nPeso del artículo excede peso permitido")
                respuesta = Error2()
                if respuesta == 2:
                    return(0)
            else:
                flag_peso = False

        # Destino
        while flag_destino:
            destino = input("Ingrese nombre del artículo: ")
            if "," in destino:
                print("Valor ingresado correcto, contiene una coma (,) en el nombre\n")
                respuesta = Error2()
                if respuesta == 2:
                    return(0)
            else:
                flag_destino = False

        if flag_nombre == False and flag_destino == False and flag_peso == False and flag_receptor == False:
            flag = False

    print("\n¡Encomienda ingresada al sistema de forma exitosa!\n")
    print("Datos de la encomienda ingresada:\n" \
    f" -Nombre de encomienda: {nombre}\n -Nombre de receptor: {receptor}\n -Peso de encomienda: {peso}\n"
    f" -Destino de encomienda: {destino}")

    
                

    pass

Encomiendas(set(DatosUsuarios().keys()))