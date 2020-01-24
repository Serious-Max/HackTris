import GameObject
import config as c
import pygame
from Tools import Button
import Tetris


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.objects = list()
        self.menu_buttons = list()
        self.mouse_handlers = list()
        for i, (text, handler) in enumerate((('Load Game', self.load),
                                             ('New Game', self.new_game),
                                             ('Settings', self.settings),
                                             ('Quit', self.quit))):
            b = Button(c.menu_offset_x(),
                       c.menu_offset_y() + (c.menu_button_h() + int((c.height * 5) / 100)) * i,
                       c.menu_button_w(),
                       c.menu_button_h(),
                       text,
                       handler,
                       padding=c.padding())
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def run(self, event):
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.menu_buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()

    def draw(self):
        for i in self.objects:
            i.draw(self.screen)

    def new_game(self):
        pass

    def quit(self):
        pass

    # global running
    # running = False

    def load(self):
        pass

    def settings(self):
        pass


class SavesMenu:
    def __init__(self):
        pass

    def run(self):
        pass


class GameMenu:
    def __init__(self):
        pass

    def run(self):
        pass


class PlayLevel:
    def __init__(self, screen):
        self.screen = screen
        self.tetris = Tetris.Tetris(10, 20)
        self.active_figure = None
        self.figure_poz_x = 0
        self.figure_poz_y = 0

    def run(self, event):
        pass

    def draw(self):
        if self.active_figure:
            temp = self.tetris.render(self.active_figure, self.figure_poz_x, self.figure_poz_y)
        else:
            temp = self.tetris.render([0, 0, ''], 0, 0)
        for x in range(self.tetris.xsize):
            for y in range(self.tetris.ysize):
                symb = temp[y][x]
                if symb:
                    temp_obj = GameObject.GameObject(c.bowl_x() + x * (c.square_size() + 1),
                                                     c.bowl_y() + y * (c.square_size() + 1), c.square_size(),
                                                     c.square_size())
                    pygame.draw.rect(self.screen, c.square_color, temp_obj.bounds)


class Store:
    def __init__(self):
        pass

    def run(self):
        pass
