from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import *
import Defending
from ScoreMenual import *
from SBOBox import *

world = World(['bg', 'bgpitcher', 'bbbatter', 'interaction'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = False
shows_object_count = True

sbo_basepos = [[[95, 650], [155, 650], [215, 650]], [[95, 600], [155, 600]], [[95, 550], [155, 550]]]


def enter():

    world.append(Background('res/Stadium1.png'), world.layer.bg)
    world.append(SBOBox('res/SBOcanvas.png', 150, 600), world.layer.bg)

    global pitcher
    global ball
    global batter
    global sbo

    pitcher = Pitcher()
    batter = Batter()
    sbo = [[SBOCircle('res/blackCircle.png', sbo_basepos[i][j][0], sbo_basepos[i][j][1], i) for j in range(3 - i)] for i in range(3)]
    sbo[2].append(SBOCircle('res/blackCircle.png', sbo_basepos[2][1][0], sbo_basepos[2][1][1], 2))
    ball = BallAttack([0, 0], 610, 240, sbo)

    sbo[1][0].subindex = 2
    sbo[1][1].subindex = 2
    sbo[2][0].subindex = 3
    sbo[2][1].subindex = 3
    sbo[1][0].ChangeFileName()
    sbo[1][1].ChangeFileName()    
    sbo[2][0].ChangeFileName()    
    sbo[2][1].ChangeFileName()    

    world.append(pitcher, world.layer.bgpitcher)
    world.append(batter, world.layer.bbbatter)
    world.append(ball, world.layer.interaction)

    for i in range(3):
        for j in range(3 - i):
            world.append(sbo[i][j], world.layer.interaction)

    world.append(sbo[2][1], world.layer.interaction)


def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    batter.handle_event(e)

    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
    if e.type == SDL_KEYDOWN and (e.key == SDLK_KP_ENTER) :
        if(ball.inited == False):
            ball.inited = True
            ball.godraw = True
    if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                if(ball.area < ball.ballwidth / 2 * 0.25):
                    overlap = batter.Check_collision(ball)
                    if overlap is not None:
                        ball.dx = (overlap[1][0] - overlap[0][0]) * 24
                        ball.dy = (overlap[1][1] - overlap[0][1]) * 24  
                        
                        print(f'{overlap[0][0]=}\n')
                        if(overlap[0][0] < 650.0):
                            if(overlap[0][0] > 620):
                                ball.dx = 0
                            else:
                                ball.dx *= -1

                        balldelta[0] = (ball.dx)
                        balldelta[1] = (ball.dy)

                        print(ball.godraw)
                        if(overlap[2] < 400 or ball.godraw == False):
                            pass
                        else:
                            sbo[1][0].ChangeFileName()
                            sbo[1][1].ChangeFileName()  

                            gfw.push(Defending)

                    else:
                        pass
           
    

    ball.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

