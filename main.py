"""
    Run this file to start game. 
"""
import pygame as pg
from Constants import Constants as const
from FrameHandler import FrameHandler
from States import State
import time
import threading

pg.init()



def main():
    # TODO: create game window on startup and initialize game constants
    screen = pg.display.set_mode(const.SCREEN_SIZE)
    pg.display.set_caption(const.GAME_NAME)
    screen.fill(const.BACKGROUND_COLOR)
    pg.display.flip()
    global fh
    fh = FrameHandler()
    State.init(screen = screen, frameHandler = fh)

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
