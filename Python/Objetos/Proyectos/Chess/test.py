import pygame

ancho = alto = 512
dimension = 8
cuadrado = ancho // dimension
timer = pygame.time.Clock()
fps = 60
pantalla = pygame.display.set_mode([ancho,alto])

# Cargar imagen de piezas
def cargar_imagen():  
    imag_blancas = []
    imag_blancas_small = []
    imag_negras = []
    imag_negras_small = []  
    piezas_blancas = ['bP', 'bT', 'bC', 'bA', 'bQ', 'bK']
    piezas_negras = ['nP', 'nT', 'nC', 'nA', 'nQ', 'nK']  
    for pieza in piezas_blancas:
        imag_blancas[pieza] = pygame.image.load("/Images" + pieza + ".png")
        imag_blancas_small[pieza] = pygame.transform.scale(imag_blancas[piezas_blancas], (100, 100))
    for pieza in piezas_negras:
        imag_negras[pieza] = pygame.image.load("/Images" + pieza + ".png")
        imag_negras_small[pieza] = pygame.transform.scale(imag_negras[piezas_negras], (100, 100))
    
    lista_piezas = ['peon', 'torre', 'caballo', 'alfil', 'reina', 'rey']    
        
# Piezas
piezas_blancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon' ,'peon' ,'peon' ,'peon' ,'peon']
ubicacion_blancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0) ,(7, 0),
                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1) ,(7, 1)]
piezas_negras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                  'peon', 'peon', 'peon', 'peon' ,'peon' ,'peon' ,'peon' ,'peon']
ubicacion_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7) ,(7, 7),
                     (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6) ,(7, 6)]
piezas_blancas_capturadas = []
piezas_negras_capturadas = []


# Fases
fase = 0
seleccion = 100
movimientos_validos = []

pieces = {}
pieces['bT'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bT.png')
pieces['bC'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bC.png')
pieces['bA'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bA.png')
pieces['bQ'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bQ.png')
pieces['bK'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bK.png')
pieces['bP'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/bP.png')
pieces['nT'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nT.png')
pieces['nC'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nC.png')
pieces['nA'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nA.png')
pieces['nQ'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nQ.png')
pieces['nK'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nK.png')
pieces['nP'] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/nP.png')

# Graficas
def dibujar_tablero():
    colores = [pygame.Color("white"), pygame.Color("gray")]
    for fila in range(dimension):
        for columna in range(dimension):
            color = colores[(fila+columna) % 2]   
            pygame.draw.rect(pantalla, color, (columna * cuadrado, fila* cuadrado, cuadrado, cuadrado))
           
                
def main():
    run = True
    while run:
        timer.tick(fps)
        pantalla.fill('white')
        dibujar_tablero()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False               
        pygame.display.flip()
    pygame.quit()
    
    class Pieza:
        def __init__(self):               
            self.pieza = ['bT', 'bC', "bA", 'bQ', 'bK', 'bP', 'nT', 'nC', "nA", 'nQ', 'nK', 'nP']

        def cargar(self):        
            for i in self.pieza:
                dibujado[i] = pygame.image.load('Python/Objetos/Ejercicios/Chess/Images/' + i + '.png')
                
        def dibujar(self, pantalla):
            for fila in range(dimension):
                for columna in range(dimension):                
                        pieza_imagen = dibujado[self.pieza]
                        pantalla.blit(pieza_imagen, pygame.Rect(columna * cuadrado, fila * cuadrado, cuadrado, cuadrado))