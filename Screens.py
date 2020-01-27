import GameObject
import TextObject
import config as c
import pygame
import os
from Tools import Button
import Tetris
import random


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
        self.command = '0'
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.menu_buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        for i in self.objects:
            i.draw(self.screen)

    def new_game(self, obj):
        file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='wt')
        file.write(';'.join([self.name, str(0), str(0)]))
        file.close()

    def quit(self, obj):
        self.command = 'exit'

    def load(self, obj):
        self.command = 'change;Saves_menu'
        # print('load')

    def settings(self, obj):
        pass

    def fill(self):
        self.screen.fill((0, 0, 0))


class SavesMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = list()
        for i, (text, handler) in enumerate((('Slot 1', self.load1),
                                             ('Slot 2', self.load2),
                                             ('Slot 3', self.load3),
                                             ('Slot 4', self.load4),
                                             ('Back', self.back))):
            b = Button(c.save_menu_offset_x(),
                       c.save_menu_offset_y() + (c.save_menu_button_h() + int((c.height * 5) / 100)) * i,
                       c.save_menu_button_w(),
                       c.save_menu_button_h(),
                       text,
                       handler,
                       padding=c.padding())
            self.buttons.append(b)

    def run(self, event):
        self.command = '0'
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        for i in self.buttons:
            i.draw(self.screen)

    def load1(self, obj):
        self.command = 'load;1'

    def load2(self, obj):
        self.command = 'load;2'

    def load3(self, obj):
        self.command = 'load;3'

    def load4(self, obj):
        self.command = 'load;4'

    def back(self, obj):
        self.command = 'change;Main_menu'

    def fill(self):
        self.screen.fill((0, 0, 0))


class Desktop:
    def __init__(self, screen):
        self.screen = screen
        self.slot = 1
        self.buttons = []
        for i, (text, handler) in enumerate((('Mail', self.open_text),
                                             ('IDE', self.start_level),
                                             ('Main_menu', self.back))):
            b = Button(c.mail_button_x(),
                       c.mail_button_y() + (c.desktop_square_button() + int((c.height * 5) / 100)) * i,
                       c.desktop_square_button(),
                       c.desktop_square_button(),
                       text,
                       handler,
                       padding=c.padding())
            self.buttons.append(b)

    def run(self, event):
        self.command = '0'
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        temp = GameObject.GameObject(0, 0, c.toolbar_width(), c.height)
        pygame.draw.rect(self.screen, c.toolbar_color, temp.bounds)
        for i in self.buttons:
            i.draw(self.screen)

    def open_text(self, obj):
        pass

    def start_level(self, obj):
        pass

    def back(self, obj):
        self.save()
        self.command = 'change;Main_menu'

    def save(self):
        file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='wt')
        file.write(';'.join([self.name, str(self.money), str(self.next_level)]))
        file.close()

    def load(self):
        file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='rt')
        temp = file.readlines()
        file.close()
        self.name = temp[0]
        self.money = int(temp[1])


    def fill(self):
        self.screen.fill((0, 0, 0))


class PlayLevel:
    def __init__(self, screen):
        self.screen = screen
        self.active_figure = None
        self.figure_poz_x = 5
        self.figure_poz_y = 0
        self.game_run = False
        self.TICK = 2
        pygame.time.set_timer(self.TICK, c.sencivity)

    def run(self, event):
        self.command = '0'
        self.fill()
        if self.game_run:
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                self.game_run = False
            if event.type == self.MOVE:
                if self.active_figure:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y + 1):
                        self.figure_poz_y += 1
                        # print('Move down')
                    else:
                        # print('Crash')
                        self.tetris.add(self.active_figure, self.figure_poz_x, self.figure_poz_y)
                        self.active_figure = None
                        self.figure_poz_y = 0
                        self.figure_poz_x = 5
                        for i in range(self.tetris.ysize):
                            if all(self.tetris.board[i]):
                                self.tetris.del_line(i)
                                self.del_lines += 1
                                if self.del_lines == self.end:
                                    self.game_win = True
                else:
                    # print('Generate figure...')
                    # print(self.tetris.board)
                    self.active_figure = self.tetris.figure(random.randint(0, 6), 0)
                    if self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y):
                        self.game_over = True
                        self.game_run = False
                    # print(self.tetris.board)
                    # print('Generate figure...OK')
            if self.active_figure and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                temp = self.tetris.rotate(self.active_figure)
                if not self.tetris.is_intersection(temp, self.figure_poz_x, self.figure_poz_y):
                    self.active_figure = temp
            if event.type == self.TICK and self.active_figure:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x - 1, self.figure_poz_y):
                        self.figure_poz_x -= 1
                if keys[pygame.K_RIGHT]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x + 1, self.figure_poz_y):
                        self.figure_poz_x += 1
                if keys[pygame.K_DOWN]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y + 1):
                        self.figure_poz_y += 1
        else:
            if self.game_over:
                pass
            else:
                temp = TextObject.TextObject(c.pause_text_x(), c.pause_text_y(), lambda: 'Press F to play',
                                             c.game_font_color, c.game_front_name, c.game_font_size)
                temp.draw(self.screen)
                if event.type == pygame.KEYUP and event.key == pygame.K_f:
                    # print(1)
                    self.game_run = True
        self.draw()
        return self.command

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

    def fill(self):
        self.screen.fill((0, 0, 0))

    def load_level(self, level_name):
        self.tetris = Tetris.Tetris(10, 20)
        file = open(level_name, mode='rt')
        temp = file.readlines()
        self.difficult = int(temp[1])
        self.end = int(temp[2])
        self.game_over = False
        self.game_win = False
        file.close()
        self.MOVE = 1
        self.del_lines = 0
        pygame.time.set_timer(self.MOVE, self.difficult)


class Store:
    def __init__(self):
        pass

    def run(self):
        pass
