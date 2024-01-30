# Abstraccion

# Ocultar la complejidad de un sistema y dando las funcionalidades relevantes

class auto():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo...")
        
mi_auto = auto()
mi_auto.conducir()