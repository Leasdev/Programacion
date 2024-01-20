# Herencia
"""
class Nombre:                                                       
    def __init__(self, idetificador1 , ...,identificador n):           
        self.ident1 = idetificador1
        ...
        self.identn = idetificadorn
        
class Nombre2(Nombre):
    def __init__(self, idetificador1 , ...,identificador n, nuevoIdentificador 1, nuevoIdentificador n):
        super().init(idetificador1 , ...,identificador n)                                                     # main class
        self.Nident1 = nuevoIdentificador 1
        ...
        self.Nidentn = nuevoIdentificador n
"""
class Humano:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        
class Sexo(Humano):
    def __init__(self, nombre, altura, peso, hombre, mujer):
        super().__init__(nombre, altura, peso)
        self.hombre = hombre
        self.mujer = mujer
        
    def presentar(self):
        print("Nombre: %s \nAltura: %s \nPeso: %s kg \nGenero: %s" %(self.nombre, self.altura, self.peso, self.hombre))
        
persona = Sexo("Leandro", 195, 78, "Masculino", "Femenino")

persona.presentar()