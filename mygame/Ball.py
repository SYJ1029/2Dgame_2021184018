from pico2d import * 
from gfw import *
import copy



class Ball(Sprite):
    ballwidth = 40
    ballheight = 40
    area = 20
    initpos = [0, 0]
    maxarea = 40 * 40
    center = [610, 240]
    inited = False
    godraw = False


    def __init__(self, ballarea):
        super().__init__(f'res/Ball.png',  600, 360 - 50)
        self.center += ballarea
        self.ballwidth = 40
        self.ballheight = 40
        self.initpos = copy.deepcopy(self.center)
        self.inited = False
 

    def initbbpos():
        pass
    
    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_RETURN:
                print('It works!')
                print()
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
        
        if(self.area <= 0):
            self.godraw = False
        #print(self.area)

    def draw(self):
        if self.godraw:
            self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return (self.center[0] - (self.ballwidth / 2 - self.area), self.center[1] - (self.ballheight / 2 - self.area), 
                self.center[0] + (self.ballwidth / 2 - self.area), self.center[1] + (self.ballheight / 2 - self.area))

