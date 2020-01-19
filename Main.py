import pygame
import os
from GameObject import GameObject
from TextObject import TextObject
import config as c


class Tetris:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.board = [list([0] * xsize) for _ in range(ysize)]

    # def get_board(self):
    #    return self.board

    def figure(self, type, pozition):
        figure_list = [
            # 0 - line, 1 - square, 2 - 'L',
            # 3 - 'Z', 4 - 'T', 5 - 'L's, 6 - 'Z's
            [[1, 4, '1111', 0, 0, 2],
             [4, 1, '1111', 0, -1, 1]],

            [[2, 2, '1111', 1, -1, 2]],

            [[2, 3, '101011', 2, 0, 4],
             [3, 2, '111100', 2, 1, 1],
             [2, 3, '110101', 2, 2, 2],
             [3, 2, '001111', 2, -1, 3]],

            [[3, 2, '011110', 3, 0, 2],
             [2, 3, '101101', 3, -1, 1]],

            [[3, 2, '010111', 4, 0, 4],
             [2, 3, '101110', 4, 1, 1],
             [3, 2, '111010', 4, 2, 2],
             [2, 3, '011101', 4, -1, 3]],

            [[2, 3, '010111', 5, 0, 4],
             [3, 2, '100111', 5, 1, 1],
             [2, 3, '111010', 5, 2, 2],
             [3, 2, '111001', 5, -1, 3]],

            [[3, 2, '110011', 6, 0, 2],
             [2, 3, '011110', 6, -1, 1]]
        ]
        return figure_list[type][pozition]

    def is_intersection(self, figure, x, y):
        if (figure[0] + x > self.xsize) \
                or (x < 0) or (figure[1] + y > self.ysize):
            return True
        else:
            temp = list(figure[2])
            for i in range(len(temp)):
                if (temp[i] == '1') \
                        and (self.board[x + i % figure[0]][y + i // figure[1]] != '0'):
                    return True
            return False

    def rotate(self, figure, degree=0):
        if degree == 0:
            return self.figure(figure[3], figure[4] + 1)
        else:
            return self.figure(figure[3], figure[5] + 1)

    def render(self, figure, x, y):
        temp1 = self.board
        temp2 = list(figure[2])
        for i in range(len(temp)):
            temp1[x + i % figure[0]][y + i // figure[1]] = temp2[i]
        return temp1

    def add(self, figure, x, y):
        temp2 = list(figure[2])
        for i in range(len(temp)):
            self.boardx[x + i % figure[0]][y + i // figure[1]] = temp2[i]


class Menu:
    def __init__(self, screen):
        self.screen = screen


class Button():
    def __init__(self,
                 x,
                 y,
                 w,
                 h,
                 text,
                 on_click=lambda x: None,
                 padding=0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = TextObject(x + padding,
                               y + padding, lambda: text,
                               c.button_text_color,
                               c.font_name,
                               c.font_size)

    def draw(self, surface):
        pygame.draw.rect(surface,
                         self.back_color,
                         self.bounds)
        self.text.draw(surface)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    def back_color(self):
        return dict(normal=c.button_normal_back_color,
                    hover=c.button_hover_back_color,
                    pressed=c.button_pressed_back_color)[self.state]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Game:
    def __init__(self):
        self.objects = []
        self.menu_buttons = []
        self.mouse_handlers = []

    def create_menu(self):
        for i, (text, handler) in enumerate((('PLAY', on_play),
                                             ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

game = Game()
game.create_menu()
running = True
while running:
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            running = False
    pygame.display.flip()