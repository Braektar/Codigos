import os
from parametros import (
    MIN_CARACTERES,
    LARGO_CONTRASENA,
    RUTA_USUARIOS
)

ruta = RUTA_USUARIOS

def get_input(op):
    inp = input("Indique la opción elegida: ")
    if inp not in {str(i) for i in range(1, op + 1)}:
        print(f" Opcion invalida, debes seleccionar un numero de 1 a {op}")
        inp = get_input(op)
    return int(inp)


def DatosUsuarios(diccionario = dict(), ruta = ruta):
    
    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            usuario, contraseña = linea.strip().split(",")
            diccionario[usuario] = contraseña
    return(diccionario)        

def IniciarSesion(diccionario_usuarios: dict):
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

def CrearUsuario(ruta = ruta):
    diccionario = DatosUsuarios()
    set_usuarios = set(diccionario.keys())
    print("** Bienvenido a la pestaña de creación de usuario **\n")
    print("Instrucciones: \n")
    print(f"El nombre de usuario debe tener un largo minimo de {MIN_CARACTERES} \n")
    nombre = input("Ingrese nombre de usuario: ")
    if nombre in set_usuarios:
        print("Nombre de usuario ya existe\n")
        return(diccionario)
    elif len(nombre) < MIN_CARACTERES:
        print("Nombre de usuario tiene un largo menor al permitido\n")
    else:
        print(f"La contraseña debe tener un largo minimo de {LARGO_CONTRASENA} caracteres\n")
        contraseña = input("Ingrese contraseña: ")
        if len(contraseña) < LARGO_CONTRASENA:
            print("El largo de contraseña es menor al permitido\n")
            return(diccionario)
        else:
            print("Usuario ingresado correctamente")
            diccionario[nombre] = contraseña
            with open(ruta, "wt") as archivo:
                for usuario, contraseña in diccionario.items():
                    fila = [usuario, contraseña]
                    fila_en_texto = ",".join(fila) + "\n"
                    archivo.write(fila_en_texto)
            return(diccionario)