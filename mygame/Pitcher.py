from pico2d import *
from gfw import *




def make_rect(size, idx):
    x, y = idx % 100, idx // 100
    return (x * (size + 2) + 2, y * (size + 2) + 2, size, size)

def make_rects(size, idxs):
    return list(map(lambda idx: make_rect(size, idx), idxs))



class Pitcher(Sprite):
    ballLocation = {0, 0}


    def __init__(self):


        super().__init__(f'res/Pitcher.png',  640 - 10, 360 - 100 )
        ballLocation = {640, 360 - 50}

    def handle_event(e):
        pass

    def update(self):
        pass

    def draw(self):
        super().draw






