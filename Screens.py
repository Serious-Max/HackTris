import config as c
from Tools import Button

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        for i, (text, handler) in enumerate((('Load Game', self.load),
                                             ('New Game', self.new_game),
                                             ('Settings', self.settings),
                                             ('Quit', self.quit))):
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

    def run(self):
        pass


    def new_game(self):
        pass

    def quit(self):
        pass

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
    def __init__(self):
        pass
    def run(self):
        pass

class Store:
    def __init__(self):
        pass
    def run(self):
        pass