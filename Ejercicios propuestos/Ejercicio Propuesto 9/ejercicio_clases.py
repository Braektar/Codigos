class Alumno:
    
    def __init__(self, nombre, apellido, numero_alumno):
        #Completar
        self.nombre = nombre
        self.apellido = apellido
        self.numero_alumno = numero_alumno
        self.clases = []

class Sala:
    
    def __init__(self, lista_alumnos, numero_sala, sigla):
        #Completar
        self.lista_alumnos = lista_alumnos
        self.numero_sala = numero_sala
        self.sigla = sigla
    
    def ingresar_alumno(self, alumno):
        #Completar
        diccionario = {}
        for alumno_sala, numero_sala in self.lista_alumnos:
            diccionario[alumno_sala] = numero_sala
        flag = False
        if alumno.nombre in diccionario.keys():
            if alumno.numero_alumno == diccionario[alumno.nombre]:
                flag = True
        if flag:
            alumno.clases.append(self.sigla)
            print(f"{alumno.nombre} {alumno.apellido} ha ingresado a la sala {self.numero_sala} - {self.sigla}")
        else:
            print(f"{alumno.nombre} {alumno.apellido} se ha intentado colar a la salda {self.numero_sala} - {self.sigla}")
        return()
    
javier = Alumno("Javier", "Gomez", "18639942")
josefa = Alumno("Josefa", "Paz", "16645578")
tomas = Alumno("Tomas", "Gonzalez", "19638225")

sala = Sala([("Michael", "19643721"),("Silvana", "18632890"),("Tomas", "19638225"),
             ("Josefa", "16645578"),("Javier", "16665798"),("", "")], 666, "IIC2233")
sala.ingresar_alumno(javier)
sala.ingresar_alumno(josefa)
sala.ingresar_alumno(tomas)

print(josefa.clases)