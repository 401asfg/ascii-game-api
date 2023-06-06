from abc import ABC, abstractmethod
from typing import Tuple

from ascii_game_api.gameobject import GameObject


# TODO: create save system
# TODO: x and y values as keys?
# TODO: rewrite code that iterates over a game that has a spatial requirement iterate over coordinates instead of every gameobject
# TODO: use generic type bound by game object?


class DuplicateGameObjectError(Exception):
    """
    An error that is thrown when a game object instance is spawned within a game that already 
    contains that same game object instance
    """


class Game(ABC):
    """
    A game that can have objects spawned within it
    """

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> GameObject:
        """
        :return: The next game object in the game, if there is a next game object
        :raise StopIteration: If there is not a next game object in the game
        """
        if self._index >= self.num_gameobjects():
            raise StopIteration

        gameobject = self.get_gameobject(self._index)
        self._index += 1
        return gameobject

    @abstractmethod
    def spawn(self, gameobject: GameObject):
        """
        Spawns the given gameobject in the game; Triggers the given game_object's on_spawn event

        :param gameobject: The game object to spawn
        :raise DuplicateGameObjectError: If the given gameobject instance is already in the game
        """

    @abstractmethod
    def despawn(self, gameobject: GameObject):
        """
        Despawns the given gameobject in the game; Triggers the given game_object's on_despawn event

        :param gameobject: The game object to despawn
        :raise ValueError: If the given gameobject instance is not in the game
        """

    @abstractmethod
    def get_gameobject(self, index: int) -> GameObject:
        """
        :param index: The index of the game object to get
        :return: The game object at the given index in the game

        :raise IndexError: If the given index is less than 0, or greater than or equal to num_gameobjects()
        """

    @abstractmethod
    def get_gameobjects(self, x: int, y: int) -> Tuple[GameObject, ...]:
        """
        :param x: The x coordinate to get the game objects from
        :param y: The y coordinate to get the game objects from
        :return: The game objects at the given x, y coordinate pair in this game
        """

    @abstractmethod
    def num_gameobjects(self) -> int:
        """
        :return: The number of game objects in the game
        """

    @abstractmethod
    def __contains__(self, gameobject: GameObject) -> bool:
        """
        :param gameobject: The game object to check the game for
        :return: True if the given game object is in the game; otherwise, False
        """

    @abstractmethod
    def check_collision(self, x: int, y: int):
        """
        Triggers the collision events of all solid game objects at the given coordinates, if there is more 
        than one solid game object there

        :param x: The x coordinate to check for a collision at
        :param y: The y coordinate to check for a collision at
        """
