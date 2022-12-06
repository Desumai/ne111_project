from Constants import Constants as const
from GameObject import GameObject
from States import State as STATES
import pygame as pg
import time

class TimerBar(GameObject):
    def __init__(self) -> None:
        self.size = (const.SCREEN_SIZE[0], 50)
        self.renderPriority = -10
        self.updatePriority = -10
        self.isActive = True
        self.backgroundColor = const.COLOR_LIGHTGRAY
        self.timerText = "--:--:---" #minutes : seconds : milliseconds
        self.background = pg.Rect((0, 0), self.size)
        self.timerTextPos = None
        self.textRect = None
        self.startTime = time.time_ns()//1000000 #in milliseconds
        self.endTime = self.startTime + const.GAME_LENGTH * 1000 #in milliseconds

    def getTime(self):
        """
        returns remaining time in milliseconds (int). Also saves to [STATES.TIME_REMAINING]
        """
        STATES.TIME_REMAINING = self.endTime - time.time_ns()//1000000
        return STATES.TIME_REMAINING
    
    def timeToString(self, time):
        """
        (int) -> string
        returns [time] as a string in the format of "minutes:seconds:milliseconds"
        """
        if(time >= 0):
            return "{min:02}:{sec:02}:{millisec:03}".format(min = time//60000, sec = (time//1000)%60, millisec = time%1000)
        else:
            time = abs(time)
            return "-{min:02}:{sec:02}:{millisec:03}".format(min = time//60000, sec = (time//1000)%60, millisec = time%1000)
        

    def update(self):
        self.timerText = self.timeToString(self.getTime())
        self.textRect = STATES.TIMER_FONT.render(self.timerText, True, const.COLOR_WHITE, self.backgroundColor)
        if(self.timerTextPos is None):
            rect = self.textRect.get_rect()
            self.timerTextPos = ((const.SCREEN_SIZE[0] - rect.width)/2, self.background.centery - rect.height/2)


    def render(self):
        pg.draw.rect(STATES.SCREEN, self.backgroundColor, self.background)
        STATES.SCREEN.blit(self.textRect, self.timerTextPos)