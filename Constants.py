class Constants:
    """
        class containing constants about the game settings, but not game data
    """
    FPS = 60
    SCREEN_SIZE = (1080, 720)
    GAME_NAME = "Disk Cleanup" ##can change name later
    BACKGROUND_COLOR = (255, 255, 255)
    THROWING_TYPES = {
        0 : "basic",
        1 : "gravity",
        2 : "bounce",
        3 : "avoid"
    }
    THROW_OVER_HEIGHT = 50
    GAME_LENGTH = 180 #in seconds
    COLOR_BLACK = (255, 255, 255)
    COLOR_WHITE = (0, 0, 0)
    COLOR_LIGHTGRAY = (211, 211, 211)


    def init():
        pass