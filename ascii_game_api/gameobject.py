from abc import ABC, abstractmethod

from ascii_loader import Entity
from ascii_renderer import Sprite

from utils import Direction

# TODO: add more events?
# TODO: centralized event manager?
# TODO: make event system in other project and import it?
# TODO: add solid property and collisions?
# TODO: setters for x and y that update this gameobject's location in the game
# TODO: on_spawn and on_despawn each set the gameobject's game (need to account for scenario where gameobject is in multiple games)


class GameObject(Entity, ABC):
    """
    An object that can be added to a game
    """

    _sprite: Sprite
    _depth: int
    is_solid: bool

    def __init__(self, sprite: Sprite, x: int, y: int, depth: int = 0, is_solid: bool = False):
        """
        Initializes the class

        :param sprite: The game object's sprite
        :param x: The game object's x coordinate in a game
        :param y: The game object's y coordinate in a game
        :param depth: The game object's depth in a game; the larger the depth, the lower the game object
        :param is_solid: Whether the game object is solid
        """
        super().__init__(x, y)
        self._sprite = sprite
        self._depth = depth
        self.is_solid = is_solid

    @property
    def sprite(self) -> Sprite:
        return self._sprite

    @property
    def depth(self) -> int:
        return self._depth

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
