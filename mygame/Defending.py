from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import *
from Player import Player


world = World(['bg', 'Objects', 'Ball', 'controller'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = True
shows_object_count = True

basePos = [[550, 580], [550, 250], 
           [870, 680], [650, 850], [330, 750], [230, 680],
           [150, 900], [550, 1050], [1100, 900]]

def enter():

    bg = ClipedScrollBackGround(f'res/Stadium_2.png')
    world.append(bg, world.layer.bg)
    world.bg = bg

    print(balldelta)
    global team1
    global team2
    team1 = [ Player(f'res/Pitcher.png', basePos[a][0], basePos[a][1]) for a in range(9)]
    team2 = [ Player(f'res/Pitcher.png', basePos[a][0], basePos[a][1]) for a in range(9)]

    ball = BallDefence([0, 0], 550, 250)

    for i in range(9):
        world.append(team1[i], world.layer.Objects)

    ball.inited = True
    ball.godraw = True
    ball.hit = True
    ball.area = 10
    world.append(ball, world.layer.Ball)

    ball.dx = balldelta[0]
    ball.dy = balldelta[1]





def exit():
    balldelta[0] = 0
    balldelta[1] = 0
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
         print(world.objects)

if __name__ == '__main__':
    gfw.start_main_module()

