import pygame as pg
from abc import ABC, abstractmethod
from GameObject import GameObject
from States import State as STATES

class ThrowableObject(GameObject, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.rigidBody = None
        self.isClicked = False
        self.flyDuration = 30 #frames
        self.flyTimer = 0
        self.type = -1
        self.throwSpeed = 1
    
    def contains(self, point) -> bool:
        """
            checks if object contains the coordinate of the screen specified by [point]. Used to check if the object was clicked by the mouse.
            Returns [True] if contains [point], else returns [False]
        """
        print(self.rigidBody.collidepoint(point))
        return self.rigidBody.collidepoint(point)

    @abstractmethod
    def start(self): pass

    def simpleMove(self):
        if(not self.translate(self.velocity)):
            self.velocity = (0, 0)


    @staticmethod
    def findClicked(throwableList, point):
        throwableList.reverse()
        for item in throwableList:
            if (item.contains(point)):
                return item
    
    @staticmethod
    def getClicked(throwableList):
        """
            (List<ThrowableObject>) -> ThrowableObject
        """
        for item in throwableList:
            if(item.isClicked):
                return item

    @abstractmethod
    def throwSpeedFunction(self):
        pass

    def handleThrow(self):
        self.isClicked = False
        self.flyTimer = self.flyDuration
        self.velocity = (self.throwSpeed * STATES.MOUSE_DIRECTION[0], self.throwSpeed * STATES.MOUSE_DIRECTION[1])
    
    def createMsg(self):
        from Constants import Constants
        msg = f"o:{self.type} {self.size[0]},{self.size[1]} {Constants.SCREEN_SIZE[0] - self.pos[0]} {-self.velocity[0]},{-self.velocity[1]}" 
        return msg

    def checkIfThrownOver(self):
        from Constants import Constants
        #considered thrown over if more than half of the object is over the line
        return ((self.flyTimer >0) and (self.pos[1] + self.size[1]/2 < Constants.THROW_OVER_HEIGHT))

    def handleThrownOver(self):
        import connection
        STATES.FRAME_HANDLER.removeThrowable(throwableObject=self)
        connection.sendMsg(self.createMsg)

