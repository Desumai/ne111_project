"""
    Run this file to start game. 
"""
import pygame as pg 
# import each class from their file so that their methods and variables can be accesed
from Constants import Constants as const
from FrameHandler import FrameHandler
from States import State as STATES
from ThrowableItems.BasicItem import BasicItem
from ThrowableItems.BounceItem import BounceItem
from ThrowableItems.GravityItem import GravityItem
from ThrowableItems.AvoidItem import AvoidItem
from TimerBar import TimerBar
import time
import connection
import threading

pg.init()


def main():
    #setup server-client connections
    print("[STARTING] Program is starting...")
    print("[INPUT REQUSTED] Do you wish to host a game(y/n)?")
    userInput = input()
    if(userInput == 'y'):
        STATES.IS_HOST = True
        STATES.SERVER_ID = connection.getAddress()
        
        connection.createServer()
        pass
    elif(userInput == 'n'):
        STATES.IS_HOST = False
        print('[INPUT REQUIRED] Enter the server address of the host:')
        STATES.SERVER_ID = input()
        connection.createClient()
        pass
    else:
        print("[ERROR] Invalid input. Program is closing...")
        time.sleep(3)
        return
    #setup GUI
    screen = pg.display.set_mode(const.SCREEN_SIZE) # Create screen variable to display the game screen using the set size from Constants class
    pg.display.set_caption(const.GAME_NAME) # Change window title to game name 'Disk Cleanup'
    screen.fill(const.BACKGROUND_COLOR) # Set background to white
    pg.display.flip() # Update entire display
    fh = FrameHandler() # create fh as an instance of FrameHandler class\
    # Call on newGame() function of States class and pass through newly created variables fh and screen as parameters to initialize STATES
    STATES.newGame(screen = screen, frameHandler = fh)
    

    print(STATES.IS_RUNNING) # Should be true after executing newGame()
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
    while STATES.IS_RUNNING: # Run this as long as IS_RUNNING is true
        startTime = time.time() # How much time has passed since the epoch in Coordinated Universal Time
        nextFrameTime = startTime + 1/const.FPS # Create variable to track when the next frame will occur  

        STATES.FRAME_HANDLER.frameTasks() # Run frameTasks; does all events that need to be completed each frame

        timeRemaining = nextFrameTime - time.time() # Find out how much time is left before next frame
        if(timeRemaining > 0):
            time.sleep(timeRemaining) # If there is still time left until the next frame stop this function from repeating to avoid updating the data twice in the same frame
        
        #print(1/(time.time()-startTime)) #print fps


if (__name__ == "__main__"):
    main()
