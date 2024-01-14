import pygame as pg
import sys
import util

from GameWorld import GameWorld


class Game:
    def __init__(self) -> None:
        pg.init()
        self.window : pg.Surface = pg.display.set_mode((util.screen_wdth, util.screen_hgth))
        self.clock = pg.time.Clock()
        self.game_world = GameWorld(self.window)
        
        self.start_screen = pg.image.load("assets\start.png")
        self.end_screen = pg.image.load("assets\over.png")
        self.running : bool = True
        self.game_over : bool = False
        
    def run(self) -> None:
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()    
                    sys.exit()
#===========START MENU==================================================
            # if not self.running and not self.game_over:
            #     self.window.blit(self.start_screen, pg.Vector2(0,0))
            #     pg.display.update()
                
            #     keys = pg.key.get_pressed()
            #     if keys[pg.K_SPACE]:
            #         self.running = True
            #     elif keys[pg.K_ESCAPE]:
            #         pg.quit()    
            #         sys.exit()
#===========GAME LOOP====================================================
            if self.running:
                self.update()
                keys = pg.key.get_pressed()
                if keys[pg.K_ESCAPE]:
                    pg.quit()    
                    sys.exit()
#===========GAME OVER====================================================
            # elif self.game_over:
            #     self.window.blit(self.end_screen, pg.Vector2(0,0))
            #     pg.display.update()
                
            #     keys = pg.key.get_pressed()
            #     if keys[pg.K_r]:
            #         self.game_world = GameWorld(self.window)
            #         self.running = True
            #         self.game_over = False
            #     elif keys[pg.K_ESCAPE]:
            #         pg.quit()    
            #         sys.exit()
                
                
    def update(self) -> None:
        
        dt : int = self.clock.tick(180)
                
        #===================DRAWING=============================        
        self.game_world.draw()
        
        #===================COLLISION===========================

        
        
        #===================MOVEMENT============================
        self.game_world.update(dt)
        
        
        #===================DEBUG============================
        # print(agent.velocity)        
                
                
        pg.display.update()
            
            
        
        
if __name__=="__main__":
    
    Game().run()