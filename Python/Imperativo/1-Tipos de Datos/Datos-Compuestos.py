# Tipos de Datos Compuestos

"""
Lista:
indentificador = ["string", entero, float, bool, ....]
indentificador = list("string", entero, float, bool, ....)

Tupla: (no se puede modificar)
indetificador = ("string", entero, float, bool, ....)
indetificador = tuple("string", entero, float, bool, ....)

Conjunto:
indetificador = {"string", entero, float, bool, ....}
indetificador = set("string", entero, float, bool, ....)
indetificador = {frozenset(conjunto), "chau"} # utilizando funcion frozenset (conjunto que no se puede modificar)
Subconjunto:
indetificador = conjunto.issubset(conjunto3) # si es subconjunto (menor)
indetificador = conjunto <= conjunto2
indetificador = conjunto.issuperset(conjunto3) # si es subconjunto (mayor)
indetificador = conjunto >= conjunto2

Diccionario:
indentificador = {
    indetificador1 : "string",
    indetificador2 : entero,
    indetificador3 : float,
    indetificador4 : bool
}
indetificador = dict(
    indetificador1 : "string",
    indetificador2 : entero,
    indetificador3 : float,
    indetificador4 : bool
)
indetificador = dict.fromkeys(["tupla", "apellido"]) # crea un diccionario con los keys de la lista
indetificador = dict.fromkeys("tupla", "apellido") # crea un diccionario con los keys por letra 
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