#For:

"""
for indetificador, ... in expresion:
    sentencia 1
    sentencia n
    
for indetificador in range(numero):                 # itera cantidad del rango
    sentencia 1
    sentencia n
    
for indetificador in enumarate(numero):             # recorre la lista devuelve un tuple
    sentencia 1
    sentencia n
"""
i = 1
gurimus = ["sun", "milan", "santi", "brian"]
alturas = {194, 183, 183, 170}
 
for gurimu, altura in zip(gurimus, alturas):        # accede a la lista
    print("Gurimu[%d]: %s \naltura: %d mm" %(i, gurimu.capitalize(), altura))
    i += 1
     
for num in range(len(alturas)): 
    print(num)
      
for num in enumerate(alturas):
    a = num[0] + 1 
    print("altura[%d]: %d" %(a, num[1]))
else:
    print("termino") # siempre se ejecuta
    
diccionario = {
    "nombre" : "Leandro",
    "altura" : 195,
    "crack" : True
}

"""for key in diccionario: 
    print(key) # devuele solo la clave del diccionario"""
    
for datos in diccionario.items(): # devuelve la tupla
    print("la key es %s y es %s" %(datos[0], datos[1]))         