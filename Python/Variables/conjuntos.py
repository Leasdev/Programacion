#conjuntos
print("frozenset():")
conjunto = set(["hola", ("caca","coca")])

conjunto2 = {frozenset(conjunto), "chau"} # conjunto que no se puede modificar

print(conjunto2)
print("\n")

#subconjuntos

print("Conjunto 1 = {1, 2, 3, 4, 5}")
print("Conjunto 2 = {2, 4}")
conjunto3 = set([1, 2, 3, 4, 5])
conjunto4 = {2,4}

resultado = conjunto4.issubset(conjunto3)
resultado = conjunto4 <= conjunto3

print(f'Conjunto 2 es sub de Conjunto 1?: {resultado}')

resultado = conjunto4.issuperset(conjunto3)
resultado = conjunto4 >= conjunto3

print(f'Conjunto 2 es super de Conjunto 1?: {resultado}')