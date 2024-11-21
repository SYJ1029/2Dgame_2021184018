from pico2d import * 
from gfw import *



class Ball(Sprite):
    ballwidth = 40
    ballheight = 40
    area = 0
    maxarea = 40 * 40
    center = [650, 200]


    def __init__(self, ballarea):
        super().__init__(f'res/Ball.png',  600, 360 - 50)
        self.center += ballarea
        self.ballwidth = 40
        self.ballheight = 40
        self.area = 0

    def initbbpos():
        pass
    
    def handle_event(e):
        pass

    def update(self):
        self.area += 1

    def draw(self):
        self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return (self.center[0] - self.ballwidth / 2, self.center[1] - self.ballheight / 2, 
                self.center[0] + self.ballwidth / 2, self.center[1] + self.ballheight / 2)

