import pygame as pg
import queue
import threading

class State():
    """
        class containing variables on the states of the program
    """

    SCENE = 0 ##current scene of the game
    SCREEN = None ## the screen of the game
    IS_RUNNING = False #if the "game" part is running 
    FRAME_HANDLER = None #reference to the FrameHandler object used for the game
    MOUSE_SPD = 0
    MOUSE_DIRECTION = None
    MOUSE_POS = None
    TIMER_FONT = None #font object for the timer font
    TIME_REMAINING = 1 #in milliseconds
    SCORE = 0

    #connectivity
    SOCKET_CONNECTION = None #the socket.socket of the client/server
    SERVER_ID = '' #id of the host server. Supposed to be the host's bluetooht MAC address but the ipv4 address is used instead
    ADDRESS = (None, None) #tuple containing server id and port
    IS_HOST = False #if this application is being the server host or client
    RECIEVED_MSG_QUEUE = queue.Queue() #Queue of the messages recieved from the opposing player. Queue should be checked emptied out each frame
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

        
