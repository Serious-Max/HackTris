import pygame

width = 800
height = 600
button_text_color = pygame.Color('black')
button_normal_back_color = pygame.Color(255, 255, 255)
button_hover_back_color = pygame.Color('red')
button_pressed_back_color = pygame.Color('blue')
square_color = pygame.Color('White')
font_name = 'Times New Roman'
font_size = 24
game_front_name = 'Times New Roman'
game_font_size = 18
game_font_color = pygame.Color('green')
sencivity = 200

def pause_text_x():
    return 200

def pause_text_y():
    return 200

def bowl_x():
    return 10


def bowl_y():
    return 10


def square_size():
    return 10


def padding():
    return 5


def menu_offset_x():
    return int((width * 30) / 100)


def menu_offset_y():
    return int((height * 30) / 100)


def menu_button_w():
    return int((width * 40) / 100)


def menu_button_h():
    return int((height * 10) / 100)
