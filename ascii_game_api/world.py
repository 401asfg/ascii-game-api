from ascii_game_api.game import Game
from ascii_game_api.game_object import GameObject
from ascii_game_api.room import Room


# TODO: allow some game objects to be persistent


class World(Game):
    """
    A world that can spawn game objects within its current room
    """

    _room: Room

    def __init__(self, starting_room: Room):
        """
        Initializes the class
        
        :param starting_room: The room that the world starts at
        """
        self._room = starting_room

    def spawn(self, game_object: GameObject):
        self.room.spawn(game_object)

    def despawn(self, game_object: GameObject):
        self.room.despawn(game_object)

    def get_game_object(self, index: int) -> GameObject:
        return self.room.get_game_object(index)

    def num_game_objects(self) -> int:
        return self.room.num_game_objects()

    def __contains__(self, game_object: GameObject) -> bool:
        return game_object in self.room

    def __iter__(self):
        return iter(self.room)

    def __next__(self) -> GameObject:
        return next(self.room)

    def goto_room(self, room: Room):
        """
        Change the world's current room to the given room

        :param room: The room to go to
        """
        self._room = room

    @property
    def room(self) -> Room:
        return self._room
