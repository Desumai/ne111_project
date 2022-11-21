

class FrameHandler():
    """
        class for handling actions for each frame
    """

    def __init__(self) -> None:
        self.updateList = []
        self.renderList = []


    def addGameObject(gameObject, self):
        self.updateList.append(gameObject)
        self.renderList.append(gameObject)

        ##sort the lists by prioritites
        self.updateList.sort(key=lambda x: x.updatePriority, reverse = True)
        self.renderList.sort(key=lambda x: x.RenderPriority, reverse = True)


    def removeGameObject(gameObject, self):
        self.updateList.remove(gameObject)
        self.renderList.remove(gameObject)


    def handleUpdates(self):
        for gameObject in self.updateList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()
    

    def handleRenders(self):
        for gameObject in self.renderList:
            if (gameObject is None):
                self.removeGameObject(gameObject)
            elif (gameObject.isActive):
                gameObject.update()

    def frameTasks(self):
        pass