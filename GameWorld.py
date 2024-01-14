import pygame as pg
from pygame import Vector2 as Vec2
from GameObject import *


class GameWorld:
    def __init__(self, window : pg.surface) -> None:
        self.window = window
        self.window_w, self.window_h = window.get_size()
        
        #container of projectiles
        self.projectiles : list = []
        

    
    def update(self, dt : float) -> None :
        pass    
        
    def draw(self) -> None :
        self.window.fill(pg.Color(0,0,0)) # BACKGROUND