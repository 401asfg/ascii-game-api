import unittest

from ascii_renderer import Sprite, Screen

from ascii_game_api import GameObject, Game, Room, GameView


class MockGameObject(GameObject):

    def on_spawn(self):
        pass

    def on_despawn(self):
        pass


class TestGameView(unittest.TestCase):
    HUD_WIDTH = 10
    HUD_HEIGHT = 7

    GAMEVIEW_X = 0
    GAMEVIEW_Y = 0

    sprite_empty: Sprite
    sprite_a: Sprite
    sprite_b: Sprite
    sprite_c: Sprite
    sprite_d: Sprite
    sprite_e: Sprite
    sprite_f: Sprite
    sprite_g: Sprite
    sprite_h: Sprite
    sprite_i: Sprite
    sprite_j: Sprite
    sprite_k: Sprite
    sprite_l: Sprite
    sprite_m: Sprite

    gameobject_a: GameObject
    gameobject_b: GameObject
    gameobject_c: GameObject
    gameobject_d: GameObject
    gameobject_e: GameObject
    gameobject_f: GameObject
    gameobject_g: GameObject
    gameobject_h: GameObject
    gameobject_i: GameObject
    gameobject_j: GameObject
    gameobject_k: GameObject
    gameobject_l: GameObject
    gameobject_m: GameObject

    game: Game
    hud: Screen
    gameview: GameView

    def setUp(self) -> None:
        # TODO: design game and hud layouts in comments, then make objects to reflect them

        """ Game
        XXXXXXXXZXXXXXXZXXXX
        .....YY.....Y..Z....
        XXXXXXXYYXXXXXXXXXXX
        ....................
        AAAAAAAAAAAAAAAAAAAA
        BBBBBBBBBBBBBBBBBBBB
        X..................X
        Y..................Y
        Z..................Z
        Z..................X
        Z..................Y
        X..................Z
        XAAAAAAAABBAAAAAAAAX
        """

        self.sprite_empty = Sprite(' ')
        self.sprite_a = Sprite('a')
        self.sprite_b = Sprite('b')
        self.sprite_c = Sprite('c')
        self.sprite_d = Sprite('d')
        self.sprite_e = Sprite('e')
        self.sprite_f = Sprite('f')
        self.sprite_g = Sprite('g')
        self.sprite_h = Sprite('h')
        self.sprite_i = Sprite('i')
        self.sprite_j = Sprite('j')
        self.sprite_k = Sprite('k')
        self.sprite_l = Sprite('l')
        self.sprite_m = Sprite('m')

        self.gameobject_a = MockGameObject(self.sprite_a, 0, 0, 0)      # behind b
        self.gameobject_b = MockGameObject(self.sprite_b, 0, 0, 0)      # 0, 0
        self.gameobject_c = MockGameObject(self.sprite_c, 5, 11, 1)     # behind d
        self.gameobject_d = MockGameObject(self.sprite_d, 5, 11, -1)    # 5, 11
        self.gameobject_e = MockGameObject(self.sprite_e, -27, 9, -11)  # -27, 9
        self.gameobject_f = MockGameObject(self.sprite_f, -27, 9, -40)  # behind f
        self.gameobject_g = MockGameObject(self.sprite_g, 59, 0, 0)     # 59, 0
        self.gameobject_h = MockGameObject(self.sprite_h, 59, 1, 0)     # 59, 1
        self.gameobject_i = MockGameObject(self.sprite_i, 1, 1, 77)     # 1, 1
        self.gameobject_j = MockGameObject(self.sprite_j, 7, -7, 0)     # behind k
        self.gameobject_k = MockGameObject(self.sprite_k, 7, -7, -2)    # 7, -7
        self.gameobject_l = MockGameObject(self.sprite_l, 7, -7, 6)     # behind k
        self.gameobject_m = MockGameObject(self.sprite_m, 9, 5, 1)      # 9, 5

        self.game = Room((self.gameobject_a,
                          self.gameobject_b,
                          self.gameobject_c,
                          self.gameobject_d,
                          self.gameobject_e,
                          self.gameobject_f,
                          self.gameobject_g,
                          self.gameobject_h,
                          self.gameobject_i,
                          self.gameobject_j,
                          self.gameobject_k,
                          self.gameobject_l,
                          self.gameobject_m))

        self.hud = Screen(self.sprite_empty, self.HUD_WIDTH, self.HUD_HEIGHT)

        self.gameview = GameView(self.game, self.hud, self.GAMEVIEW_X, self.GAMEVIEW_Y)

    def test_init(self):
        self.assertEqual(self.game, self.gameview.game)
        self.assertEqual(self.hud, self.gameview.hud)
        self.assertEqual(self.GAMEVIEW_X, self.gameview.x)
        self.assertEqual(self.GAMEVIEW_Y, self.gameview.y)

    def test_render_depth(self):

        ...     # TODO: write

    def test_render_overlay(self):
        ...     # TODO: write

    def test_render_different_empty_space_sprite(self):
        ...     # TODO: write

    def test_render_different_size(self):
        ...     # TODO: write

    def test_render_different_coordinates(self):
        ...     # TODO: write


if __name__ == '__main__':
    unittest.main()
