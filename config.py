import pygame

width = 800
height = 600
button_text_color = pygame.Color('black')
button_normal_back_color = pygame.Color(255, 255, 255)
button_hover_back_color = pygame.Color('red')
button_pressed_back_color = pygame.Color('blue')
font_name = 'Times New Roman'
font_size = 24


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
