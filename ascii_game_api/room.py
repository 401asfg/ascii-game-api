from typing import List, Tuple
from ascii_game_api.game import Game, DuplicateGameObjectError
from ascii_game_api.game_object import GameObject


# TODO: test


class Room(Game):
    """
    A room that can have game objects spawned within it
    """

    _game_objects: List[GameObject]

    def __init__(self, game_objects: Tuple[GameObject, ...] = ()):
        """
        Initializes the class
        
        :param game_objects: A set of game objects that are spawned into the room 
        upon its creation
        """
        self._game_objects = []
        [self.spawn(game_object) for game_object in game_objects]

    def spawn(self, game_object: GameObject):
        if game_object in self:
            raise DuplicateGameObjectError

        self._game_objects.append(game_object)
        game_object.on_spawn()

    def despawn(self, game_object: GameObject):
        self._game_objects.remove(game_object)
        game_object.on_despawn()

    def get_game_object(self, index: int) -> GameObject:
        return self._game_objects[index]

    def num_game_objects(self) -> int:
        return len(self._game_objects)

    def __contains__(self, game_object: GameObject) -> bool:
        return game_object in self._game_objects

    def __iter__(self):
        self._index = 0
        return self
    
    def __next__(self) -> GameObject:
        if self._index >= self.num_game_objects():
            raise StopIteration

        game_object = self.get_game_object(self._index)
        self._index += 1
        return game_object
