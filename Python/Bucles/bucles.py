import os
i = 1
#lista
gurimus = ["sun", "milan", "santi", "brian"]
alturas = {194, 183, 183, 170}

#for
#for gurimu in gurimus:
#    print("nombre [%d]: %s" %(i, gurimu.capitalize()))
#    i += 1

os.system("cls")
    
for gurimu, altura in zip(gurimus, alturas):
    print("Gurimu[%d]: %s \naltura: %d mm" %(i, gurimu.capitalize(), altura))
    i += 1
    
print("\nfuncion range():")    # recorre la cantidad pero no podes acceder al indice
for num in range(len(alturas)): 
    print(num)
    

    
print("\nfuncion enumerate():")    # recorre la lista devuelve un tuple 
for num in enumerate(alturas):
    a = num[0] + 1 
    print("altura[%d]: %d" %(a, num[1]))
else:
    print("termino") # siempre se ejecuta
    
    