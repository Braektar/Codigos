from collections import namedtuple
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    lista_final = []
    Plato = namedtuple("Plato", ["nombre", "categoria", "tiempo", "precio", "ingredientes"])
    with open(ruta_archivo, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea = linea.strip().split(",")
            flag = True
            nombre = str(linea[0])
            categoria = str(linea[1])
            tiempo = int(linea[2])
            precio = int(linea[3])
            ingredientes = linea[4].split(";")
            set_ingredientes = set()
            for ingrediente in ingredientes:
                set_ingredientes.add(ingrediente)            
            tupla = Plato(nombre, categoria, tiempo, precio, set_ingredientes)
            lista_final.append(tupla)
    return(lista_final)

# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    diccionario_ingredientes = {}
    with open(ruta_archivo, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea = linea.strip().split(",")
            nombre = linea[0]
            cantidad = int(linea[1])
            diccionario_ingredientes[nombre] = cantidad
    return(diccionario_ingredientes)

print(cargar_platos)