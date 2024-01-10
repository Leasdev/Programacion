#While:
#iteracion infinita
import os

os.system("cls")
numero = input("ingrese un numero: ")

#validacion utilizando while
while not numero.isnumeric(): 
    numero = input("Error, ingrese un numero: ")
    
print("Ok, su numero es: %s" %(numero))