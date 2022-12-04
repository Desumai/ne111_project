import sys
sys.path.append((sys.path[0])[0:sys.path[0].rfind('ThrowableItems')])

import pygame
from GameObject import GameObject
from ThrowableObject import ThrowableObject
from States import State as STATES
from Constants import Constants as const
from ExtraFunctions import ExtraFunctions as EF

class AvoidItem(ThrowableObject):
    def __init__(self, position, size, sprite, velocity = (0, 0) ) -> None:
        super().__init__()

        self.sprite = sprite
        self.pos = position
        self.size = size
        self.rigidBody = pygame.Rect(position, size)
        if(velocity != (0, 0)):
            self.velocity = velocity
            self.flyTimer = self.flyDuration
        self.throwSpeed = 10
        self.type = 3
        self.avoidSpeed = 5 #speed at which object avoids mouse
        self.avoidRange = 60 #distance from the mouse where avoiding behaviour starts (inclusive)
        
    def throwSpeedFunction(self):
        return self.throwSpeed

    def start(self):
        pass

    def onDestroy(self):
        pass
    
    def render(self):
        
        pygame.draw.rect(STATES.SCREEN, (0, 0, 255), self.rigidBody)
        pass

    def update(self):
        if(self.isClicked):
            self.velocity = (0, 0)
            self.pos = self.getPosFromCenter(STATES.MOUSE_POS)
        elif(self.flyTimer > 0):
            self.simpleMove()
            self.flyTimer -= 1
            if (self.flyTimer == 0):
                self.velocity = (0, 0)
        else:
            center = self.getCenter()
            distance = EF.calculateDistanceFromMouse(center)
            if(distance <= self.avoidRange):
                xVel = (center[0] - STATES.MOUSE_POS[0])/distance * self.avoidSpeed
                yVel = (center[1] - STATES.MOUSE_POS[1])/distance * self.avoidSpeed
                self.velocity = (xVel, yVel)
                self.translate(self.velocity)
                if(self.pos[1] <= const.THROW_OVER_HEIGHT):
                    self.pos = (self.pos[0], const.THROW_OVER_HEIGHT)
            else:
                self.velocity = (0, 0)
        self.rigidBody = pygame.Rect(self.pos, self.size)
        pass

    