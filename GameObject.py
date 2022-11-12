from abc import ABC, abstractmethod

class GameObject(ABC):
        """
            class for "game objects" in the game. To be used as an interface like in other programming languages
        """

    ##Attributes
    isActive = True

    @abstractmethod
    def start():
        """
            runs once when the game object is created
        """
        pass

    @abstractmethod
    def onDestroy():
        """
            runs once when the game object is destroyed
        """
        pass

    @abstractmethod
    def update():
        """
            runs once every frame. Used to update the game object
            runs before screen rendering, the "render()" methods
        """
        pass

    @abstractmethod
    def render():
        """
            runs once every frame. Used to update the game object's graphics on the game screen
            runs after frame updates, the "update()" methods
        """
        pass
