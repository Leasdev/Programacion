#While:

"""
while expresion:
    sentencia 1
    sentencia n
"""
numero = input("ingrese un numero: ")

while not numero.isnumeric():  # validacion utilizando while
    numero = input("Error, ingrese un numero: ")
    
print("Ok, su numero es: %s" %(numero))