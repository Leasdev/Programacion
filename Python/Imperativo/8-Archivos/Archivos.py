# Archivos

"""
Modo de acceso:
r = read (Lectura)
w = write (Escritura)
a = append (anadir)
"""

# Abrir el archivo con la ruta del path (dafault abre en modo lectura)
""" archivo = open("ruta", "modo de acceso") """                            # encoding = "UTF-8" reconoce mas caracteres

# Leer el archivo
""" archivo = open("Python\\Imperativo\\8-Archivos\\texto.txt","r") """
""" leer = archivo.read() """                                               # coloca el cursor al principio y lo lee
""" leermas = archivo.readlines() """                                       # Leer linea por linea y devuelve en una lista
""" leeruno = archivo.readline(cantidad de caracteres) """                  # Leer linea una sola linea

# Escribir en el archivo
""" archivo = open("Python\\Imperativo\\8-Archivos\\texto.txt","w") """
""" archivo.write("prueba") """                                             # coloca el cursor al principio, si hay algo lo pisa
""" archivo.writelines(["\ntesteando", " el writelines"]) """               # agrega 

# Agregando al archivo
""" archivo = open("Python\\Imperativo\\8-Archivos\\texto.txt","a") """
""" archivo.write("\nAgregando al archivo") """                             # coloca el cursor al final y agrega

# Cerrar el archivo
""" archivo.close() """

# Forma optima con with open
""" with open("Python\\Imperativo\\8-Archivos\\texto.txt") as archivo: """ # abre el archivo  con archivo y lo cierra
"""     print(archivo.read()) """