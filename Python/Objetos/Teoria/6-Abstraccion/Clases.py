from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, genero, actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer(self):
        pass
    
    def presentar(self):
        print("Me llamo %s tengo %s anios" %(self.nombre, self.edad))
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def hacer(self):
        print("estudio %s" %(self.actividad))
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
        
    def hacer(self):
        print("trabajo de %s" %(self.actividad))        
    
leandro = Estudiante("Leandro", 25, "M", "Programacion")
leandro1 = Trabajador("Leandro", 25, "M", "Nada")

leandro.presentar()
leandro.hacer()
leandro1.presentar()
leandro1.hacer()    