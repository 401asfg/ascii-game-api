from typing import List, Tuple
from ascii_game_api.game import Game, DuplicateGameObjectError
from ascii_game_api.gameobject import GameObject


class Room(Game):
    """
    A room that can have game objects spawned within it
    """

    _gameobjects: List[GameObject]

    def __init__(self, gameobjects: Tuple[GameObject, ...] = ()):
        """
        Initializes the class
        
        :param gameobjects: A set of game objects that are spawned into the room
        upon its creation
        """
        self._gameobjects = []
        [self.spawn(gameobject) for gameobject in gameobjects]

    def spawn(self, gameobject: GameObject):
        if gameobject in self:
            raise DuplicateGameObjectError

        self._gameobjects.append(gameobject)
        gameobject.on_spawn()

    def despawn(self, gameobject: GameObject):
        self._gameobjects.remove(gameobject)
        gameobject.on_despawn()

    def get_gameobject(self, index: int) -> GameObject:
        return self._gameobjects[index]

    def num_gameobjects(self) -> int:
        return len(self._gameobjects)

    def __contains__(self, gameobject: GameObject) -> bool:
        return gameobject in self._gameobjects

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self) -> GameObject:
        if self._index >= self.num_gameobjects():
            raise StopIteration

        gameobject = self.get_gameobject(self._index)
        self._index += 1
        return gameobject
