import pygame
import os
from GameObject import GameObject
from TextObject import TextObject
from Tetris import Tetris
import Screens
import config as c
import Tools as *

# игровые экраны
class Game:
    def __init__(self):
        pass


pygame.init()
game = Game()
game.create_menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            running = False
    pygame.display.flip()
