from pico2d import * 
from gfw import *


class Batter(Sprite):

    def __init__(self):


        super().__init__(f'res/Batter.png', 640 + 150, 200)

    def handle_event(e):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
