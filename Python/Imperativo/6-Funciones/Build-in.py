# Build In

"""
default de python
indentificador = max(lista, tupla, conjunto)                    # numero mas alto de una lista
indentificador = min(lista, tupla, conjunto)                    # numero mas chico de una lista
indentificador = round(variable, cantidad de decimales)         # redondea decimales
indentificador = bool(0, vacio, False, None)                    # devuelve true si no es alguna de esas
indentificador = all("string, numero, True)                     # devuelve false si uno ya es falso
"""
numero = [3, 42, -90]

maximo = max(numero)

minimo = min(numero)

numeros = round(34.12324, 3) 

falso = bool("hola") 

verdad = all(["hola", 10, True]) 
print(verdad)