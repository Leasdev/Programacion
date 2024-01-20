# Tipos de Datos Compuestos

"""
Lista:
identificador = ["string", entero, float, bool, ....]
identificador = list("string", entero, float, bool, ....)

Tupla: (no se puede modificar)
identificador = ("string", entero, float, bool, ....)
identificador = tuple("string", entero, float, bool, ....)

Conjunto:
identificador = {"string", entero, float, bool, ....}
identificador = set("string", entero, float, bool, ....)
identificador = {frozenset(conjunto), "chau"} # utilizando funcion frozenset (conjunto que no se puede modificar)
Subconjunto:
identificador = conjunto.issubset(conjunto3) # si es subconjunto (menor)
identificador = conjunto <= conjunto2
identificador = conjunto.issuperset(conjunto3) # si es subconjunto (mayor)
identificador = conjunto >= conjunto2

Diccionario:
identificador = {
    idetificador1 : "string",
    idetificador2 : entero,
    idetificador3 : float,
    idetificador4 : bool
}
identificador = dict(
    identificador1 : "string",
    identificador2 : entero,
    identificador3 : float,
    identificador4 : bool
)
identificador = dict.fromkeys(["tupla", "apellido"])     # crea un diccionario con los keys de la lista
identificador = dict.fromkeys("tupla", "apellido")       # crea un diccionario con los keys por letra 
"""
lista = ["Leandro", "Sun", 1.95, True]

tupla = ("Leandro", "Sun", 1.95, True)

conjunto = {"Leandro", "Sun", 1.95, True}

diccionario = {
    "nombre" : "Leandro",
    "apellido" : "Sun",
    "altura" : 1.95,
    "crack" : True
}