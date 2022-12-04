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

    def init():
        pass