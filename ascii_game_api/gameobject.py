from abc import ABC, abstractmethod

from ascii_loader import Entity
from ascii_renderer import Sprite


# TODO: add depth property?


class GameObject(Entity, ABC):
    """
    An object that can be added to a game
    """

    _sprite: Sprite

    def __init__(self, sprite: Sprite, x: int, y: int):
        """
        Initializes the class

        :param sprite: The game object's sprite
        :param x: The game object's x position in a game
        :param y: The game object's y position in a game
        """
        super().__init__(x, y)
        self._sprite = sprite

    @property
    def sprite(self) -> Sprite:
        return self._sprite

    @abstractmethod
    def on_spawn(self):
        """
        Performs the game object's spawn event; 
        This method should only ever be called by a game's spawn method
        """

    @abstractmethod
    def on_despawn(self):
        """
        Performs the game object's despawn event;
        This method should only ever be called by a game's despawn method
        """
