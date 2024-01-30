# Archivos pd

"""
import pandas as pd
identificador = pd.read_csv("ruta del archivo csv", names=["indetificador"])  # Leer el archivo
identificador = df["columna del encabezado"]                                  # obteniendo los datos de la columna nombre
identificador = df.sort_values("columna del encabezado")                      # ordenando el dataframe por la altura ascendente
identificador = df.sort_values("columna del encabezado", ascending=False)     # ordenando el dataframe por la altura descendente
identificador = pd.concat([indentificador1, indetificador2])                  # concatena los archivos
identificador = df.head(numero de fila)                                       # muestra hasta la fila indicada
identificador = df.tail(numero de fila)                                       # muestra desde la ultima fila indicada
identificador = df.shape                                                      # cantidad de filas y columnas (f,c)
identificador = df.loc[numero fila, nombre de columna]                        # accede al elemento especifico
identificador = df.iloc[numero de fila, index de columna]                     # accede al elemento especifico con index
df["nombre de columna"].astype(tipo)                                          # convierte el tipo de columna
df["nombre de columna"].replace("a reemplazar", "reemplazo", inplace=True)    # reemplaza los datos 
identificador = df.dropna(axis = 1)                                           # elimina las filas faltantes 0 fila /1 columnas
identificador = df.drop_duplcates()                                           # elimina las filas duplicadas
df.to_csv("ruta del archivo nuevo csv")                                       # una vez modificado crea un archivo nuevo
"""
import pandas as pd
df = pd.read_csv("Python\\Imperativo\\8-Archivos\\datos.csv")                 # dataframe

nombres = df["nombre"] 
ordenadoA = df.sort_values("altura") 
ordenadoD = df.sort_values("altura", ascending=False) 
primeras = df.head(1)
ultimas = df.tail(4)
cantidad = df.shape
elemento = df.loc[2,"altura"]   # : accede a todos los elementos
elemento1 = df.iloc[2,2]    