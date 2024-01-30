import os
class Juego:
    def __init__(self, Inombre, Iconsola, Icategoria):
            self.nombre = Inombre
            self.consola = Iconsola
            self.categoria = Icategoria
    
    def abrir(self):
        print("Abriste el juego %s\nCategoria: %s\nConsola: %s" %(self.nombre,self.categoria, self.consola))
   
def menu():
    while True:
        print("Menu:")
        print("1 - Agregar Juego")
        print("2 - Mostrar Juegos")
        print("s - Salir")
        opcion = input("Seleccione uno: ")
        return opcion    

def crear():
    nombre = input("Ingrese nombre: ")
    consola = input("Ingrese consola: ")
    categoria = input("Ingrese categoria: ")
    creado = Juego(nombre, consola, categoria)
    return creado               

def mostrar():
    global juegos
    os.system("cls")
    for i in range(len(juegos)):
        print("Nombre: %s\nConsola: %s\nCategoria %s\n" %(juegos[i].nombre, juegos[i].consola, juegos[i].categoria))           
        
# Main                

os.system("cls")
juegos = []

while True:
    seleccion = menu()
    if seleccion == "1":       
        juegos.append(crear())             
    elif seleccion == "2":        
        mostrar()            
    elif seleccion == "s":
        os.system("cls")
        print("Salio")
        break
