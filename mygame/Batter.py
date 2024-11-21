from pico2d import * 
from gfw import *


class Batter(Sprite):

    def __init__(self):
        super().__init__(f'res/Batter.png', 640 + 150, 200)
        self.center = [0, 0]
        self.batwidth = 40
        self.batheight = 40


    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            pass
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                self.center[0] = e.x
                self.center[1] = 720 - e.y
                print(self.center)


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return (self.center[0] - self.batwidth / 2, self.center[1] - self.batheight / 2, 
            self.center[0] + self.batwidth / 2, self.center[1] + self.batheight / 2)
