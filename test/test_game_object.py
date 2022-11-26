import unittest

from ascii_renderer import Sprite

from ascii_game_api.game_object import GameObject


class TestGameObject(unittest.TestCase):
    def test_init(self):
        def assert_init(char, x, y):
            expected_sprite = Sprite(char)
            actual_game_object = GameObject(Sprite(char), x, y)
            
            self.assertEqual(expected_sprite, actual_game_object.sprite)
            self.assertEqual(x, actual_game_object.x)
            self.assertEqual(y, actual_game_object.y)

        assert_init('a', 0, 0)
        assert_init('b', -28, -7)
        assert_init('c', 8, 791)
        assert_init('d', 1, 1)
        assert_init('e', 38, -9)
