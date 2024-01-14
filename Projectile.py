from GameObject import MovingObject

class Projectile(MovingObject):
    def __init__(self) -> None:
        self.gameworld = None
        self.defaultrounds = None
        self.maxrounds = None
        self.firerate = None
        self.idealrange = None
        self.projectilespeed = None
        self.owner = None
        
    def ShootAt(self):
        pass
    
    def Render(self):
        pass
    
    
    
    
    
        