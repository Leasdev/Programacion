import pygame

# Dimesiones de la pantalla
ancho = alto = 512
dimension = 8
cuadrado = ancho // dimension

class Tablero:
    def __init__(self, pantalla):            
        colores = [pygame.Color("white"), pygame.Color("gray")]
        for fila in range(dimension):
            for columna in range(dimension):
                color = colores[(fila + columna) % 2]   
                pygame.draw.rect(pantalla, color, (columna * cuadrado, fila* cuadrado, cuadrado, cuadrado))
                     
class Pieza:
    def __init__(self, id, fila, columna, imagen, tamano, color):               
        self.id = id
        self.fila = fila
        self.columna = columna
        self.imagen = imagen
        self.tamano = tamano
        self.color = color
           
    def dibujar(self, pantalla):
        x = self.columna * self.tamano
        y = self.fila * self.tamano 
        pantalla.blit(self.imagen, (x, y))
        
    def get_id(self):
        return self.id
       
class Peon(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        self.primer_movimiento = True
        
    def mover(self, fila, columna):    
            self.fila = fila
            self.columna = columna
            self.primer_movimiento = False

class Torre(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        
        
class Caballo(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        

class Alfil(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        
        
class Reina(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        
        
class Rey(Pieza):
    def __init__(self, id, fila, columna, imagen, tamano, color):
        super().__init__(id, fila, columna, imagen, tamano, color)
        
        
# Main 
class ChessGame:
    def __init__(self):       
        # inicia Pygame
        pygame.init()
        
        # Dibujar Tablero
        self.pantalla = pygame.display.set_mode([ancho,alto])
        pygame.display.set_caption('Chess')        
        self.tablero = Tablero(self.pantalla)
        self.piezas = []

        # Peon        
        peon_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nP.png")
        peon_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bP.png")
        for i in range(8):
            self.piezas.append(Peon("nP_" + str(i+1), 1, i, peon_negro, cuadrado, "n"))
            self.piezas.append(Peon("bP_"+ str(i+1), 6, i, peon_blanco, cuadrado, "b"))   
                            
        # Torre    
        torre_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nT.png")
        torre_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bT.png")
    
        self.piezas.append(Torre("nT_1", 0, 0, torre_negro, cuadrado, "n"))
        self.piezas.append(Torre("bT_1", 7, 0, torre_blanco, cuadrado, "b"))
        self.piezas.append(Torre("nT_2", 0, 7, torre_negro, cuadrado, "n"))
        self.piezas.append(Torre("bT_2", 7, 7, torre_blanco, cuadrado, "b"))   
           
        # Caballo
        caballo_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nC.png")
        caballo_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bC.png")
     
        self.piezas.append(Caballo("nC_1", 0, 1, caballo_negro, cuadrado, "n"))
        self.piezas.append(Caballo("bC_1", 7, 1, caballo_blanco, cuadrado, "b"))
        self.piezas.append(Caballo("nC_2", 0, 6, caballo_negro, cuadrado, "n"))
        self.piezas.append(Caballo("bC_2", 7, 6, caballo_blanco, cuadrado, "b"))                    
            
        # Alfil
        alfil_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nA.png")
        alfil_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bA.png")
        
        self.piezas.append(Alfil("nA_1", 0, 2, alfil_negro, cuadrado, "n"))
        self.piezas.append(Alfil("bA_1", 7, 2, alfil_blanco, cuadrado, "b"))
        self.piezas.append(Alfil("nA_2", 0, 5, alfil_negro, cuadrado, "n"))
        self.piezas.append(Alfil("bA_2", 7, 5, alfil_blanco, cuadrado, "b"))   
            
        # Reina
        reina_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nQ.png")
        reina_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bQ.png")       
        self.piezas.append(Reina("nQ_1", 0, 3, reina_negro, cuadrado, "n"))
        self.piezas.append(Reina("bQ_1", 7, 3, reina_blanco, cuadrado, "b"))   
                        
        # Rey
        rey_negro = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/nK.png")
        rey_blanco = pygame.image.load("Python/Objetos/Proyectos/Chess/Images/bK.png")       
        self.piezas.append(Rey("nK_1", 0, 4, rey_negro, cuadrado, "n"))
        self.piezas.append(Rey("bK_1", 7, 4, rey_blanco, cuadrado, "b"))   
            
        for i in range(32):
            self.piezas[i].dibujar(self.pantalla)
            print(self.piezas[i].get_id())    
                  
    def run(self):        
        run = True
        while run:                       
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    run = False                
                                                     
            pygame.display.flip()
        pygame.quit()       
               
#if __name__ == "__main__":
juego = ChessGame()
juego.run()
    