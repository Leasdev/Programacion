# Clases y Objetos
"""
class Nombre():                                                     # atributos estaticos
    identificador = valor 1                   
    identificador = valor n

identificador = Nombre()                                           # instancia de la clase
"""
# Atributos
"""
# metodo constructor
class Nombre:                                                       # se va a ejecutar simepre cuando se pase el objeto
    def __init__(self, idetificador1 , ...,identificador n):        # self: se refiere a si mismo 
        self.indent1 = idetificador1
        ...
        self.identn = idetificadorn
        
identificador = Nombre("string", "string", int)                    # cualquier tipo de dato 
"""
# Metodos
"""
class Nombre:                                                       
    def __init__(self, idetificador1 , ...,identificador n):           
        self.ident1 = idetificador1
        ...
        self.identn = idetificadorn
        
    def accion(self):                                               # metodo
        sentencia 1
        sentencia n

identificador = Nombre("string", "string", int)
identificador.accion()
"""

class Juego:
    def __init__(self, Inombre, Iconsola, Icategoria):
            self.nombre = Inombre
            self.consola = Iconsola
            self.categoria = Icategoria
    
    def abrir(self):
        print("Abriste el juego %s\nCategoria: %s\nConsola: %s" %(self.nombre,self.categoria, self.consola))
               
juego1 = Juego("Rocket League", "PC", "Football")
juego2 = Juego("Grim Dawn", "PC", "RPG")