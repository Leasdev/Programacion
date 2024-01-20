# Herencia Multiple
"""
identificador.__init__(self, nombre)            # hereda de la clase especifica
super().nombreFuncion()                         # Toma el primer parametro asignado de la clase, y ejecuta la funcion
self.nombreFuncion()                            # Toma de la misma clase la funcion
identificador = issubclass(subclase, clase)     # Devuelve True si la corresponde su herencia
identificador = isinstance(objetoclase, clase)  # Devuelve True si la corresponde la instancia   
"""
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        print("muestro") 
        
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrarHabilidad(self):
        print("no muestro")
                  
class EmpleadoArtista(Persona, Artista):     
    def __init__(self, habilidad):
        Artista.__init__(self, habilidad)

    def mostrar(self):
        super().mostrarHabilidad()              
            
empleado = EmpleadoArtista("baila")

empleado.mostrar()