# Encapsulamiento
"""
class Nombre:
    def__init__(self):
        self._identificador = nombre            # _ atributo privado
        
class Nombre:
    def__init__(self):
        self.__identificador = nombre            # __ atributo mas privado        

"""
class Clase:
    def __init__(self):
        self._privado = "Valor"
        
class Clases:
    def __init__(self):
        self.__privado = "Valor"
        
objeto = Clase()

print(objeto._privado)