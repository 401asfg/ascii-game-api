import unittest

from ascii_renderer import Sprite

from ascii_game_api import GameObject


class MockGameObject(GameObject):
    def __init__(self, sprite: Sprite, x: int, y: int, depth: int = 0):
        super().__init__(sprite, x, y, depth)

    def on_spawn(self):
        ...

    def on_despawn(self):
        ...


class TestGameObject(unittest.TestCase):
    CHAR_A = 'a'
    XA = 0
    YA = 0
    DEPTH_A = 0
    IS_SOLID_A = False

    CHAR_B = 'b'
    XB = 23
    YB = 7
    DEPTH_B = 11
    IS_SOLID_B = False

    CHAR_C = 'c'
    XC = -1
    YC = -98
    DEPTH_C = -100
    IS_SOLID_C = True

    sprite_a: Sprite
    sprite_b: Sprite
    sprite_c: Sprite

    gameobject_a: MockGameObject
    gameobject_b: MockGameObject
    gameobject_c: MockGameObject

    def setUp(self) -> None:
        self.sprite_a = Sprite(self.CHAR_A)
        self.sprite_b = Sprite(self.CHAR_B)
        self.sprite_c = Sprite(self.CHAR_C)

        self.gameobject_a = MockGameObject(
            self.sprite_a, self.XA, self.YA, self.DEPTH_A, self.IS_SOLID_A)
        self.gameobject_b = MockGameObject(
            self.sprite_b, self.XB, self.YB, self.DEPTH_B, self.IS_SOLID_B)
        self.gameobject_c = MockGameObject(
            self.sprite_c, self.XC, self.YC, self.DEPTH_C, self.IS_SOLID_C)

    def test_init(self):
        def assert_init(sprite, x, y, depth, is_solid, gameobject):
            self.assertEqual(sprite, gameobject.sprite)
            self.assertEqual(x, gameobject.x)
            self.assertEqual(y, gameobject.y)
            self.assertEqual(depth, gameobject.depth)
            self.assertEqual(is_solid, gameobject.is_solid)

        assert_init(self.sprite_a, self.XA, self.YA,
                    self.DEPTH_A, self.IS_SOLID_A, self.gameobject_a)
        assert_init(self.sprite_b, self.XB, self.YB,
                    self.DEPTH_B, self.IS_SOLID_B, self.gameobject_b)
        assert_init(self.sprite_c, self.XC, self.YC,
                    self.DEPTH_C, self.IS_SOLID_C, self.gameobject_c)


if __name__ == '__main__':
    unittest.main()
