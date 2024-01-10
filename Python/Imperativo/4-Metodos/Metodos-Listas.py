#Metodos de Listas:

#utilizando la funcion list
lista = list(["chau", False, 1, 2])

cantidad = len(lista) # devuelve cantidad de elementos

lista.append("final") # agrega al final de la lista

lista.insert(1, "no") # agrega un elemento en la posicion indicada

lista.extend(["milan", 69]) # agrega varios elementos a la lista

lista.pop(0) # elimina un elemento de lista (indicar indice)

lista.remove("milan") # elimina un elemento de la lista, si lo encuentra
lista.remove("no")
lista.remove("final")

lista.sort() # ordena la lista ascendentemente
lista.sort(reverse=True) # ordena la lista al reves

lista.reverse() # invierte la lista

print(lista) 