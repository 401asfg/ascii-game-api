from ascii_game_api.game import Game
from ascii_game_api.gameobject import GameObject
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

    def spawn(self, gameobject: GameObject):
        self.room.spawn(gameobject)

    def despawn(self, gameobject: GameObject):
        self.room.despawn(gameobject)

    def get_gameobject(self, index: int) -> GameObject:
        return self.room.get_gameobject(index)

    def num_gameobjects(self) -> int:
        return self.room.num_gameobjects()

    def __contains__(self, gameobject: GameObject) -> bool:
        return gameobject in self.room

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
