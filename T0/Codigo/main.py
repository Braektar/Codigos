from menu import (
    Inicio,
    Usuario
)
from funciones import (
    get_input,
    DatosUsuarios,
    IniciarSesion,
    CrearUsuario,
    InicioAdmin
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
            respuesta = get_input(4)
        # Menu principal        

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
            estado_menu == 1

        elif estado_menu == 0 and respuesta == 3:
            resultado_admin = InicioAdmin()
            pass


        ## Menú usuario
        if estado_menu == 1:
            Usuario()
            respuesta = get_input(5)

            if respuesta == 5:
                estado_menu = 0

            elif respuesta == 1:
                pass


            
        
    pass

            


if __name__ == "__main__":
    main()

