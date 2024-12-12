from pico2d import * 
from gfw import *
import copy

class SBOBox(Sprite):
    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

    
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)

class SBOCircle(Sprite):
    def __init__(self, filename, x, y, i):
        super().__init__(filename, x, y)
        self.filenamepiece = [filename, 'res/gCircle.png', 'res/yCircle.png', 'res/rCircle.png']
        self.index = i
        self.subindex = i

    def ChangeFileName(self):
        if self.index != 0: self.index = 0 
        else: self.index =  self.subindex
        self.filename = self.filenamepiece[self.index]

    def RenderFileName(self):

        print(f'{self.filename=}')
        self.image = image.load(self.filename)

    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x, self.y)

global sbo