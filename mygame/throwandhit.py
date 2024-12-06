from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import *
import Defending


world = World(['bg', 'bgpitcher', 'bbbatter', 'interaction'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = True
shows_object_count = True

def enter():

    world.append(Background('res/Stadium1.png'), world.layer.bg)


    global pitcher
    global ball
    global batter

    pitcher = Pitcher()
    batter = Batter()
    ball = BallAttack([0, 0], 610, 240)


    world.append(pitcher, world.layer.bgpitcher)
    world.append(batter, world.layer.bbbatter)
    world.append(ball, world.layer.interaction)




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
                        ball.dx = (overlap[1][0] - overlap[0][0]) * 20
                        ball.dy = (overlap[1][1] - overlap[0][1]) * 20

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
                            gfw.push(Defending)

                    else:
                        pass
           
    

    ball.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

