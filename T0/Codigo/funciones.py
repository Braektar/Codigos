import os

def get_input(op):
    inp = input("Indique la opción elegida: ")
    if inp not in {str(i) for i in range(1, op + 1)}:
        print(f" Opcion invalida, debes seleccionar un numero de 1 a {op}")
        inp = get_input(op)
    return int(inp)


def DatosUsuarios(diccionario):
    ruta = os.path.join("Codigo", "usuarios.csv")
    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            usuario, contraseña = linea.strip().split(",")
            diccionario[usuario] = contraseña
    return(diccionario)        

def IniciarSesion(diccionario_usuarios):
    '''
    La función recibe el diccionario de usuarios (con el formato de la función DatosUsuarios)
    Devuelve 1 si inicia sesión correctamente
    Devuelve 0 si falla al iniciar sesión
    '''
    print("** Inicio de sesión **\n")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario not in diccionario_usuarios.keys():
        print("\n-- Usuario no registrado --\n"
              "\nDebe registrar su usuario si quiere iniciar sesión\n")
        return(0)
    else:
        intentos = 1
        while intentos <= 3:
            if contraseña != diccionario_usuarios[usuario]:
                print(f"Contraseña incorrecta, le quedan ({3 - intentos}) intentos\n")
                contraseña = input("Ingrese contraseña: ")
            else:
                print("\n----- Bienvenido -----")
                intentos = 4
                return(1)
            if intentos == 3:
                print("Ha ingresado la contraseña incorrecta demasiadas veces, volviendo al menú principal")
                return(0)
            intentos += 1
