import pygame as pg
import queue
import threading

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

    #connectivity
    SOCKET_CONNECTION = None
    SERVER_ID = '10.34.134.239'
    ADDRESS = None
    FORMAT = 'utf-8'
    DISCONNECT_MSG = "!!!"
    IS_HOST = False
    RECIEVED_MSG_QUEUE = queue.Queue()
    CONNECTION_THREAD = None

    @staticmethod
    def init(screen, frameHandler):
        from Constants import Constants
        print("blah")
        State.SCENE = 0
        State.SCREEN = screen
        State.IS_RUNNING = True
        State.FRAME_HANDLER = frameHandler
        State.TIMER_FONT = pg.font.Font("Photonico.ttf", 32)
        State.ADDRESS = (State.SERVER_ID, Constants.PORT)

    @staticmethod
    def newGame(screen, frameHandler):
        State.init(screen= screen, frameHandler= frameHandler)
        
