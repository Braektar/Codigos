from cargar import cargar_platos
from collections import defaultdict

# --- EJEMPLO --- #
# [Plato1, Plato2, Plato2, Plato4]
# pasa a ser
# {"Categoria1": [Plato3, Plato2], "Categoria2": [Plato1, Plato4]}
def platos_por_categoria(lista_platos: list) -> dict:
    informacion_platos = cargar_platos("platos.csv")
    diccionario_final = defaultdict(list)
    for plato in lista_platos:
        for info_plato in informacion_platos:
            if plato == info_plato.nombre:
                categoria = info_plato.categoria
                diccionario_final[categoria].append(info_plato)
    return(diccionario_final)

# Debe devolver los platos que no tengan ninguno de los ingredientes descartados
def descartar_platos(ingredientes_descartados: set, lista_platos: list):
    #asumiendo que namedtuple sigue el patron de cargar_platos
    #por las dudas, aunque ya viene como set, hare una set de nammedtuple.ingredientes
    lista_final = []
    for plato in lista_platos:
        set_ingredientes = plato.ingredientes
        if len(ingredientes_descartados - set_ingredientes) == len(ingredientes_descartados):
            lista_final.append(plato.nombre)
    return(lista_final)


# --- EXPLICACION --- #
# Si el plato necesita un ingrediente que no tiene cantidad suficiente,
# entonces retorna False
#
# En caso que tenga todo lo necesario, resta uno a cada cantidad y retorna True
def preparar_plato(plato, ingredientes: dict) -> bool:
    for ingrediente_plato in plato.ingredientes:
        if ingredientes[ingrediente_plato] <= 0:
            return False

    for ingrediente_plato in plato.ingredientes:
        ingredientes[ingrediente_plato] -= 1

    return True

# --- EXPLICACION --- #
# Debe retornar un diccionario que agregue toda la información ...
#  de la lista de platos.
# precio total, tiempo total, cantidad de platos, platos
def resumen_orden(lista_platos: list) -> dict:
    #Comenzaré asumiendo que la lista es una nammed tuple
    precio = 0
    tiempo = 0
    cantidad = 0
    platos = []
    for plato in lista_platos:
        precio += plato.precio
        tiempo += plato.tiempo
        cantidad += 1
        platos.append(plato.nombre)
    diccionario_final = {
        "precio total": precio,
        "tiempo total": tiempo,
        "cantidad de platos": cantidad,
        "platos": platos
    }
    return(diccionario_final)