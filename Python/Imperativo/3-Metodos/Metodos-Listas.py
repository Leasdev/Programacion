#Metodos de Listas:

"""
indetificador = len(lista)                  # devuelve cantidad de elementos
lista.append("string")                      # agrega al final de la lista
lista.insert(1, "string")                   # agrega un elemento en la posicion indicada
lista.extend(["string", ...])               # agrega varios elementos a la lista
lista.pop(0)                                # elimina un elemento de lista (indicar indice)
lista.remove("string")                      # elimina un elemento de la lista, si lo encuentra
lista.sort()                                # ordena la lista ascendentemente
lista.sort(reverse=True)                    # ordena la lista al reves
lista.reverse()                             # invierte la lista

"""
lista = list(["chau", False, 1, 2])

cantidad = len(lista) 

lista.append("final") 

lista.insert(1, "no") 

lista.extend(["milan", 69]) 

lista.pop(0) 

lista.remove("milan") 
lista.remove("no")
lista.remove("final")

lista.sort() 
lista.sort(reverse=True) 

lista.reverse() 

print(lista) 