

def verificar_input(opcion: str, rango: int) -> str:
    valores_permitidos = list(range(rango+1))
    if opcion not in valores_permitidos:
        print(f"Opción invalida, debe ingresar un numero de 0 a {rango}")
        return(False)
    else:  
        return(True)


