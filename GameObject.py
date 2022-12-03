from abc import ABC, abstractmethod
from Constants import Constants as const

class GameObject(ABC):
    """
        class for "game objects" in the game. To be used as an interface like in other programming languages
    """

    def __init__(self) -> None:
        super().__init__()
        self.isActive = True
        self.updatePriority = 0 ##priority for updating. 0 by default. The greater the number, the higher its priority to be updated first. Negative numbers are allowed
        self.renderPriority = 0 ##same as "updatePriority". Game objects that are rendered LAST will be drawn ontop of other game objects (i think)
        self.pos = None #the coordinate for the top left corner of the object. A two entry float tuple
        self.size = (0 ,0)
        self.sprite = None
        self.velocity = (0, 0)
        self.center = None #coordinate of center of game object

    @abstractmethod
    def start(self):
        """
            runs once when the game object is created
        """
        pass

    @abstractmethod
    def onDestroy(self):
        """
            runs once when the game object is destroyed
        """
        pass

    @abstractmethod
    def update(self):
        """
            runs once every frame. Used to update the game object
            runs before screen rendering, the "render()" methods
        """
        pass

    @abstractmethod
    def render(self):
        """
            runs once every frame. Used to update the game object's graphics on the game screen
            runs after frame updates, the "update()" methods
        """
        pass

    @abstractmethod
    def contains(self, point) -> bool:
        """
            (tuple(int, int)) -> bool

            Determines if a point on the screen is contained in the game object. Returns [True] if contained, else returns [False]. [point] is a 2-point tuple of two integers in the format (x, y) with the upper left corner of the screen being (0, 0). 
        """
        pass

    def getCenter(self):
        return (self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2)

    def getPosFromCenter(self, center):
        return (center[0] - self.size[0]/2, center[1] - self.size[1]/2)
    
    def translate(self, xy):
        """
        (tuple(float, float)) -> bool

        translates [self] by [xy] but stops [self] from going out of bounds. If [self] was stoped, returns [False]. Else returns [True]
        """
        fullyMoved = True
        x = max(min(self.pos[0] + xy[0], const.SCREEN_SIZE[0] - self.size[0]), 0)
        y = max(min(self.pos[1] + xy[1], const.SCREEN_SIZE[1] - self.size[1]), 0)
        if(x != self.pos[0] + xy[0] or y != self.pos[1] + xy[1]):
            fullyMoved = False
        self.pos = (x, y)
        return fullyMoved

        
