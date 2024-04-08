import pygame
import sys

# Dimensiones de la ventana y del tablero
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Clase Pieza
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - 5
        pygame.draw.circle(window, self.color, (self.x + SQUARE_SIZE // 2, self.y + SQUARE_SIZE // 2), radius)

# Clase Peón
class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()

# Inicialización de Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ajedrez')

# Creación de las piezas
pawn = Pawn(6, 2, BLUE)

# Función principal del juego
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                pawn.move(clicked_row, clicked_col)

        draw_window()

    pygame.quit()
    sys.exit()

# Función para dibujar el tablero y las piezas
def draw_window():
    window.fill(WHITE)
    draw_board()
    pawn.draw(window)
    pygame.display.update()

# Función para dibujar el tablero
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(window, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()