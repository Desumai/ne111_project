
import pygame as pg
from States import State
import math

class FrameHandler():
    """
        class for handling actions for each frame
    """

    def __init__(self) -> None:
        self.updateList = []
        self.renderList = []
        self.mousePrevPos = ()


    def addGameObject(gameObject, self):
        self.updateList.append(gameObject)
        self.renderList.append(gameObject)

        ##sort the lists by prioritites
        self.updateList.sort(key=lambda x: x.updatePriority, reverse = True)
        self.renderList.sort(key=lambda x: x.RenderPriority, reverse = True)


    def removeGameObject(gameObject, self):
        self.updateList.remove(gameObject)
        self.renderList.remove(gameObject)


    def handleUpdates(self):
        for gameObject in self.updateList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()
    

    def handleRenders(self):
        for gameObject in self.renderList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                State.IS_RUNNING == False
            pass

    def calcMouseMovement(self):
        """
            calculates the movement of the mouse and gives information to [State]
        """
        
        State.MOUSE_POS = pg.mouse.get_pos()
        movement = pg.mouse.get_rel()

        if(movement == (0, 0)):
            State.MOUSE_SPD = 0
            State.MOUSE_DIRECTION = (0, 0)
        else:
            State.MOUSE_SPD = math.sqrt(movement[0]**2 + movement[1]**2)
            State.MOUSE_DIRECTION = (movement[0]/State.MOUSE_SPD, movement[1]/State.MOUSE_SPD)
            
        pass
        

    def frameTasks(self):
        self.handleEvents()
        self.calcMouseMovement()
        pass