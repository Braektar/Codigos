from collections import namedtuple
# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    lista_final = []
    Plato = namedtuple("Plato_type", ["nombre", "categoria", "tiempo", "precio", "ingredientes"])
    with open(ruta_archivo, "rt") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea = linea.strip().split(",")
            flag = True
            nombre = str(linea[0])
            categoria = str(linea[1])
            tiempo = int(linea[2])
            precio = int(linea[3])
            ingredientes = linea[4:]
            # if nombre.isalpha() == False:
            #     print(nombre)
            #     flag = False
            # elif categoria.isalpha() == False:
            #     flag = False
            # elif tiempo.isdigit() == False:
            #     flag = False
            # elif precio.isdigit() == False:
            #     flag = False
            # ingredientes = set(ingredientes)
            # if flag == True:                
            tupla = Plato(nombre, categoria, tiempo, precio, ingredientes)
            lista_final.append(tupla)
    return(lista_final)



    pass


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass


print(cargar_platos("platos.csv"))