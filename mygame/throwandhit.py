from pico2d import * 
from gfw import *
from Ball import Ball
from Pitcher import Pitcher
from Batter import Batter

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


    world.append(pitcher, world.layer.bgpitcher)
    world.append(batter, world.layer.bbbatter)



def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
        return
    if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
        ball = Ball(1)
        world.append(ball, world.layer.interaction)

        return

if __name__ == '__main__':
    gfw.start_main_module()

