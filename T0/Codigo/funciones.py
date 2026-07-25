

def get_input(op):
    inp = input("Indique la opción elegida: ")
    if inp not in {str(i) for i in range(1, op + 1)}:
        print(f" Opcion invalida, debes seleccionar un numero de 1 a {op}")
        inp = get_input(op)
    return int(inp)


