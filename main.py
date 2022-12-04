"""
    Run this file to start game. 
"""
import pygame as pg
from Constants import Constants as const
from FrameHandler import FrameHandler
from States import State
from ThrowableItems.BasicItem import BasicItem
from ThrowableItems.BounceItem import BounceItem
from ThrowableItems.GravityItem import GravityItem
import time
import threading

pg.init()



def main():
    # TODO: create game window on startup and initialize game constants
    screen = pg.display.set_mode(const.SCREEN_SIZE)
    pg.display.set_caption(const.GAME_NAME)
    screen.fill(const.BACKGROUND_COLOR)
    State.SCREEN = screen
    pg.display.flip()
    global fh
    fh = FrameHandler()
    State.init(screen = screen, frameHandler = fh)
    #test objects
    fh.addThrowable(BasicItem(position = (20, 20), size = (30, 40), sprite = None))
    fh.addThrowable(BasicItem(position = (50, 500), size = (25, 75), sprite = None))
    fh.addThrowable(BounceItem(position = (150, 100), size = (50, 60), sprite= None, velocity= (2,10)))
    fh.addThrowable(GravityItem(position = (200, 120), size = (60, 50), sprite= None))
    gameLoop()
    pass

def gameLoop():
    while State.IS_RUNNING:
        startTime = time.time()
        nextFrameTime = startTime + 1/const.FPS

        fh.frameTasks()

        timeRemaining = nextFrameTime - time.time()
        if(timeRemaining > 0):
            time.sleep(timeRemaining)
        
        #print(1/(time.time()-startTime)) #print fps


if (__name__ == "__main__"):
    main()
