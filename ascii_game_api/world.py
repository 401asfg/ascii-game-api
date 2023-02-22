from ascii_game_api.game import Game, DuplicateGameObjectError
from ascii_game_api.gameobject import GameObject
from ascii_game_api.room import Room


class World(Game):
    """
    A world that can spawn game objects within its current room
    """

    _room: Room
    _persistent_gameobjects: list[GameObject]

    def __init__(self, room: Room, persistent_gameobjects: tuple[GameObject, ...] = ()):
        """
        Initializes the class
        
        :param room: The room that the world starts at
        :param persistent_gameobjects: The persistent game objects that the world starts with; persistent game objects
        occupy the world's lowest indices

        :raise DuplicateGameObjectError: If not every gameobject instance in both the given room and
        persistent_gameobjects is unique
        """
        self._room = room
        self._persistent_gameobjects = []

        [self.spawn(persistent_gameobject, persistent=True)
         for persistent_gameobject in persistent_gameobjects]

    def spawn(self, gameobject: GameObject, persistent: bool = False):
        """
        Spawns the given gameobject in the game; Triggers the given gameobject's on_spawn event

        :param gameobject: The game object to spawn
        :param persistent: Whether the game object should be spawned as persistent; persistent game objects occupy the
        world's lowest indices
        :raise DuplicateGameObjectError: If the given gameobject instance is already in the game
        """
        if gameobject in self:
            raise DuplicateGameObjectError

        if not persistent:
            self._room.spawn(gameobject)
        else:
            self._persistent_gameobjects.append(gameobject)
            gameobject.on_spawn()   # TODO: change to a call to super if on_spawn is called by game

    def despawn(self, gameobject: GameObject):
        if gameobject in self._room:
            self._room.despawn(gameobject)
        else:
            self._persistent_gameobjects.remove(gameobject)
            gameobject.on_despawn() # TODO: change to a call to super if on_despawn is called by game

    def get_gameobject(self, index: int) -> GameObject:
        """
        Produces the game object at the given index; all the persistent game objects occupy all the lowest indexes

        :param index: The index of the game object to get
        :return: The game object at the given index in the game

        :raise IndexError: If the given index is less than 0, or greater than or equal to num_gameobjects()
        """
        num_persistent_gameobjects = len(self._persistent_gameobjects)

        if index < num_persistent_gameobjects:
            return self._persistent_gameobjects[index]

        return self._room.get_gameobject(index - num_persistent_gameobjects)

    def num_gameobjects(self) -> int:
        return self._room.num_gameobjects() + len(self._persistent_gameobjects)

    def __contains__(self, gameobject: GameObject) -> bool:
        return gameobject in self._room or gameobject in self._persistent_gameobjects

    def goto_room(self, room: Room):
        """
        Change the world's current room to the given room

        :param room: The room to go to
        :raise DuplicateGameObjectError: If any of the persistent game object instances in this world are also
        contained within the given room
        """
        for persistent_gameobject in self._persistent_gameobjects:
            if persistent_gameobject in room:
                raise DuplicateGameObjectError

        self._room = room
