

class FrameHandler():
    """
        class for handling actions for each frame
    """

    gameObjects = []

    def handleUpdates():
        for gameObject in gameObjects:
            if (gameObject is None):
                gameObjects.remove(gameObject)
            elif (gameObject.isActive):
                gameObject.update()
    
