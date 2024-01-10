#Metodos de diccionarios:

diccionario = {
    "nombre" : 'Leandro',
    "altura" : 195,
    "crack" : True
}

claves = diccionario.keys() # devuelve un objeto dict_item

valor = diccionario.get("altura") #parametro key, y devuelve el valor

diccionario.pop("altura") # elimina un elemento del diccionario

test = diccionario.items() # devuelve todo el diccionario

#diccionario.clear() # elimina el diccionario

print(test)