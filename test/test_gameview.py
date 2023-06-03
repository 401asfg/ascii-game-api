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
    gameobject_n: GameObject
    gameobject_o: GameObject
    gameobject_p: GameObject
    gameobject_q: GameObject
    gameobject_r: GameObject
    gameobject_s: GameObject
    gameobject_t: GameObject
    gameobject_u: GameObject
    gameobject_v: GameObject
    gameobject_w: GameObject
    gameobject_x: GameObject
    gameobject_y: GameObject
    gameobject_z: GameObject
    gameobject_aa: GameObject
    gameobject_ab: GameObject
    gameobject_ac: GameObject
    gameobject_ad: GameObject
    gameobject_ae: GameObject
    gameobject_af: GameObject
    gameobject_ag: GameObject
    gameobject_ah: GameObject
    gameobject_ai: GameObject

    game: Game
    hud: Screen
    gameview: GameView

    def setUp(self) -> None:
        # TODO: design game and hud layouts in comments, then make objects to reflect them

        """
        P: all pos depth
        N: all neg depth
        O: one object
        M: mixed sign depth
        Z: one has zero depth
        """

        """ Game
        0123456789ABCDEFGHIJ

        PNO................. 0
        MZ............PN.... 1
        ..MZP............O.. 2
        ...NO..........MZ... 3
        .................... 4
        .................... 5
        .................... 6
        ..MPNOZ......PN..... 7
        .............ZO..... 8
        ..............M....Z 9
        ...................N A
        ...................O B
        ..................PM C
        .................... D
        ........PMZON....... E
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

        # TODO: test same sprite overlapping
        # TODO: test different sprite overlapping
        # TODO: test sprite empty overlapping solid sprite
        # TODO: test solid overlapping empty sprite

        # TODO: test hud same sprite overlapping
        # TODO: test hud different sprite overlapping
        # TODO: test hud solid overlapping empty sprite
        # TODO: test hud with sprite empty overlapping solid sprite
        # TODO: test hud with sprite empty overlapping empty sprite

        # TODO: test view goes out of game pos x
        # TODO: test view goes out of game pos y
        # TODO: test view goes out of game pos x and y
        # TODO: test view goes out of game neg x
        # TODO: test view goes out of game neg y
        # TODO: test view goes out of game neg x and y
        # TODO: test view goes out of game pos x and neg y
        # TODO: test view goes out of game neg x and pos y

        # TODO: test game goes out of view pos x
        # TODO: test game goes out of view pos y
        # TODO: test game goes out of view pos x and y
        # TODO: test game goes out of view neg x
        # TODO: test game goes out of view neg y
        # TODO: test game goes out of view neg x and y
        # TODO: test game goes out of view pos x and neg y
        # TODO: test game goes out of view neg x and pos y
        # TODO: test entire game in view

        # TODO: test 0x0 hud
        # TODO: test small hud
        # TODO: test large hud

        # TODO: test hud with border
        # TODO: test hud with image in middle
        # TODO: test hud with border and image in middle

        self.gameobject_a = MockGameObject(self.sprite_a, 0, 0, 10)
        self.gameobject_b = MockGameObject(self.sprite_b, 1, 0, 10)
        self.gameobject_c = MockGameObject(self.sprite_c, 2, 0, 10)
        self.gameobject_d = MockGameObject(self.sprite_d, 0, 1, 10)
        self.gameobject_e = MockGameObject(self.sprite_e, 1, 1, 10)
        self.gameobject_f = MockGameObject(self.sprite_f, 14, 1, 10)
        self.gameobject_g = MockGameObject(self.sprite_g, 15, 1, 10)
        self.gameobject_h = MockGameObject(self.sprite_h, 2, 2, 10)
        self.gameobject_i = MockGameObject(self.sprite_i, 3, 2, 10)
        self.gameobject_j = MockGameObject(self.sprite_j, 4, 2, 10)
        self.gameobject_k = MockGameObject(self.sprite_k, 17, 2, 10)
        self.gameobject_l = MockGameObject(self.sprite_l, 3, 3, 10)
        self.gameobject_m = MockGameObject(self.sprite_m, 4, 3, 10)
        self.gameobject_n = MockGameObject(self.sprite_m, 15, 3, 10)
        self.gameobject_o = MockGameObject(self.sprite_l, 16, 3, 10)
        self.gameobject_p = MockGameObject(self.sprite_k, 2, 7, 10)
        self.gameobject_q = MockGameObject(self.sprite_j, 3, 7, 10)
        self.gameobject_r = MockGameObject(self.sprite_i, 4, 7, 10)
        self.gameobject_s = MockGameObject(self.sprite_h, 5, 7, 10)
        self.gameobject_t = MockGameObject(self.sprite_g, 6, 7, 10)
        self.gameobject_u = MockGameObject(self.sprite_f, 13, 7, 10)
        self.gameobject_v = MockGameObject(self.sprite_e, 14, 7, 10)
        self.gameobject_w = MockGameObject(self.sprite_d, 13, 8, 10)
        self.gameobject_x = MockGameObject(self.sprite_c, 14, 8, 10)
        self.gameobject_y = MockGameObject(self.sprite_b, 14, 9, 10)
        self.gameobject_z = MockGameObject(self.sprite_b, 19, 9, 10)
        self.gameobject_aa = MockGameObject(self.sprite_a, 19, 10, 10)
        self.gameobject_ab = MockGameObject(self.sprite_b, 19, 11, 10)
        self.gameobject_ac = MockGameObject(self.sprite_c, 18, 12, 10)
        self.gameobject_ad = MockGameObject(self.sprite_d, 19, 12, 10)
        self.gameobject_ae = MockGameObject(self.sprite_e, 8, 14, 10)
        self.gameobject_af = MockGameObject(self.sprite_f, 9, 14, 10)
        self.gameobject_ag = MockGameObject(self.sprite_g, 10, 14, 10)
        self.gameobject_ah = MockGameObject(self.sprite_h, 11, 14, 10)
        self.gameobject_ai = MockGameObject(self.sprite_i, 12, 14, 10)

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
                          self.gameobject_m,
                          self.gameobject_n,
                          self.gameobject_o,
                          self.gameobject_p,
                          self.gameobject_q,
                          self.gameobject_r,
                          self.gameobject_s,
                          self.gameobject_t,
                          self.gameobject_u,
                          self.gameobject_v,
                          self.gameobject_w,
                          self.gameobject_x,
                          self.gameobject_y,
                          self.gameobject_z,
                          self.gameobject_aa,
                          self.gameobject_ab,
                          self.gameobject_ac,
                          self.gameobject_ad,
                          self.gameobject_ae,
                          self.gameobject_af,
                          self.gameobject_ag,
                          self.gameobject_ah,
                          self.gameobject_ai))

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
