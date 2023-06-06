from abc import ABC, abstractmethod
from ascii_game_api import Game

from ascii_loader import Entity
from ascii_renderer import Sprite

# TODO: add more events?


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

    # TODO: test
    def move(self, x: int, y: int, game: Game):
        """
        Moves this game object to the given x, y coordinates; if this game object is solid, and the 
        given x, y coordinates contains other solid game objects, the collision event of all solid game 
        objects will be triggered

        :param x: The x coordinate to move the game object to
        :param y: The y coordinate to move the game object to
        :param game: The environment of game objects that both includes and surrounds this game object
        """
        self._x = x
        self._y = y
        game.check_collision(self.x, self.y)

    @property
    def sprite(self) -> Sprite:
        return self._sprite

    @property
    def depth(self) -> int:
        return self._depth

    # TODO: needs to be passed more context?
    @abstractmethod
    def on_spawn(self):
        """
        Performs the game object's spawn event; 
        This method should only ever be called by a game's spawn method
        """

    # TODO: needs to be passed more context?
    @abstractmethod
    def on_despawn(self):
        """
        Performs the game object's despawn event;
        This method should only ever be called by a game's despawn method
        """

    # TODO: called multiple times when 2 objects move into each other at the same time?
    # TODO: needs to be passed more context?
    @abstractmethod
    def on_collision(self):
        """
        Performs the game object's collision evnet;
        This method should only ever be called when this game object is solid and moves into another 
        solid game object or another solid game object moves into it
        """

    # TODO: add on_command event?
