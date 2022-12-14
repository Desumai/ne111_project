import sys
sys.path.append((sys.path[0])[0:sys.path[0].rfind('ThrowableItems')])

import pygame
from ThrowableObject import ThrowableObject
from States import State as STATES
from Constants import Constants as const

class GravityItem(ThrowableObject):
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
        self.type = 1
        
    def throwSpeedFunction(self):
        return self.throwSpeed

    def start(self):
        pass

    def onDestroy(self):
        pass
    
    def render(self):
        
        pygame.draw.rect(STATES.SCREEN, (0, 255, 0), self.rigidBody)
        pass

    def update(self):
        if(self.checkIfThrownOver()):
            self.handleThrownOver()
        if(self.isClicked):
            self.velocity = (0, 0)
            self.pos = self.getPosFromCenter(STATES.MOUSE_POS)
        elif(self.flyTimer > 0):
            if(not self.translate(self.velocity)):
                self.flyTimer = 0
            else: 
                self.flyTimer -= 1
        else:
            x = self.pos[0] + self.velocity[0]
            y = self.pos[1] + self.velocity[1]
            xVel = self.velocity[0]
            yVel = self.velocity[1]
            if(x <= 0):
                x = 0
                xVel = 0
            elif(x >= const.SCREEN_SIZE[0] - self.size[0]):
                x = const.SCREEN_SIZE[0] - self.size[0]
                xVel = 0
            if(y >= const.SCREEN_SIZE[1]- self.size[1]):
                y = const.SCREEN_SIZE[1] - self.size[1]
                yVel = 0
                xVel = 0
            elif(y <= const.THROW_OVER_HEIGHT):
                y = const.THROW_OVER_HEIGHT + 1
                if(yVel <= 0): yVel = 1
                else: yVel *= -1
            else:
                yVel += 1
            self.pos = (x, y)
            self.velocity = (xVel, yVel)


            
        self.rigidBody = pygame.Rect(self.pos, self.size)
        pass

    