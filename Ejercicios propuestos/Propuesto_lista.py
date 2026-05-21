import random
from collections import namedtuple

class Juego:
    
    def __init__(self, turnos):
        
        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
    
    def read_file(self):
        # Leer las cartas y guardarlas en una estructura de datos adecuada
        # NOTA: la primera fila del archivo son los atributos de las cartas

        card = namedtuple('Card_type', ['nombre', 'ataque', 'defensa'])

        path = "cards.csv"
        with open(path, "rt") as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            linea = linea.strip().split(",")
            new_card = card(linea[0], linea[1], linea[2])
            self.mazo.append(new_card)
        self.mazo = self.mazo[1:]
    
    def repartir_cartas(self):
        # Barajar las cartas y repartirlas de a 1
        repartir = []
        contador = 1
        while contador <= 10:
            indice = random.randrange(len(self.mazo))
            carta = self.mazo.pop(indice)
            repartir.append(carta)
            contador += 1  
        self.cartas_j1.extend(repartir[0:5])
        self.cartas_j2.extend(repartir[5:10])
                      
    
    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        # Rellenar aquí
        nombre_atacante = atacante.nombre
        nombre_defensor = defensa.nombre
        print(f"Atacante: nombre carta: {nombre_atacante: ^8.8s}, ataque: {ptos_ataque:>5s}")
        # print("-"*50)
        print(f"Defensor: nombre carta: {nombre_defensor: ^8.8s}, defensa: {ptos_defensa:>5s}")
        if ptos_ataque >= ptos_defensa:
            print("Victoria!")
            return("win")
        else:
            print("Derrota!")
            return("lose")


    
    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                # Ataca el jugador 1
                # Rellenar aquí
                numero_carta_1 = random.randrange(len(self.cartas_j1))
                numero_carta_2 = random.randrange(len(self.cartas_j2))
                carta_1 = self.cartas_j1[numero_carta_1]
                carta_2 = self.cartas_j2[numero_carta_2]
                resultado = self.atacar(carta_1, carta_2)
                if resultado == "win":
                    print("Jugador 1 vence")
                    self.cartas_j2.pop(numero_carta_2)
                else:
                    print("Jugador 1 pierde")
                    self.cartas_j1.pop(numero_carta_1)
                pass
            else:
                # Ataca el jugador 2
                # Rellenar aquí
                numero_carta_1 = random.randrange(len(self.cartas_j1))
                numero_carta_2 = random.randrange(len(self.cartas_j2))
                carta_1 = self.cartas_j1[numero_carta_1]
                carta_2 = self.cartas_j2[numero_carta_2]
                resultado = self.atacar(carta_1, carta_2)
                if resultado == "win":
                    print("Jugador 2 vence")
                    self.cartas_j1.pop(numero_carta_1)
                else:
                    print("Jugador 2 pierde")
                    self.cartas_j2.pop(numero_carta_2)
                pass
                if (len(self.cartas_j1)) == 0:
                    print("Jugador 2 gana")
                    return
                elif len(self.cartas_j2) == 0:
                    print("Jugador 1 gana")
                    return


juego = Juego(10)