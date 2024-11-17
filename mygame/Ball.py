from pico2d import * 
from gfw import *



class Ball(Sprite):

    def __init__(self):
        super().__init__(f'res/Ball.png',  640, 360 - 50)
    
    def handle_event(e):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 32, self.x + 30, self.y + 28

