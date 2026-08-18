from menu import (
    Inicio
)
from funciones import (
    get_input,
    DatosUsuarios,
    IniciarSesion,
    CrearUsuario
)

def ApagarPrograma():
    print("\n"+"*"*30)
    print(
        "\n Muchas gracias por confiar en nosotros\n"
        "Atentantemente\n"
        "DCCoreos"
        )
    print("\n"+"*"*30)
    return(False)


def main():

    print("---- Bienvenid@ a DCCorreos de Chile ---\n")
    diccionario_usuarios = DatosUsuarios(dict())
    usuarios_registrados = set(diccionario_usuarios.keys())

    estado_menu = 0
    programa_encendido = True

    while programa_encendido:
        if estado_menu == 0:
            Inicio()

        # Menu principal
        respuesta = get_input(4)

        ## Estado menu = 0 (Ventana inicial)
        ## Apagar programa
        if estado_menu == 0 and respuesta == 4:
            programa_encendido = ApagarPrograma()

        ## Iniciar sesión como usuario
        elif estado_menu == 0 and respuesta == 1:
            estado_menu = IniciarSesion(diccionario_usuarios) # devuelve 1 si inicia correctamente, 0 si no            

        ## Registrarse como usuario
        elif estado_menu == 0 and respuesta == 2:
            diccionario_usuarios = CrearUsuario()
            pass
    pass

            


if __name__ == "__main__":
    main()

