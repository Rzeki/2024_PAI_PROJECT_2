import random
from pygame import Vector2 as Vec2

DEBUG : bool = True
screen_wdth, screen_hgth = 960, 540

grid : int = 60

def grid_to_coord(x : int, y : int) -> Vec2 :
    return Vec2(x*grid+grid/2, y*grid+grid/2)

def coord_to_grid(pos : Vec2) -> (int, int) :
    w, h = 0, 0
    for i in range(0, screen_wdth, grid) :
        if pos.x > i and pos.x < i+grid:
            break
        w += 1
    for i in range(0, screen_hgth, grid) :
        if pos.x > i and pos.x < i+grid:
            break
        h += 1
    return w, h