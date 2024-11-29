from pico2d import * 
from gfw import *
from Pitcher import Pitcher
from Batter import Batter
from Ball import Ball
from Player import Player


world = World(['bg', 'Objects', 'controller'])

canvas_width = 1280
canvas_height = 720
shows_bounding_box = True
shows_object_count = True

def enter():

    bg = ClipedScrollBackGround(f'res/Stadium_2.png')
    world.append(bg, world.layer.bg)
    world.bg = bg

    global team1
    global team2
    team1 = [ Player(f'res/Pitcher.png', a * 10, a * 10) for a in range(10)]
    team2 = [ Player(f'res/Pitcher.png', a * 10, a * 10) for a in range(10)]

    for i in range(10):
        world.append(team1[i], world.layer.Objects)







def exit():
    world.clear()

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    pass

if __name__ == '__main__':
    gfw.start_main_module()

