from menu import (
    Inicio
)
from funciones import (
    get_input
)


def main():

    print("---- Bienvenid@ a DCCorreos de Chile ---\n")

    estado_menu = 0
    programa_encendido = True

    while programa_encendido:
        if estado_menu == 0:
            Inicio()

        # Menu principal
        respuesta = get_input(4)

        if estado_menu == 0 and respuesta == 4:
            print("\n"+"*"*30)
            print(
                "\n Muchas gracias por confiar en nosotros\n"
                "Atentantemente\n"
                "DCCoreos"
                )
            print("\n"+"*"*30)
            programa_encendido = False
        elif estado_menu == 0 and respuesta == 1:

            pass
    pass

            


if __name__ == "__main__":
    main()

