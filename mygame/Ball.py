from pico2d import * 
from gfw import *
import copy
from ScoreMenual import *
from SBOBox import *

global balldelta
balldelta = list([0, 0])


class Ball(Sprite):



    def __init__(self, ballarea, x, y):
        super().__init__(f'res/Ball.png',  x, y)
        
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
       

        self.bg.scroll(self.dx, self.dy)
        #print(self.area)


    def draw(self):
        if self.godraw:
            self.image.draw(self.x, self.y, self.ballwidth, self.ballheight)

    def get_bb(self):
        return (self.center[0] - (self.ballwidth / 2 - self.area), self.center[1] - (self.ballheight / 2 - self.area), 
                self.center[0] + (self.ballwidth / 2 - self.area), self.center[1] + (self.ballheight / 2 - self.area))




class BallAttack(Ball):
    def __init__(self, ballarea, x, y, sbo):
        super().__init__(ballarea, x, y)
        self.hit = False
        self.catch = False
        self.sbo = sbo
        self.index = [1, 0]

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

    def move(self):
        self.x += self.dx * self.t
        self.y += self.dy * self.t
        self.t += 0.00005

        if(self.area <= 0):
            self.catch = True



    def update(self):
        if(self.godraw and self.hit == False):
            self.area -= 0.1
            self.move()
        
        global Score, ScoreIndex, Strike, Ballcount, Out, attackSequence
        # print(f'{attackSequence}\n\n{Strike=}\n{Ballcount=}\n{Out=}')

        if(self.area <= 0):
            self.clear()
            
            if(self.catch):
                Strike += 1

                if Strike == 3:
                    Out += 1
                    print(f'{attackSequence}\n\n{Strike=}\n{Ballcount=}\n{Out=}')
                    Strike = 0
                    Ballcount = 0
                    self.sbo[1][0].ChangeFileName()
                    self.sbo[1][0].RenderFileName()
                    self.sbo[1][1].ChangeFileName()
                    self.sbo[1][1].RenderFileName()
                    if Out < 3:
                        self.sbo[2][Out - 1].ChangeFileName()
                        self.sbo[2][Out - 1].RenderFileName()
                else:
   
                    self.sbo[1][Strike - 1].ChangeFileName()
                    self.sbo[1][Strike - 1].RenderFileName()
                if Out >= 3:
                    ChangeAtt()
                    if attackSequence == True:
                        ScoreIndex += 1
                    Out = 0
                    self.sbo[2][0].ChangeFileName()
                    self.sbo[2][0].RenderFileName()
                    self.sbo[2][1].ChangeFileName()
                    self.sbo[2][1].RenderFileName()
                self.catch = False
            




class BallDefence(Ball):
    def __init__(self, ballarea, x, y, position):
        super().__init__(ballarea, x, y)
        self.t = 0
        self.z = 0
        self.dz = 1
        self.theta = 0
        self.initxy = [copy.deepcopy(x), copy.deepcopy(y)]
        self.defnum = position
        self.distlist = list()
        self.first = True
        self.base = None
        self.prevx = copy.deepcopy(self.x)
        self.prevy = copy.deepcopy(self.y)

        self.drawpos = copy.deepcopy(self.initpos)
        self.catch = False
        self.bound = False
        self.InPlayer = False
        

    def InitBase(self, base):
        self.base = base
    def move(self):
        global Score, ScoreIndex, Out, attackSequence, runs, runInterval, delaytime
        if(self.t < 1):
            self.x = self.initpos[0] + self.dx * self.t
            self.y = self.initpos[1] + self.dy * self.t
            self.prevx = self.drawpos[0] + self.dx * self.t * 0.25
            self.prevy = self.drawpos[1] + self.dy * self.t * 0.25
            self.t += 0.01
            

            # self.prevx = copy.deepcopy(self.x)
            # self.prevy = copy.deepcopy(self.y)
        else:
            self.bound = True
            delaytime += 1
   
    def update(self):
        global Score, ScoreIndex, Out, attackSequence, delaytime, runInterval, runs
        if(self.godraw):
            self.move()

       
        # if(self.area <= 0):
        #     self.clear()
        self.bg.scrollTo(self.prevx + self.ballwidth, self.prevy + self.ballheight)

        mindist = float("inf")
        for i in range(len(self.distlist)):
            if(self.distlist[i][0] < mindist):
                mindist = copy.deepcopy(self.distlist[i][0])
                self.defnum = self.distlist[i][1]
                
        # print(f'{mindist=}, {self.defnum=}')

        if(self.t >= 1):
            # self.dx = 0
            # self.dy = 0
            if(self.first == True):
                print(f'<ball>\n {self.dx=}, {self.dy=}')
                print(f'{self.x=}, {self.y=}')
                print(f'{mindist=}, {self.defnum=}')
                print(self.distlist[9 - self.defnum])
                self.first = False

            
            self.initpos = copy.deepcopy([self.x, self.y])
            self.drawpos = copy.deepcopy([self.prevx, self.prevy])
        else:
            self.first = True

    
        self.distlist.clear()
        if(delaytime > runInterval):
            runs += 1
            delaytime = 0
            pop()
            # import Defending
            # Defending.exit()


    def handle_event(self, e):
        pass

    def draw(self):
        if self.godraw:
            self.image.draw(self.initxy[0], self.initxy[1], self.ballwidth, self.ballheight)