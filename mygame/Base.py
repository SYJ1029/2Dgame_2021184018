from pico2d import * 
from gfw import *
from Ball import *
from Player import *


class Base:
    def __init__(self, basetype, pos):
        self.type = basetype
        self.x = pos[0]
        self.y = pos[1]
        self.x2 = pos[0] + 40
        self.y2 = pos[1] + 40
        self.ball = 0
        self.InPlayer = [False, False]
        self.InBall = [False, False]
        self.CheckIn()
        self.distlist = list()

    def CheckIn(self):
        if self.type == 3:
            self.InPlayer = [True, True]

    def handle_event(self, e):
        pass

    def update(self):
        mindist = float("inf")
        for i in range(len(self.distlist)):
            if(self.distlist[i][0] < mindist):
                mindist = copy.deepcopy(self.distlist[i][0])
                self.defnum = self.distlist[i][1]
            

    def draw(self): 
        pass