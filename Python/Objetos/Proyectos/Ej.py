class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return "Nombre: %s\n Fuerza: %s\n Velocidad: %s" %(self.nombre, self.fuerza, self.velocidad)
    
    def __add__(self, nuevo):
        Nnombre = self.nombre[:-2] + nuevo.nombre[2:]
        Nfuerza = int(self.fuerza) + int(nuevo.fuerza)
        Nvelocidad = int(self.velocidad) + int(nuevo.velocidad)
        return Personaje(Nnombre, Nfuerza, Nvelocidad)    
        
def menu():
    print("Menu:")
    print("1 - Crear Personaje")
    print("2 - Fusion")
    print("3 - Mostrar Personajes")
    print("4 - Mostrar Fusiones")
    print("s - Salir")
    
def crear():
    nombre = input("Ingrese el nombre: ")
    fuerza = input("Ingrese la fuerza: ")
    velocidad = input("Ingrese la velocidad: ")
    return Personaje(nombre, fuerza, velocidad)

def mostrar(personajes):
    if not personajes:
        print("no creo ningun personaje.")
    else:
        for i, personaje in enumerate(personajes):
            print("Personaje [%s]: \n %s" %(i+1, personaje))
                  
# Main
personajes = []
personajes_fusionados = []    
while True:
    menu()
    opcion = input("Seccione una opcion: ")
    
    if opcion == "1":
        creado = crear()
        personajes.append(creado)
    elif opcion == "2":
        if len(personajes) < 2:
            print("Debe haber un minimo de 2 personajes para fusionar.")
        else:
            mostrar(personajes)
            num1 = int(input("Ingrese el numero del personaje: "))
            num2 = int(input("Ingrese el siguiente numero del personaje: "))
            if 1 <= num1 <= len(personajes) and 1 <= num2 <= len(personajes) and num1 != num2:
                personaje1 = personajes[num1 - 1]
                personaje2 = personajes[num2 - 1]
                fusionado = personaje1 + personaje2
                personajes_fusionados.append(fusionado)
                print("Fusion Exitosa!")
            else:
                print("Error, Ingrese un numero valido")
    elif opcion == "3":
        mostrar(personajes)       
    elif opcion == "4":
        mostrar(personajes_fusionados)    
    elif opcion == "s":
        print("Termino")
        break
    else:
        print("Error, ingrese opcion valida: ")
        
    