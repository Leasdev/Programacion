#Metodos de diccionarios

"""
idetificador = diccionario.keys()           # devuelve un objeto dict_item
idetificador = diccionario.get("altura")    # parametro key, y devuelve el valor
diccionario.pop("altura")                   # elimina un elemento del diccionario
idetificador = diccionario.items()          # devuelve todo el diccionario
diccionario.clear()                         # elimina el diccionario
"""
diccionario = {
    "nombre" : 'Leandro',
    "altura" : 195,
    "crack" : True
}

claves = diccionario.keys() 

valor = diccionario.get("altura") 

diccionario.pop("altura") 

test = diccionario.items() 