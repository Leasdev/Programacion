# Funcion Lambda

"""
indetificador = lambda parametro, ... : expresion                # apto para solo una instruccion, y return   
"""
sumar = lambda x, y : x + y

print("sumar(1,2): %s" %(sumar(1,2)))

# Funcion Filter

"""
indetificador = filter(funcion, (lista, conjunto, tupla))        # variable = filter(funcion, parametro)
"""
sopa = ["a", "1", "b", "2", "c", "3"]

def only_letras(x):                                     # utilizando con funcion
    if not x.isnumeric():
        return True
    
letras = filter(only_letras, sopa)

numeros = filter(lambda num: num.isnumeric(), sopa)     # utilizando con funcion lambda

print("letras = filter(only_letras, sopa): %s" %(list(letras))) # para ver los elementos se pasan a listas
print("numeros = filter(lambda num: num.isnumeric(), sopa): %s" %(list(numeros)))