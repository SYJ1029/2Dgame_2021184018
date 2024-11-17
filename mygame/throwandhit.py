from pico2d import * 
from gfw import *
import Ball
from Pitcher import Pitcher
import Batter

world = World(['bg', 'bgpitcher', 'bbbatter', 'interaction'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = True
shows_object_count = True

def enter():

    world.append(Background('res/Stadium1.png'), world.layer.bg)


    global pitcher
    pitcher = Pitcher()

    world.append(pitcher, world.layer.bgpitcher)
    world.append(Sprite('res/Batter.png', canvas_width / 2 + 150, 200), world.layer.bbbatter)



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

if __name__ == '__main__':
    gfw.start_main_module()

