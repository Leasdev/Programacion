# Archivos CSV

"""
import csv

with open("ruta del archivo csv") as indetificador:
    nombre = csv.reader(indetificador)              # lee el archivo
    for nombre2 in nombre:
        print(nombre2)
"""
import csv

with open("Python\\Imperativo\\8-Archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)