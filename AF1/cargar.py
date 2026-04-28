# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
from collections import defaultdict, namedtuple


def cargar_platos(ruta_archivo: str) -> list:
    Plato = namedtuple("Plato", ["nombre", "categoria", "tiempo_preparacion", "precio", "ingredientes"])
    lista = []
    with open(ruta_archivo, "r") as file:
        for linea in file:
            datos = linea.strip().split(",")
            ingredientes = set(datos[4].split(";"))
            plato = Plato(*datos[:2], int(datos[2]), int(datos[3]), ingredientes)
            lista.append(plato)
    return(lista)


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    diccionario = {}
    with open(ruta_archivo, "r") as file:
        for linea in file:
            datos = linea.strip().split(",")
            diccionario[datos[0]] = datos[1]
    return(diccionario)
