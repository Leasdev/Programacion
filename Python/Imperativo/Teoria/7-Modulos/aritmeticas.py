# Funciones:

def sumar(x,y):
    return x + y

def restar(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
    