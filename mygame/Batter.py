from pico2d import * 
from gfw import *
from Ball import Ball

class Batter(Sprite):

    def __init__(self):
        super().__init__(f'res/Batter.png', 640 + 150, 200)
        self.center = [0, 0]
        self.batwidth = 40
        self.batheight = 40


    def handle_event(self, e, ball):
        if e.type == SDL_KEYDOWN:
            pass
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                self.center[0] = e.x
                self.center[1] = 720 - e.y
                print(self.center)
                self.Check_collision(ball)


    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return (self.center[0] - self.batwidth / 2, self.center[1] - self.batheight / 2, 
            self.center[0] + self.batwidth / 2, self.center[1] + self.batheight / 2)
    

    def GetOverlapBox(self, ball):
        batterbb = [[self.center[0] - self.batwidth / 2, self.center[1] - self.batheight / 2], 
                [self.center[0] + self.batwidth / 2, self.center[1] + self.batheight / 2]]
        print(f'Batterbb: {list(batterbb)}\n')

        ballbb = [[ball.center[0] - ball.ballwidth / 2, ball.center[1] - ball.ballwidth / 2], 
                [ball.center[0] + ball.ballwidth / 2, ball.center[1] + ball.ballwidth / 2]]
        print(f'Ballbb: {list(ballbb)}\n')

        overlap1 = [max(batterbb[0][0], ballbb[0][0]), max(batterbb[0][1],ballbb[0][1])]
        overlap2 = [min(batterbb[1][0], ballbb[1][0]), min(batterbb[1][1], ballbb[1][1])]
        print(f'overlapbb: {list(overlap1)}, {list(overlap2)}')

        if overlap1[0] < overlap2[0] and overlap1[1] < overlap2[1]:
            return [overlap1, overlap2]
        else:
            return None  # 겹치는 영역 없음

    def Check_collision(self, ball):
        overlap = self.GetOverlapBox(ball)

        if overlap != None:
            area = (overlap[1][0] - overlap[0][0]) * (overlap[1][1] - overlap[0][1])
            print(area)
            return area
        
        return None
   
