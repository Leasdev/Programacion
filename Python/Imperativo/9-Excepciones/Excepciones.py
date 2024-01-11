# Excepciones
"""
try:            # intenta ejecutar la sentencia
    sentencia 1
    sentencia n
    
except:         # cuando el try tira excepcion
    sentencia 1
    sentencia m
"""

def sumar():
    while True:
        a = input("Ingrese numero 1: ")
        b = input("Ingrese numero 2: ")
        try:
            resultado = int(a) + int(b)
            break
        except:
            print("Error, Ingrese un numero")
    return resultado

print(sumar())