
import pygame as pg
from States import State
import math
from ThrowableObject import ThrowableObject
from Constants import Constants as const
import sys
import queue
from ExtraFunctions import createThrowableObjectFromMsg
from random import randint, uniform

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


    def addGameObject(self, gameObject): #adds game object to list of object to update and render every frame
        self.updateList.append(gameObject)
        self.renderList.append(gameObject)

        ##sort the lists by prioritites
        self.updateList.sort(key=lambda x: x.updatePriority, reverse = True)
        self.renderList.sort(key=lambda x: x.renderPriority, reverse = True)


    def removeGameObject(self, gameObject): #removes game object from list of objects to render and update, effectively "destroying" it from the game
        self.updateList.remove(gameObject)
        self.renderList.remove(gameObject)

    def addThrowable(self, throwableObject): #like addGameObject but for throwables
        self.throwableList.append(throwableObject)
    
    def removeThrowable(self, throwableObject = None, index = None):
        if(index is None and throwableObject is not None):
            self.throwableList.remove(throwableObject)
        elif(index is not None and throwableObject is None):
            del self.throwableList[index]

    def handleUpdates(self): #object updates per frame
        for gameObject in self.updateList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()
        for temp in self.throwableList:
            temp.update()
    

    def handleRenders(self): #object rendering per frame
        pg.draw.rect(State.SCREEN, (255, 255, 255), pg.Rect(0,0, const.SCREEN_SIZE[0], const.SCREEN_SIZE[1]))
        for gameObject in self.renderList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.render()
        for temp in self.throwableList:
            temp.render()
        pg.display.flip()

    def handleMouseDragging(self): #handles mouse movement and behaviours
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

    def handleEvents(self): #handle pygame events
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
        

    def frameTasks(self): #tasks to do every frame
        self.handleEvents()
        self.calcMouseMovement()
        self.handleSpawning()
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

    def handleSpawning(self): #handles the spontaneous spawning behaviour of throwables
        if(randint(1, const.SPAWN_PROBABILITY) == const.SPAWN_PROBABILITY//2):
            spawnType = randint(0, 3)
            self.addThrowable(self.spawn(spawnType))
        pass

    def spawn(self, type): #spawns a randomized throwable of a given type
        from ThrowableItems.BasicItem import BasicItem
        from ThrowableItems.AvoidItem import AvoidItem
        from ThrowableItems.GravityItem import GravityItem
        from ThrowableItems.BounceItem import BounceItem
        size = (randint(15, const.THROW_OVER_HEIGHT-5), randint(15, const.THROW_OVER_HEIGHT-5))
        position = (randint(0, const.SCREEN_SIZE[0] - size[0]), randint(const.THROW_OVER_HEIGHT + 1, const.SCREEN_SIZE[1] - size[1]))

        if(type == 0):
            return BasicItem(position=position, size=size, sprite=None)
        elif(type == 1):
            return GravityItem(position=position, size=size, sprite=None)
        elif(type == 2):
            return BounceItem(position=position, size=size, sprite=None, velocity=(randint(0, 9)*uniform(-1, 1), randint(0, 9)*uniform(-1, 1)))
        elif(type == 3):
            return AvoidItem(position=position, size=size, sprite=None)

    def handleMsgs(self): #handles the queue of messages sent by the opposing player
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

    def calculateScore(self): #calculates player's current score
        score = 0
        for _ in self.throwableList:
            score += const.THROWING_TYPES_SCORES[const.THROWING_TYPES[str(_.type)]]
        return score
