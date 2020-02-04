import pygame

width = 800
height = 600
screen_mode = 0
animation_time = 90
FPS = 60
DRAW = 4
button_text_color = pygame.Color('black')
button_normal_back_color = pygame.Color(255, 255, 255)
button_hover_back_color = pygame.Color('red')
button_pressed_back_color = pygame.Color('blue')
background_square_color = pygame.Color('grey')
square_color = pygame.Color('Green')
font_name = 'Times New Roman'
font_size = 24
game_front_name = 'Times New Roman'
game_font_size = 18
game_font_color = pygame.Color('green')
sencivity = 250
mail_icon_name = 'Mail_icon_1.png'
toolbar_color = pygame.Color('Grey')
text_messange_font = 'Times New Roman'
text_messange_size = 20
text_messange_color = pygame.Color('Green')
def text_messange_repeat_x():
    return 200

def text_messange_repeat_y():
    return 200

def text_messange_repeat_button_w():
    return 50

def text_messange_repeat_button_h():
    return 50



def text_messange_next_x():
    return 400

def text_messange_next_y():
    return 200

def text_messange_next_button_w():
    return 50

def text_messange_next_button_h():
    return 50


def toolbar_width():
    return 60

def pause_text_x():
    return int((width * 50) / 100)

def pause_text_y():
    return int((height * 50) / 100)

def bowl_x():
    return 10


def bowl_y():
    return 10


def square_size():
    return int((height * 4.5) / 100)


def padding():
    return 5

def text_padding():
    return 20


def menu_offset_x():
    return int((width * 30) / 100)


def menu_offset_y():
    return int((height * 30) / 100)


def menu_button_w():
    return int((width * 40) / 100)


def menu_button_h():
    return int((height * 10) / 100)

def save_menu_offset_x():
    return int((width * 30) / 100)


def save_menu_offset_y():
    return int((height * 10) / 100)

#def decktop_button():
#    return 10


def save_menu_button_w():
    return int((width * 40) / 100)


def save_menu_button_h():
    return int((height * 10) / 100)


def mail_button_x():
    return 10


def mail_button_y():
    return 10

def desktop_square_button():
    return 64

def char_in_line():
    return 80