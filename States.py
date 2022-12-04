import pygame as pg

class State():
    """
        class containing variables on the states of the program
    """

    SCENE = 0 ##current scene of the game
    SCREEN = None ## the screen of the game
    IS_RUNNING = False
    FRAME_HANDLER = None
    MOUSE_SPD = 0
    MOUSE_DIRECTION = None
    MOUSE_POS = None
    TIMER_FONT = None

    @staticmethod
    def init(screen, frameHandler):
        print("blah")
        State.SCENE = 0
        State.SCREEN = screen
        State.IS_RUNNING = True
        State.FRAME_HANDLER = frameHandler
        State.TIMER_FONT = pg.font.Font("Photonico.ttf", 32)

    @staticmethod
    def newGame(screen, frameHandler):
        State.init(screen= screen, frameHandler= frameHandler)
        
