import pygame as pg
from abc import ABC, abstractmethod
from GameObject import GameObject
from ExtraFunctions import ExtraFunctions as EF
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

