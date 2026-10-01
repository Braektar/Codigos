from funciones import get_input, Error2, DatosUsuarios
from parametros import MAX_PESO
from parametros import RUTA_ENCOMIENDAS, RUTA_RECLAMOS
from datetime import datetime


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
    print("[4] Cerrar sesión\n")

    return()

def Admin():
    print("** Menú de administrador **\n")
    print("[1] Actualizar encomiendas")
    print("[2] Revisar reclamos")
    print("[3] Cerrar sesión\n")
    return()




def Encomiendas(usuarios_registrados: set):
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
                peso = str(peso)

        # Destino
        while flag_destino:
            print("\n\nIngrese la dirección destino\n" \
            "El nombre del destino no puede tener comas (,)\n")
            destino = input("Ingrese la dirección del destino: ")
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
    ruta = RUTA_ENCOMIENDAS
    filas = []

    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        fila = linea.strip().split(',')
        filas.append(fila)

    ahora = datetime.now()
    hora_formateada = ahora.strftime("%Y/%m/%d %H:%M:%S")
    fila = [nombre, receptor, peso, destino, hora_formateada, "Emitida"]
    filas.append(fila)

    with open(ruta, "wt") as archivo:
        for fila in filas:
                fila_en_texto = ",".join(fila) + "\n"
                archivo.write(fila_en_texto)
    return(1)           

def EstadoEncomienda(usuario_activo: str):
    ruta = RUTA_ENCOMIENDAS
    encomiendas = []
    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        linea = linea.strip().split(',')
        nombre, usuario,_, _, _, estado = linea
        if usuario == usuario_activo:
            encomiendas.append([nombre, estado])

    print("** Estado de encomiendas **\n\n" \
    f"Usuario activo: << {usuario_activo} >> \n")
    for encomienda in encomiendas:
        nombre, estado = encomienda        
        print(f"\nNombre de encomienda: {nombre}\n"
              f"Estado de encomienda: {estado}")
        print("-"*100)
    return(1)
        
def RealizarReclamo(usuario_activo: str):
    print("** Menu de reclamos **\n\n")
    print("Usted está a punto de realizar un reclamo\n" \
    "Si quiere continuar, presione [1]\n" \
    "Si quire volver, presione [2]\n")
    respuesta = get_input(2)

    if respuesta == 2:
        return(1)

    titulo = input("Ingrese el titulo de su reclamo: ")
    print()
    descripcion = input("Ingrese la descripción de su reclamo: ")

    reclamo = [usuario_activo, titulo, descripcion]
    ruta = RUTA_RECLAMOS
    reclamos = []

    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        fila = linea.strip().split(',')
        reclamos.append(fila)
    reclamos.append(reclamo)

    with open(ruta, "wt") as archivo:
        for fila in reclamos:
                fila_en_texto = ",".join(fila) + "\n"
                archivo.write(fila_en_texto)

    print(">>> Reclamo realizado correctamente <<<")
    return(1)

def ActualizarEncomiendas():
    print("** Encomiendas registradas **\n\n")

    print("   "
    "|      Nombre artículo      |    Receptor    |  Peso  |   Destino   |      Estado      |\n")

    Encomiendas = {}
    ruta = RUTA_ENCOMIENDAS

    # Lectura de archivo
    with open(ruta, "rt") as archivo:
        lineas = archivo.readlines()

    # Preparación de diccionario de encomiendas
    indice = 0
    for linea in lineas:
        fila = linea.strip().split(',')
        Encomiendas[indice] = fila
        nombre, receptor, peso, destino, _, estado = fila
        if indice != 0:
            peso = float(peso)
            print(f"[{indice}]"
                f" {nombre:^27.26s}|"
                f" {receptor:^15.14s}|"
                f" {peso:^7.1f}|"
                f" {destino:<12.11s}|"
                f" {estado:^17.16s}|")
        indice += 1

    print(f"\n[{indice}] Volver")

    seleccion = get_input(indice)
    if seleccion == indice:
        print("Volviendo al menu anterior ...\n\n")
        return(2)

    estados = ["Emitida", "Revisada por agencia", "En camino", "Llegada al destino"]
    nombre, receptor, peso, destino, hora, estado_encomienda = Encomiendas[seleccion]

    contador = 0
    while contador < len(estados):
        if contador + 1 == len(estados):
            print("\n !! La encomienda ya se encuentra finalizada !!\n\n"
                  "Volviendo al menú anterior ...\n\n")
            return(2)
        if estados[contador] == estado_encomienda:
            estado_encomienda = estados[contador + 1]
            print(f"\nEl estado de la encomienda {nombre} fue actualizado exitosamente a < {estado_encomienda} >\n\n")
            contador = len(estados)
        contador += 1

    Encomiendas[seleccion] = [nombre, receptor, peso, destino, hora, estado_encomienda]

    with open(ruta, "wt") as archivo:
            for fila in Encomiendas.values():
                    fila_en_texto = ",".join(fila) + "\n"
                    archivo.write(fila_en_texto)

    return(2)

def RevisarReclamos():
    # Formato reclamos = usuario,titulo,descripcion

    diccionario_reclamos = {}
    


    return(2)