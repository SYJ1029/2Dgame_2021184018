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

#550 -> 390(-160)
#580 -> 600(-20)

basePos = [[390, 600], [390, 260], 
           [870 - 160, 680], [650 - 160, 950], [330 - 100, 950], [230 - 160, 680],
           [150 - 250, 1250], [550 - 160, 1350], [1100 - 50, 1250]]

def enter():

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


    for i in range(9):
        world.append(team1[i], world.layer.Objects)
    world.append(ball, world.layer.Ball)





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

