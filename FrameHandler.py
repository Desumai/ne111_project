
import pygame as pg
from States import State
import math
from ThrowableObject import ThrowableObject
from Constants import Constants as const
import sys
import queue
from ExtraFunctions import createThrowableObjectFromMsg

class FrameHandler():
    """
        class for handling actions for each frame
    """

    def __init__(self) -> None:
        self.updateList = []
        self.renderList = []
        self.throwableList = []
        self.mousePrevPos = ()
        self.leftMouseIsDown = False


    def addGameObject(self, gameObject):
        self.updateList.append(gameObject)
        self.renderList.append(gameObject)

        ##sort the lists by prioritites
        self.updateList.sort(key=lambda x: x.updatePriority, reverse = True)
        self.renderList.sort(key=lambda x: x.renderPriority, reverse = True)


    def removeGameObject(self, gameObject):
        self.updateList.remove(gameObject)
        self.renderList.remove(gameObject)

    def addThrowable(self, throwableObject):
        self.throwableList.append(throwableObject)
    
    def removeThrowable(self, throwableObject = None, index = None):
        if(index is None and throwableObject is not None):
            self.throwableList.remove(throwableObject)
        elif(index is not None and throwableObject is None):
            del self.throwableList[index]

    def handleUpdates(self):
        for gameObject in self.updateList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()
        for temp in self.throwableList:
            temp.update()
    

    def handleRenders(self):
        pg.draw.rect(State.SCREEN, (255, 255, 255), pg.Rect(0,0, const.SCREEN_SIZE[0], const.SCREEN_SIZE[1]))
        for gameObject in self.renderList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.render()
        for temp in self.throwableList:
            temp.render()
        pg.display.flip()

    def handleMouseDragging(self):
        mousePressedState = pg.mouse.get_pressed()
        if (mousePressedState[0]):
            if(not self.leftMouseIsDown): #left mouse click
                throwableObject = ThrowableObject.findClicked(self.throwableList, pg.mouse.get_pos())
                if(throwableObject is not None):
                    throwableObject.isClicked = True
            self.leftMouseIsDown = True
        elif(self.leftMouseIsDown): #left mouse release
            throwableObject = ThrowableObject.getClicked(self.throwableList)
            if(throwableObject is not None):
                print(throwableObject)
                throwableObject.handleThrow()
            self.leftMouseIsDown = False

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                State.IS_RUNNING == False
                pg.quit()
                sys.exit()
            pass
        self.handleMouseDragging()

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
        self.handleUpdates()
        self.handleRenders()
        self.checkGameOver()
        pass

    def checkGameOver(self):
        if(State.TIME_REMAINING <= 0):
            self.handleGameOver()

    def handleGameOver(self):
        State.IS_RUNNING = False
        print("[GAME OVER]")

    def handleSpawning(self):
        
        pass

    def handleMsgs(self):
        while(State.RECIEVED_MSG_QUEUE.qsize() > 0):
            try:
                msg = State.RECIEVED_MSG_QUEUE.get()
                msgType = msg[0]
                if(msgType == 'd'):
                    #TODO:disconnect
                    pass
                if(msgType == 'o'):
                    self.addThrowable(createThrowableObjectFromMsg(msg))
                elif(msgType == 's'):
                    #TODO return score
                    pass
                elif(msgType == 'c'):
                    #TODO: handle score and game over
                    pass
                elif(msgType == 't'):
                    const.GAME_LENGTH == int(msg[2:])
            except queue.Empty:
                break
            except Exception:
                pass
    def calculateScore(self):
        score = 0
        for _ in self.throwableList:
            score += const.THROWING_TYPES_SCORES[const.THROWING_TYPES[str(_.type)]]
        return score
