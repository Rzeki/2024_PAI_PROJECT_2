import GameObject

class Trigger(GameObject):
    
    def __init__(self) -> None:
        self.trigger_region = None
        pass
    
    def Try(self, bot):
        pass
    
    def Update(self):
        pass
    
    
class TriggerRegion:
    def __init__(self) -> None:
        pass
    
    def isTouching(self):
        pass
    
class TriggerRegion_Circular(TriggerRegion):
    def __init__(self) -> None:
        pass
    
    def isTouching(self):
        pass