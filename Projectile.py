from GameObject import MovingObject

class Projectile(MovingObject):
    def __init__(self) -> None:
        self.gameworld = None
        self.target = None
        self.origin = None
        self.damageinflicted = None
        self.impactpoint = None
        self.projectilespeed = None
        self.owner = None
        
    def Update(self):
        pass
    
    def Render(self):
        pass
    
    
    
    
    
    
    
        