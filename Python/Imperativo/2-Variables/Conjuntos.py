#Conjuntos:

#utilizando funcion set
conjunto = set(["hola", ("caca","coca")])


#utilizando funcion frozenset (conjunto que no se puede modificar)
conjunto2 = {frozenset(conjunto), "chau"} 

print(conjunto2)

#Subconjuntos

print("Conjunto 1 = {1, 2, 3, 4, 5}")
print("Conjunto 2 = {2, 4}")
conjunto3 = set([1, 2, 3, 4, 5])
conjunto4 = {2,4}

resultado = conjunto4.issubset(conjunto3) # si es subconjunto (menor)
resultado = conjunto4 <= conjunto3

print(f'Conjunto 2 es sub de Conjunto 1?: {resultado}')

resultado = conjunto4.issuperset(conjunto3) # si es superconjunto (mayor)
resultado = conjunto4 >= conjunto3

print(f'Conjunto 2 es super de Conjunto 1?: {resultado}')