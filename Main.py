import pygame
import os
# from GameObject import GameObject
# from TextObject import TextObject
# from Tetris import Tetris
import Screens
import config as c

pygame.init()
running = True
screen = pygame.display.set_mode((c.width, c.height),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
#screen = pygame.display.set_mode((c.width, c.height))
MainMenu = Screens.MainMenu(screen)
#MainMenu.draw()
PlayLevel = Screens.PlayLevel(screen)
PlayLevel.load_level(os.path.join('levels', '1.txt'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    running = False
        #MainMenu.run(event)
        PlayLevel.run(event)
    pygame.display.flip()
pygame.quit()
