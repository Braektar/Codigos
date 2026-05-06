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

        pass
    
    def repartir_cartas(self):
        # Barajar las cartas y repartirlas de a 1
        pass
    
    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        # Rellenar aquí
    
    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                # Ataca el jugador 1
                # Rellenar aquí
                pass
            else:
                # Ataca el jugador 2
                # Rellenar aquí
                pass


juego = Juego(10)