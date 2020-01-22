import pygame
import os
from GameObject import GameObject
from TextObject import TextObject
from Tetris import Tetris
import Screens
import config as c

pygame.init()
running = True
screen = pygame.display.set_mode((c.width, c.height))
MainMenu = Screens.MainMenu(screen)
MainMenu.draw()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        MainMenu.run(event)
    pygame.display.flip()
