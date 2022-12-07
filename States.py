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
    TIME_REMAINING = 1 #in milliseconds
    SCORE = 0

    #connectivity
    SOCKET_CONNECTION = None
    SERVER_ID = ''
    ADDRESS = None
    IS_HOST = False
    RECIEVED_MSG_QUEUE = queue.Queue()
    CONNECTION_THREAD = None
    CLIENT_TUPLE = (None, None) #only for server side

    @staticmethod
    def init(screen, frameHandler): # set values of variables when called upon from newGame()
        from Constants import Constants
        print("blah")
        State.SCENE = 0
        State.SCREEN = screen
        State.IS_RUNNING = True
        State.FRAME_HANDLER = frameHandler
        State.TIMER_FONT = pg.font.Font("Photonico.ttf", 32)
        State.ADDRESS = (State.SERVER_ID, Constants.PORT)

    @staticmethod
    def newGame(screen, frameHandler): # Called upon from main.py when game starts 
        State.init(screen= screen, frameHandler= frameHandler)

        
