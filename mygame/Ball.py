from pico2d import * 
from gfw import *
import copy



class Ball(Sprite):



    def __init__(self, ballarea):
        super().__init__(f'res/Ball.png',  600, 360 - 50)
        
        self.area = 20
        self.center = [610, 240]
        self.center += ballarea
        self.ballwidth = 40
        self.ballheight = 40
        self.initpos = copy.deepcopy(self.center)
        self.inited = False
        self.t = 0
        self.dx = 0
        self.dy = 0 
        self.inited = False
        self.godraw = False

    def initbbpos():
        pass
    
    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_RETURN and self.dx == 0:
                self.dx = (self.center[0]) - self.x
                self.dy = (self.center[1]) - self.y
            if e.key >= SDLK_1 and e.key <= SDLK_9:
                token = e.key - SDLK_0 - 1
                row = token // 3
                column = token % 3
                print(row, column)

                self.center[0] = self.initpos[0] + column * self.ballwidth
                self.center[1] = self.initpos[1] - row * self.ballheight

                pass



    def update(self):
        if(self.godraw):
            self.area -= 0.1
            self.move()
        
        if(self.area <= 0):
            self.godraw = False
            self.t = 0
        #print(self.area)

    def move(self):
        self.x += self.dx * self.t
        self.y += self.dy * self.t
        self.t += 0.00005

    def draw(self):
        if self.godraw:
            self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return (self.center[0] - (self.ballwidth / 2 - self.area), self.center[1] - (self.ballheight / 2 - self.area), 
                self.center[0] + (self.ballwidth / 2 - self.area), self.center[1] + (self.ballheight / 2 - self.area))

