# Polimorfismo

class Perro:
    def sonido(self):
        return "Guau"
    
class Gato:
    def sonido(self):
        return "Miau"
        
perro = Perro()
gato = Gato()

print(perro.sonido())
print(gato.sonido())