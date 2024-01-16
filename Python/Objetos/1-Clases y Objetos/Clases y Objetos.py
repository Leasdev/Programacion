# Clases y Objetos
"""
class Nombre():                                                     # atributos estaticos
    indentificador = valor 1                   
    indentificador = valor n

indentificador = Nombre()                                           # instancia de la clase
"""
# Atributos
"""
# metodo constructor
class Nombre:                                                       # se va a ejecutar simepre cuando se pase el objeto
    def __init__(self, indetificador1 , ...,indentificador n):      # self: se refiere a si mismo 
        self.indent1 = indetificador1
        ...
        self.indentn = indetificadorn
        
indentificador = Nombre("string", "string", int)                    # cualquier tipo de dato 
"""
# Metodos
"""
class Nombre:                                                       
    def __init__(self, indetificador1 , ...,indentificador n):           
        self.indent1 = indetificador1
        ...
        self.indentn = indetificadorn
        
    def accion(self):                                               # metodo
        sentencia 1
        sentencia n

indentificador = Nombre("string", "string", int)
indentificador.accion()
"""

class Juego:
    def __init__(self, Inombre, Iconsola, Icategoria):
            self.nombre = Inombre
            self.consola = Iconsola
            self.categoria = Icategoria
    
    def abrir(self):
        print("Abriste el juego %s\nCategoria: %s\nConsola: %s\n" %(self.nombre,self.categoria, self.consola))        
    
             
juego1 = Juego("Rocket League", "PC", "Football")
juego2 = Juego("Grim Dawn", "PC", "RPG")

juego1.abrir()
juego2.abrir()