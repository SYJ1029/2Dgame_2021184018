from pico2d import * 
from gfw import *
import copy

global balldelta
balldelta = list([0, 0])


class Ball(Sprite):



    def __init__(self, ballarea, x, y):
        super().__init__(f'res/Ball.png',  610, 240)
        
        self.area = 0
        self.center = [x, y]
        self.center += ballarea
        self.ballwidth = 40
        self.ballheight = 40
        self.initpos = copy.deepcopy(self.center)
        self.inited = False
        self.t = 0
        self.dx = 0
        self.dy = 0 
        self.godraw = False

        self.z = 0

    def initbbpos():
        pass
    
    def handle_event(self, e):
        pass


    
    
    def move(self):
        self.x += self.dx * self.t
        self.y += self.dy * self.t
        self.t += 0.00005

    def clear(self):
        self.godraw = False
        self.t = 0
        self.x = 600
        self.y = 310
        self.dx = 0        
        self.dy = 0
        self.inited = False

    def update(self):
        if(self.godraw):
            self.area -= 0.1
            self.move()
        
        if(self.area <= 0):
            self.clear()
        self.bg.scroll(self.dx, self.dy)
        #print(self.area)


    def draw(self):
        if self.godraw:
            self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return (self.center[0] - (self.ballwidth / 2 - self.area), self.center[1] - (self.ballheight / 2 - self.area), 
                self.center[0] + (self.ballwidth / 2 - self.area), self.center[1] + (self.ballheight / 2 - self.area))




class BallAttack(Ball):
    def __init__(self, ballarea, x, y):
        super().__init__(ballarea, x, y)
        self.hit = False


    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_KP_ENTER and self.dx == 0:
                self.area = self.ballwidth / 2
                self.dx = (self.center[0]) - self.x
                self.dy = (self.center[1]) - self.y
            if e.key >= SDLK_KP_1 and e.key <= SDLK_KP_9:
                token = e.key - SDLK_KP_0
                row = token // 3
                column = token % 3
                print(row, column)

                self.center[0] = self.initpos[0] + column * self.ballwidth
                self.center[1] = self.initpos[1] + row * self.ballheight


    def update(self):
        if(self.godraw and self.hit == False):
            self.area -= 0.1
            self.move()
        
        if(self.area <= 0):
            self.clear()


class BallDefence(Ball):
    def __init__(self, ballarea, x, y, position):
        super().__init__(ballarea, x, y)
        self.t = 0.01
        self.z = 0
        self.dz = 1
        self.theta = 0
        self.initxy = [copy.deepcopy(x), copy.deepcopy(y)]
        self.defnum = position
        self.distlist = list()
        
    def move(self):
        if(self.t < 1):
            self.x = self.initpos[0] + self.dx * self.t
            self.y = self.initpos[1] + self.dy * self.t
            self.t += 0.01

    def update(self):
        if(self.godraw):
            self.move()

        self.bg.scrollTo(self.x + self.ballwidth, self.y + self.ballheight)
        # if(self.area <= 0):
        #     self.clear()


        mindist = float("inf")
        for i in range(len(self.distlist)):
            if(self.distlist[i] < mindist):
                mindist = copy.deepcopy(self.distlist[i])
                self.defnum = i + 1

        if(self.t >= 1):
            print(f'{self.distlist=}')
            print(f'{mindist=}, {self.defnum=}')
        self.distlist.clear()

    def handle_event(self, e):
        pass