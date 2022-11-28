import unittest

from ascii_renderer import Sprite

from ascii_game_api import Room, GameObject, DuplicateGameObjectError, World


class GOA(GameObject):
    def on_spawn(self):
        return True

    def on_despawn(self):
        return True


class GOB(GameObject):
    def on_spawn(self):
        return True

    def on_despawn(self):
        return True


class GOC(GameObject):
    def on_spawn(self):
        return True

    def on_despawn(self):
        return True


class GOD(GameObject):
    def on_spawn(self):
        return True

    def on_despawn(self):
        return True


class TestRoom(unittest.TestCase):
    XA = 0
    YA = 0

    XB = 4
    YB = 19

    XC = -9
    YC = -1

    XD = 97
    YD = 24

    sprite_a: Sprite
    sprite_b: Sprite
    sprite_c: Sprite
    sprite_d: Sprite

    goa: GOA
    gob: GOB
    goc: GOC
    god: GOD

    empty_room: Room
    populated_room: Room

    empty_world: World
    populated_world: World

    def setUp(self) -> None:
        self.sprite_a = Sprite('a')
        self.sprite_b = Sprite('b')
        self.sprite_c = Sprite('c')
        self.sprite_d = Sprite('d')

        self.goa = GOA(self.sprite_a, self.XA, self.YA)
        self.gob = GOB(self.sprite_b, self.XB, self.YB)
        self.goc = GOC(self.sprite_c, self.XC, self.YC)
        self.god = GOD(self.sprite_d, self.XD, self.YD)

        self.populated_room = Room((self.goa, self.gob, self.goc))
        self.empty_room = Room()

        self.populated_world = World(self.populated_room)
        self.empty_world = World(self.empty_room)

    def test_init(self):
        self.assertEqual(3, self.populated_world.num_game_objects())
        self.assertTrue(self.goa in self.populated_world)
        self.assertTrue(self.gob in self.populated_world)
        self.assertTrue(self.goc in self.populated_world)

        self.assertFalse(self.god in self.populated_world)

        self.assertEqual(0, self.empty_world.num_game_objects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        self.assertEqual(self.empty_room, self.empty_world.room)
        self.assertEqual(self.populated_room, self.populated_world.room)

    def test_spawn(self):
        def assert_spawn(game_object: GameObject,
                         num_entities: int,
                         contains_a: bool,
                         contains_b: bool,
                         contains_c: bool,
                         contains_d: bool):
            self.empty_world.spawn(game_object)
            self.assertEqual(num_entities, self.empty_world.num_game_objects())
            self.assertEqual(contains_a, self.goa in self.empty_world)
            self.assertEqual(contains_b, self.gob in self.empty_world)
            self.assertEqual(contains_c, self.goc in self.empty_world)
            self.assertEqual(contains_d, self.god in self.empty_world)

        def assert_fail(game_object: GameObject,
                        num_entities: int,
                        contains_a: bool,
                        contains_b: bool,
                        contains_c: bool,
                        contains_d: bool):
            try:
                self.empty_world.spawn(game_object)
                self.fail()
            except DuplicateGameObjectError:
                self.assertEqual(num_entities, self.empty_world.num_game_objects())
                self.assertEqual(contains_a, self.goa in self.empty_world)
                self.assertEqual(contains_b, self.gob in self.empty_world)
                self.assertEqual(contains_c, self.goc in self.empty_world)
                self.assertEqual(contains_d, self.god in self.empty_world)

        assert_spawn(self.goa,
                     1,
                     True,
                     False,
                     False,
                     False)

        assert_fail(self.goa,
                    1,
                    True,
                    False,
                    False,
                    False)

        assert_spawn(self.goc,
                     2,
                     True,
                     False,
                     True,
                     False)

        assert_fail(self.goc,
                    2,
                    True,
                    False,
                    True,
                    False)

        assert_fail(self.goa,
                    2,
                    True,
                    False,
                    True,
                    False)

        assert_spawn(self.gob,
                     3,
                     True,
                     True,
                     True,
                     False)

        assert_fail(self.goa,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_fail(self.gob,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_fail(self.goc,
                    3,
                    True,
                    True,
                    True,
                    False)

        assert_spawn(self.god,
                     4,
                     True,
                     True,
                     True,
                     True)

        assert_fail(self.goa,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.gob,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.goc,
                    4,
                    True,
                    True,
                    True,
                    True)

        assert_fail(self.god,
                    4,
                    True,
                    True,
                    True,
                    True)

    def test_despawn(self):
        def assert_despawn(game_object: GameObject,
                           num_entities: int,
                           contains_a: bool,
                           contains_b: bool,
                           contains_c: bool,
                           contains_d: bool):
            self.empty_world.despawn(game_object)
            self.assertEqual(num_entities, self.empty_world.num_game_objects())
            self.assertEqual(contains_a, self.goa in self.empty_world)
            self.assertEqual(contains_b, self.gob in self.empty_world)
            self.assertEqual(contains_c, self.goc in self.empty_world)
            self.assertEqual(contains_d, self.god in self.empty_world)

        def assert_fail(game_object: GameObject,
                        num_entities: int,
                        contains_a: bool,
                        contains_b: bool,
                        contains_c: bool,
                        contains_d: bool):
            try:
                self.empty_world.despawn(game_object)
                self.fail()
            except ValueError:
                self.assertEqual(num_entities, self.empty_world.num_game_objects())
                self.assertEqual(contains_a, self.goa in self.empty_world)
                self.assertEqual(contains_b, self.gob in self.empty_world)
                self.assertEqual(contains_c, self.goc in self.empty_world)
                self.assertEqual(contains_d, self.god in self.empty_world)

        assert_fail(self.goa,
                    0,
                    False,
                    False,
                    False,
                    False)

        self.empty_world.spawn(self.goa)
        assert_despawn(self.goa,
                       0,
                       False,
                       False,
                       False,
                       False)

        assert_fail(self.goa,
                    0,
                    False,
                    False,
                    False,
                    False)

        self.empty_world.spawn(self.gob)
        self.empty_world.spawn(self.goc)
        assert_despawn(self.gob,
                       1,
                       False,
                       False,
                       True,
                       False)

        assert_fail(self.goa,
                    1,
                    False,
                    False,
                    True,
                    False)

        assert_fail(self.gob,
                    1,
                    False,
                    False,
                    True,
                    False)

        self.empty_world.spawn(self.goa)
        self.empty_world.spawn(self.gob)
        self.empty_world.spawn(self.god)
        assert_despawn(self.goa,
                       3,
                       False,
                       True,
                       True,
                       True)

        assert_fail(self.goa,
                    3,
                    False,
                    True,
                    True,
                    True)

        assert_despawn(self.goc,
                       2,
                       False,
                       True,
                       False,
                       True)

        assert_fail(self.goa,
                    2,
                    False,
                    True,
                    False,
                    True)

        assert_fail(self.goc,
                    2,
                    False,
                    True,
                    False,
                    True)

        assert_despawn(self.gob,
                       1,
                       False,
                       False,
                       False,
                       True)

        assert_fail(self.goa,
                    1,
                    False,
                    False,
                    False,
                    True)

        assert_fail(self.gob,
                    1,
                    False,
                    False,
                    False,
                    True)

        assert_fail(self.goc,
                    1,
                    False,
                    False,
                    False,
                    True)

        assert_despawn(self.god,
                       0,
                       False,
                       False,
                       False,
                       False)

        assert_fail(self.goa,
                    0,
                    False,
                    False,
                    False,
                    False)

        assert_fail(self.gob,
                    0,
                    False,
                    False,
                    False,
                    False)

        assert_fail(self.goc,
                    0,
                    False,
                    False,
                    False,
                    False)

        assert_fail(self.god,
                    0,
                    False,
                    False,
                    False,
                    False)

    def test_get(self):
        def assert_get(expected_entity: GameObject, index: int):
            self.assertEqual(expected_entity.__dict__, self.empty_world.get_game_object(index).__dict__)

        def assert_fail(lowest_fail_index: int):
            def fail(index):
                try:
                    self.empty_world.get_game_object(index)
                    self.fail()
                except IndexError:
                    pass

            fail(81)
            fail(11)
            fail(7)
            fail(6)
            fail(5)
            fail(4)

            for i in range(lowest_fail_index, 4):
                fail(i)

            for i in range(-5, (lowest_fail_index + 1) * -1):
                fail(i)

            fail(-6)
            fail(-17)
            fail(-23)

        assert_fail(0)

        self.empty_world.spawn(self.gob)
        assert_get(self.gob, 0)
        assert_fail(1)

        self.empty_world.despawn(self.gob)
        assert_fail(0)

        self.empty_world.spawn(self.goc)
        self.empty_world.spawn(self.god)
        assert_get(self.god, 1)
        assert_get(self.goc, 0)
        assert_fail(2)

        self.empty_world.despawn(self.goc)
        assert_get(self.god, 0)
        assert_fail(1)

        self.empty_world.spawn(self.goa)
        self.empty_world.spawn(self.gob)
        self.empty_world.spawn(self.goc)
        assert_get(self.god, 0)
        assert_get(self.goa, 1)
        assert_get(self.gob, 2)
        assert_get(self.goc, 3)
        assert_fail(4)

        self.empty_world.despawn(self.gob)
        assert_get(self.god, 0)
        assert_get(self.goa, 1)
        assert_get(self.goc, 2)
        assert_fail(3)

        self.empty_world.despawn(self.god)
        assert_get(self.goa, 0)
        assert_get(self.goc, 1)
        assert_fail(2)

        self.empty_world.despawn(self.goa)
        assert_get(self.goc, 0)
        assert_fail(1)

        self.empty_world.spawn(self.goa)
        assert_get(self.goa, 1)
        assert_get(self.goc, 0)
        assert_fail(2)

        self.empty_world.despawn(self.goc)
        assert_get(self.goa, 0)
        assert_fail(1)

        self.empty_world.despawn(self.goa)
        assert_fail(0)

    def test_iteration(self):
        for _ in self.empty_world:
            self.fail()

        game_objects = []

        for game_object in self.populated_world:
            game_objects.append(game_object)

        self.assertEqual(3, len(game_objects))
        self.assertEqual(self.goa, game_objects[0])
        self.assertEqual(self.gob, game_objects[1])
        self.assertEqual(self.goc, game_objects[2])

    def test_goto_room(self):
        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(3, self.empty_world.num_game_objects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(3, self.empty_world.num_game_objects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        self.empty_world.spawn(self.god)

        self.empty_world.goto_room(self.empty_room)
        self.assertFalse(0, self.empty_world.num_game_objects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        gox = GOA(Sprite('x'), 88, 2)
        self.empty_world.spawn(gox)

        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(4, self.empty_world.num_game_objects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertTrue(self.god in self.empty_world)
        self.assertFalse(gox in self.empty_world)

        self.empty_world.goto_room(self.empty_room)
        self.assertEqual(1, self.empty_world.num_game_objects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)
        self.assertTrue(gox in self.empty_world)


if __name__ == '__main__':
    unittest.main()
