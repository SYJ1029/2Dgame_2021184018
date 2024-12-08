from pico2d import * 
from gfw import *
from Ball import *
from Player import *


class Base:
    def __init__(self, basetype, pos, defender):
        self.type = basetype
        self.x = pos[0]
        self.y = pos[1]
        self.x2 = pos[0] + 40
        self.y2 = pos[1] + 40
        self.ball = 0
        self.InPlayer = [False, False]
        self.InBall = [False, False]
        self.CheckIn()
        self.distList = list()
        self.defnum = 0

        self.defenderList = defender

    def CheckIn(self):
        if self.type == 3:
            self.InPlayer = [True, True]

    def handle_event(self, e):
        pass

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

        self.defenderList[self.defnum].baseIndex = self.type
        self.distList.clear()

        
        
        
            

    def draw(self): 
        pass