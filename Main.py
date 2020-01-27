import pygame
import os
# from GameObject import GameObject
# from TextObject import TextObject
# from Tetris import Tetris
import Screens
import config as c

pygame.init()
running = True
pygame.display.set_caption("Hacktrix alfa")
load_screen = 'Desktop'
if c.screen_mode:
    screen = pygame.display.set_mode((c.width, c.height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((c.width, c.height))

# load screens
MainMenu = Screens.MainMenu(screen)
Desktop = Screens.Desktop(screen)
SavesMenu = Screens.SavesMenu(screen)
PlayLevel = Screens.PlayLevel(screen)
# PlayLevel.load_level(os.path.join('levels', '1.txt'))
command = '0'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if load_screen == 'Main_menu':
            command = MainMenu.run(event)
        elif load_screen == 'Saves_menu':
            command = SavesMenu.run(event)
        elif load_screen == 'Level':
            command = PlayLevel.run(event)
        elif load_screen == 'Desktop':
            command = Desktop.run(event)

        temp = command.split(';')
        if temp[0] == 'change':
            load_screen = temp[1]
        if temp[0] == 'exit':
            running = False
        if temp[0] == 'load':
            slot = int(temp[1])

    pygame.display.flip()
pygame.quit()
