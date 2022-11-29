import sys
sys.path.append((sys.path[0])[0:sys.path[0].rfind('ThrowableItems')])

import pygame
from GameObject import GameObject
from ThrowableObject import ThrowableObject
from States import State as STATES
from Constants import Constants as const

class BasicItem(ThrowableObject):
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
        
    def throwSpeedFunction(self):
        return self.throwSpeed

    def start(self):
        pass

    def onDestroy(self):
        pass
    
    def render(self):
        
        pygame.draw.rect(STATES.SCREEN, (0, 0, 0), self.rigidBody)
        pass

    def update(self):
        if(self.isClicked):
            self.velocity = (0, 0)
            self.pos = self.getPosFromCenter(STATES.MOUSE_POS)
        elif(self.flyTimer > 0):
            self.simpleMove()
            self.flyTimer -= 1
        else:
            velocity = (0, 0)
        self.rigidBody = pygame.Rect(self.pos, self.size)
        pass

    