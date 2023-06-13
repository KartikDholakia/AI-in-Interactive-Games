# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers_ai.checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers_ai.checkers.game import Game
from checkers_ai.minimax.algorithm import minimax

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    FPS = 60

    # Depth of Mini-max Algorithm
    DIFFICULTY_LEVEL = 4

    pygame.display.set_caption('Checkers - Human VS AI')

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), DIFFICULTY_LEVEL, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    # pygame.quit()

if __name__ == '__main__':
    main()