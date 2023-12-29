import os
diccionario = {
    "nombre" : "Leandro",
    "altura" : 195,
    "crack" : True
}
os.system("cls")

"""for key in diccionario: 
    print(key) # devuele solo la clave del diccionario"""
    
for datos in diccionario.items(): # devuelve la tupla
    print("la key es %s y es %s" %(datos[0], datos[1]))    