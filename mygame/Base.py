from pico2d import * 
from gfw import *
from Ball import *
from Player import *


class Base:
    def __init__(self, basetype, pos, ball, defender):
        self.type = basetype
        self.x = pos[0]
        self.y = pos[1]
        self.x2 = pos[0] + 40
        self.y2 = pos[1] + 40
        self.ball = ball
        self.InPlayer = [False, False]
        self.InBall = [False, False]
        self.CheckIn()
        self.distList = list()
        self.defnum = 0

        self.defenderList = defender

    def CheckIn(self):
        if self.type == 3:
            self.InPlayer = [True, True]

    def Conversion(self, key):
        keydict = {0: SDLK_d, 1: SDLK_w, 2: SDLK_a, 3: SDLK_s}

        return keydict[key]

    def handle_event(self, e, type):
        if e.type == SDL_KEYDOWN and self.type == type:
            if e.key == self.Conversion(self.type) and self.ball.catch:
                self.ball.dx = (self.x - self.ball.x)
                self.ball.dy = (self.y - self.ball.y)
                self.ball.t = 0
                self.InBall[0] = True
                self.ball.catch = False
                self.ball.godraw = True
            elif self.InBall[1]:
                self.InBall[0] = False

    def InitdistList(self):
        for i in range(len(self.defenderList)):
            self.distList.append([dist(self.x - self.defenderList[i].x, self.y - self.defenderList[i].y), i])

    def update(self):
        self.InitdistList()


        mindist = float("inf")
        for i in range(len(self.distList)):
            if(self.distList[i][0] < mindist):
                mindist = copy.deepcopy(self.distList[i][0])
                self.defnum = self.distList[i][1]

        if self.defenderList[self.defnum].baseIndex >= 5:
            self.defenderList[self.defnum].baseIndex = self.type
            self.InPlayer[0] = True

        self.distList.clear()

        
        
        
            

    def draw(self): 
        pass