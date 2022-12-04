"""
    Run this file to start game. 
"""
import pygame as pg
from Constants import Constants as const
from FrameHandler import FrameHandler
from States import State as STATES
from ThrowableItems.BasicItem import BasicItem
from ThrowableItems.BounceItem import BounceItem
from ThrowableItems.GravityItem import GravityItem
from ThrowableItems.AvoidItem import AvoidItem
from TimerBar import TimerBar
import time
import threading

pg.init()



def main():
    screen = pg.display.set_mode(const.SCREEN_SIZE)
    pg.display.set_caption(const.GAME_NAME)
    screen.fill(const.BACKGROUND_COLOR)
    print(STATES.IS_RUNNING)
    pg.display.flip()
    fh = FrameHandler()
    print(STATES.IS_RUNNING)
    STATES.newGame(screen = screen, frameHandler = fh)

    print(STATES.IS_RUNNING)
    #test objects
    fh.addGameObject(TimerBar())
    fh.addThrowable(BasicItem(position = (20, 50), size = (30, 40), sprite = None))
    fh.addThrowable(BasicItem(position = (50, 500), size = (25, 75), sprite = None))
    fh.addThrowable(BounceItem(position = (150, 100), size = (50, 60), sprite= None, velocity= (2,10)))
    fh.addThrowable(GravityItem(position = (200, 120), size = (60, 50), sprite= None))
    fh.addThrowable(AvoidItem(position = (40, 120), size = (60, 50), sprite= None))

    gameLoop()
    pass

def gameLoop():
    while STATES.IS_RUNNING:
        startTime = time.time()
        nextFrameTime = startTime + 1/const.FPS

        STATES.FRAME_HANDLER.frameTasks()

        timeRemaining = nextFrameTime - time.time()
        if(timeRemaining > 0):
            time.sleep(timeRemaining)
        
        #print(1/(time.time()-startTime)) #print fps


if (__name__ == "__main__"):
    main()
