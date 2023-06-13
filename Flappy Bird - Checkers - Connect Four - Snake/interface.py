from time import sleep
import main_flappy as mf
from pygame.locals import *
import checkers_ai.main as ch_ai
import checkers_human.main as ch_hu
import snake.agent as s_ai
import snake.snake_game_human as s_hu
import connect_four.connect4 as c4h
import connect_four.connect4ai as c4ai
import pygame
import pygame_menu
from pygame_menu import themes


player = 1

def connect4():
    print('playing:',player)
    c4ai.main() if player == 1 else c4h.main()

def snake():
    print('playing:',player)
    s_ai.main() if player == 1 else s_hu.main()

def playing(val, sel):
    global player
    player = sel
    print('player changed: ',sel)

def checkers():
    print('playing:',player)
    if player == 1:
        ch_ai.main()
    else:
        ch_hu.main()


# while(1):
def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 400),RESIZABLE)
    # surface.blit(pygame.transform.scale((500,500)),(0,0))
    mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
    # mainmenu._open()
    try:
        mainmenu.add.button('Connect 4', connect4)
        mainmenu.add.button('Snake', snake)
        mainmenu.add.button('Checkers', checkers)
        mainmenu.add.button('Flappy Bird', mf.mane)
        mainmenu.add.selector('Who is Playing:',[('AI',1),('Human',2)], onchange=playing)
        mainmenu.add.button('Quit', pygame_menu.events.EXIT)
        mainmenu.mainloop(surface)
    except:
        pass
    # pygame.display.quit()

if __name__ == '__main__':
    while(1):
        main()