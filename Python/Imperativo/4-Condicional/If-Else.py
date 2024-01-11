#Condicional:

"""
if indetificador =/>/</==/>=/<=/!= dato:
    sentencia 1
    sentencia n
else
    sentencia 1
    sentencia n

if indetificador =/>/</==/>=/<=/!= dato:
    sentencia 1
    sentencia n
elif indetificador =/>/</==/>=/<=/!= dato:
    sentencia 1
    sentencia n
else
    sentencia 1
    sentencia n
"""
numero = 100
print("numero = 100")

if numero > 50:
    print("su numero es mas que 50")
else:
    print("su numero es mas chico que 50")

if numero > 50:
    print("su numero es mas que 50")    
elif numero > 1000:
    print("su numero es mas que 1000")
else:
    print("es mas chico que 50")