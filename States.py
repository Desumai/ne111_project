import pygame as pg

class State():
    """
        class containing variables on the states of the program
    """

    SCENE = 0 ##current scene of the game
    SCREEN = None ## the screen of the game
    IS_RUNNING = True
    FRAME_HANDLER = None

    @staticmethod
    def init(screen, frameHandler):
        global SCENE
        global SCREEN
        global IS_RUNNING
        global FRAME_HANDLER

        SCENE = 0
        SCREEN = screen
        IS_RUNNING = True
        FRAME_HANDLER = frameHandler