from abc import ABC, abstractmethod

from ascii_game_api.gameobject import GameObject


# TODO: make abs methods not raise not impl err, and just have nothing?
# TODO: create save system


class DuplicateGameObjectError(Exception):
    """
    An error that is thrown when a game object instance is spawned within a game that already 
    contains that same game object instance
    """


class Game(ABC):
    """
    A game that can have objects spawned within it
    """

    @abstractmethod
    def spawn(self, gameobject: GameObject):
        """
        Spawns the given gameobject in the game; Triggers the given game_object's on_spawn event

        :param gameobject: The game object to spawn
        :raise DuplicateGameObjectError: If the given gameobject instance is already in the game
        """
        raise NotImplementedError

    @abstractmethod
    def despawn(self, gameobject: GameObject):
        """
        Despawns the given gameobject in the game; Triggers the given game_object's on_despawn event

        :param gameobject: The game object to despawn
        :raise ValueError: If the given gameobject instance is not in the game
        """
        raise NotImplementedError

    @abstractmethod
    def get_gameobject(self, index: int) -> GameObject:
        """
        :param index: The index of the game object to get
        :return: The game object at the given index in the game

        :raise IndexError: If the given index is less than 0, or greater than or equal to num_gameobjects()
        """
        raise NotImplementedError

    @abstractmethod
    def num_gameobjects(self) -> int:
        """
        :return: The number of game objects in the game
        """
        raise NotImplementedError

    @abstractmethod
    def __contains__(self, gameobject: GameObject) -> bool:
        """
        :param gameobject: The game object to check the game for
        :return: True if the given game object is in the game; otherwise, False
        """
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self) -> GameObject:
        """
        :return: The next game object in the game, if there is a next game object
        :raise StopIteration: If there is not a next game object in the game
        """
        raise NotImplementedError
