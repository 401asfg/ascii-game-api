import unittest

from ascii_renderer import Sprite

from ascii_game_api import Game, DuplicateGameObjectError, GameObject


class MockGame(Game):
    def __init__(self, gameobjects):
        self._gameobjects = []
        [self.spawn(gameobject) for gameobject in gameobjects]

    def spawn(self, gameobject):
        if gameobject in self:
            raise DuplicateGameObjectError

        self._gameobjects.append(gameobject)
        gameobject.on_spawn()

    def despawn(self, gameobject):
        self._gameobjects.remove(gameobject)
        gameobject.on_despawn()

    def get_gameobject(self, index):
        return self._gameobjects[index]

    def num_gameobjects(self):
        return len(self._gameobjects)

    def __contains__(self, gameobject):
        return gameobject in self._gameobjects


class MockGameObject(GameObject):
    def on_spawn(self):
        pass

    def on_despawn(self):
        pass


class TestGame(unittest.TestCase):
    gameobject_a: GameObject
    gameobject_b: GameObject
    gameobject_c: GameObject
    gameobject_d: GameObject

    empty_game: Game
    populated_game: Game

    def setUp(self) -> None:
        self.empty_game = MockGame(())

        self.gameobject_a = MockGameObject(Sprite('x'), 0, 0)
        self.gameobject_b = MockGameObject(Sprite('x'), 0, 0)
        self.gameobject_c = MockGameObject(Sprite('x'), 0, 0)
        self.gameobject_d = MockGameObject(Sprite('x'), 0, 0)

        self.populated_game = MockGame((
            self.gameobject_a,
            self.gameobject_b,
            self.gameobject_c,
            self.gameobject_d
        ))

    def test_iteration(self):
        for _ in self.empty_game:
            self.fail()

        gameobjects = []

        for gameobject in self.populated_game:
            gameobjects.append(gameobject)

        self.assertEqual(4, len(gameobjects))
        self.assertEqual(self.gameobject_a, gameobjects[0])
        self.assertEqual(self.gameobject_b, gameobjects[1])
        self.assertEqual(self.gameobject_c, gameobjects[2])
        self.assertEqual(self.gameobject_d, gameobjects[3])


if __name__ == '__main__':
    unittest.main()
