#Metodos de Strings:

"""
dir(cadena)                                         # devuelve la lista de atributos validos del objeto pasado
Upper =cadena.upper()                               # todo mayuscula
Lower =cadena2.lower()                              # todo minuscula
Capitalize = cadena3.capitalize()                   # la primera en mayuscula 
Find = cadena.find("m")                             # busca y devuelve la posicion sino lo encuentra devuelve -1
Index = cadena2.index("M")                          # busca y devuelve la posicion sino lo encuentra devuelve excepcion
Numeric = cadena4.isnumeric()                       # true es numero false no
Alpha = cadena4.isalpha()                           # solo letras de A a Z
Count = cadena2.count("U")                          # muestra la cantidad encontrada
cadenalen = len(cadena3)                            # muestra el total de caracteres
start = cadena.startswith("Ho")                     # verifica si empieza con
end = cadena3.endswith("un")                        # verifica si termina con
replace = cadena2.replace("string", "string")       #reemplaza la cadena si es que hay, sino devuelve la cadena original
split = cadena.split()                              #separa por cadena y devuelve una lista
"""
cadena = "Hola me llamo Leandro"
cadena2 = "GURIMU DAWN"
cadena3 = "leandro Sun"
cadena4 = "10323"

dir(cadena) 

Upper =cadena.upper() 
Lower =cadena2.lower() 
Capitalize = cadena3.capitalize() 

Find = cadena.find("m") 
Index = cadena2.index("M") 

Numeric = cadena4.isnumeric()
Alpha = cadena4.isalpha() 

Count = cadena2.count("U")
cadenalen = len(cadena3) 

start = cadena.startswith("Ho") 
end = cadena3.endswith("un") 

replace = cadena2.replace("GURIMU", "GRIM") 
split = cadena.split() 
print(split)