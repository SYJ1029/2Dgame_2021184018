from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import *
from Player import *
from Base import Base
from ScoreMenual import *


world = World(['bg','Objects', 'Ball', 'controller'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = False
shows_object_count = True

#550 -> 390(-160)
#580 -> 600(-20)

basePos = [[390, 600], [390, 260], 
           [710, 680], [490, 950], [230, 950], [230 - 160, 680],
           [150 - 250, 1350], [550 - 160, 1450], [1100 - 50, 1350]]

bbasePos = [[750, 650], [450, 950], [50, 650], [390, 260]]

def enter():
    global Score, Strike, Ballcount, Out, attackSequence

    bg = ClipedScrollBackGround(f'res/Stadium_2.png')
    world.append(bg, world.layer.bg)
    world.bg = bg

    ball = BallDefence([0, 0], 390, 260, 0)

    ball.inited = True
    ball.godraw = True
    ball.hit = True
    ball.area = 10

    ball.dx = balldelta[0]
    ball.dy = balldelta[1]
    ball.bg = bg

    # print(balldelta)


    global team1
    global team2
    team1 = [ Player(f'res/Pitcher.png', basePos[a][0], basePos[a][1], ball, a+1) for a in range(9)]
    team2 = [ Player(f'res/Pitcher.png', basePos[a][0], basePos[a][1], ball, a+1) for a in range(9)]

    global base
    base = [Base(a, bbasePos[a], ball, team1) for a in range(4)]

    ball.InitBase(base)

    for i in range(9):
        team1[i].InitBase(base)
        team2[i].InitBase(base)

    for i in range(9):
        world.append(team1[i], world.layer.Objects)
    
    for i in range(4):
        world.append(base[i], world.layer.Objects)

    
    world.append(ball, world.layer.Ball)





def exit():

    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    baseNumber = 2


    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_RETURN:
            print(world.objects)
        if e.key == SDLK_a:
            baseNumber = 2
        elif e.key == SDLK_d:
            baseNumber = 0
        elif e.key == SDLK_w:
            baseNumber = 1
        elif e.key == SDLK_s:
            baseNumber = 3

    for a in range(9):
        if a < 4:
            base[a].handle_event(e, baseNumber)
        team1[a].handle_event(e)
if __name__ == '__main__':
    gfw.start_main_module()

