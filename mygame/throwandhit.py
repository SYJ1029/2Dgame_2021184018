from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import Ball

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
    ball = Ball([0, 0])


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
    if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
        if(ball.inited == False):
            ball.inited = True
            ball.godraw = True
    if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                batter.Check_collision(ball)
           

    
    ball.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

