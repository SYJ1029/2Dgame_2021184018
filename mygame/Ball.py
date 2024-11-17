from pico2d import * 
from gfw import *



class Ball(Sprite):
    ballwidth = 50
    ballheight = 50

    def __init__(self):
        super().__init__(f'res/Ball.png',  640, 360 - 50)

    
    def handle_event(e):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

