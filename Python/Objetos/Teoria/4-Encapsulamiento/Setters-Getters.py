# Getters y Setters
"""
class Nombre:
    def__init__(self, nombre1, ..., nombren):
        self.nombre = nombre1
        ...
        self.nombren = nombren
        
    def get_nombre(self)
        return self._nombre
    
    def set_nombre(self):
        self._nombre = nombre
"""
class Persona:
    def __init__(self, nombre, altura):
        self._nombre = nombre
        self._altura = altura
        
    def get_nombre(self):
        return "Nombre: %s\nAltura: %s" %(self._nombre, self._altura)
    
    def set_nombre(self, nuevo):
        self._nombre = nuevo
                
persona = Persona("Leandro", 195)

nombre = persona.get_nombre()
print(nombre)

persona.set_nombre("Pepito")

nuevo = persona.get_nombre()

print(nuevo)