#Diccionario:

#utilizando funcion dict
diccionario = dict(nombre = "leandro", 
                   apellido = "sun", 
                   numero = 10, 
                   crack = True)

print(diccionario)

#crea un diccionario con los keys de la lista
diccio = dict.fromkeys(["tupla", "apellido"])

#crea un diccionario con los keys por letra 
diccio2 = dict.fromkeys("tupla", "apellido")  

print(diccio)
print(diccio2)