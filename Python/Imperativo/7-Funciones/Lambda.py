# Funcion Lambda

# apto para solo una instruccion, y return
#  variable = lambda parametro : funcion

sumar = lambda x, y : x + y

print("Funcion Lambda:")
print("sumar = lambda x, y : x + y")
print("sumar(1,2): %s" %(sumar(1,2)))

# Funcion Filter

# variable = filter(funcion, parametro)
sopa = ["a", "1", "b", "2", "c", "3"]

# utilizando con funcion
def only_letras(x):
    if not x.isnumeric():
        return True
    
letras = filter(only_letras, sopa)

# utilizando con funcion lambda
numeros = filter(lambda num: num.isnumeric(), sopa)

print("\nFuncion Filter:")
print("sopa = [a, 1, b, 2, c, 3]")
print("letras = filter(only_letras, sopa): %s" %(list(letras))) # para ver los elementos se pasan a listas
print("numeros = filter(lambda num: num.isnumeric(), sopa): %s" %(list(numeros)))






