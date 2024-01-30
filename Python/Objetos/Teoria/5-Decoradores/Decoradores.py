# Decoradores
"""
def decorador(funcion):
    def funcion_modificada():
        sentencia antes
        funcion():
        sentencia despues
    return funcion_modificada 

@decorador
def funcion():
    sentencia
    
def funcion():
    sentencia
    
identificador = decorador(funcion)
funcion()     
"""
def decorador(validar):
    def funcion_modificada():
        numero = input("Ingrese un numero ")
        validado = validar(numero)
        print("ok, se valido y es %s" %(validado))        
    return funcion_modificada

def validar(numero):
    while not numero.isnumeric(): 
        numero = input("Error, Ingrese un numero ")
    return numero
    
num = decorador(validar)
num()    