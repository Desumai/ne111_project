"""
    Run this file to start game. 
"""
import pygame as pg
from Constants import Constants as const
from FrameHandler import FrameHandler
import time
import threading

pg.init()

isRunning = True
fh = FrameHandler()

def main():
    # TODO: create game window on startup and initialize game constants
    screen = pg.display.set_mode(const.SCREEN_SIZE)
    isRunning = True
    
    pass

def gameLoop():
    while isRunning:
        currentTime


if (__name__ == "__main__"):
    main()
