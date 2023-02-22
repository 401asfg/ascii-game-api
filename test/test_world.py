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
    god_two: GOD

    empty_room: Room
    populated_room: Room

    empty_world: World
    populated_world: World

    empty_world_with_persistent: World
    populated_world_with_persistent: World

    def setUp(self) -> None:
        self.sprite_a = Sprite('a')
        self.sprite_b = Sprite('b')
        self.sprite_c = Sprite('c')
        self.sprite_d = Sprite('d')

        self.goa = GOA(self.sprite_a, self.XA, self.YA)
        self.gob = GOB(self.sprite_b, self.XB, self.YB)
        self.goc = GOC(self.sprite_c, self.XC, self.YC)
        self.god = GOD(self.sprite_d, self.XD, self.YD)
        self.god_two = GOD(self.sprite_d, self.XD, self.YD)

        self.populated_room = Room((self.goa, self.gob, self.goc))
        self.empty_room = Room()

        self.populated_world = World(self.populated_room)
        self.empty_world = World(self.empty_room)

        self.populated_world_with_only_persistent = World(self.empty_room, (self.god, self.gob, self.goa))
        self.populated_world_with_persistent = World(self.populated_room, (self.god,))

    def test_init(self):
        self.assertEqual(3, self.populated_world.num_gameobjects())
        self.assertTrue(self.goa in self.populated_world)
        self.assertTrue(self.gob in self.populated_world)
        self.assertTrue(self.goc in self.populated_world)
        self.assertFalse(self.god in self.populated_world)
        self.assertFalse(self.god_two in self.populated_world)

        self.assertEqual(0, self.empty_world.num_gameobjects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)
        self.assertFalse(self.god_two in self.empty_world)

        self.assertEqual(3, self.populated_world_with_only_persistent.num_gameobjects())
        self.assertTrue(self.god in self.populated_world_with_only_persistent)
        self.assertTrue(self.gob in self.populated_world_with_only_persistent)
        self.assertTrue(self.goa in self.populated_world_with_only_persistent)
        self.assertFalse(self.goc in self.populated_world_with_only_persistent)
        self.assertFalse(self.god_two in self.populated_world_with_only_persistent)

        self.assertEqual(4, self.populated_world_with_persistent.num_gameobjects())
        self.assertTrue(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.gob in self.populated_world_with_persistent)
        self.assertTrue(self.goa in self.populated_world_with_persistent)
        self.assertTrue(self.goc in self.populated_world_with_persistent)
        self.assertFalse(self.god_two in self.populated_world_with_persistent)

        def assert_fail(room_gameobjects, persistent_gameobjects):
            try:
                World(Room(room_gameobjects), persistent_gameobjects)
                self.fail()
            except DuplicateGameObjectError:
                pass

        assert_fail((self.goa, self.gob),
                    (self.goa, self.god))

        assert_fail((self.goa, self.gob),
                    (self.goc, self.gob))

        assert_fail((self.goa, self.gob),
                    (self.god, self.goc, self.god))

        assert_fail((self.goa, self.gob),
                    (self.god, self.goc, self.god, self.goa))

    def test_spawn(self):
        def assert_spawn(gameobject: GameObject,
                         num_entities: int,
                         contains_a: bool,
                         contains_b: bool,
                         contains_c: bool,
                         contains_d: bool):
            self.empty_world.spawn(gameobject)
            self.assertEqual(num_entities, self.empty_world.num_gameobjects())
            self.assertEqual(contains_a, self.goa in self.empty_world)
            self.assertEqual(contains_b, self.gob in self.empty_world)
            self.assertEqual(contains_c, self.goc in self.empty_world)
            self.assertEqual(contains_d, self.god in self.empty_world)

        def assert_fail(gameobject: GameObject,
                        num_entities: int,
                        contains_a: bool,
                        contains_b: bool,
                        contains_c: bool,
                        contains_d: bool):
            try:
                self.empty_world.spawn(gameobject)
                self.fail()
            except DuplicateGameObjectError:
                self.assertEqual(num_entities, self.empty_world.num_gameobjects())
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

    def assert_spawn_pass(self,
                          world: World,
                          gameobject: GameObject,
                          persistent: bool,
                          num_entities: int,
                          contains_a: bool,
                          contains_b: bool,
                          contains_c: bool,
                          contains_d: bool,
                          contains_d_two: bool):
        world.spawn(gameobject, persistent)
        self.assertEqual(num_entities, world.num_gameobjects())
        self.assertEqual(contains_a, self.goa in world)
        self.assertEqual(contains_b, self.gob in world)
        self.assertEqual(contains_c, self.goc in world)
        self.assertEqual(contains_d, self.god in world)
        self.assertEqual(contains_d_two, self.god_two in world)

    def assert_spawn_fail(self,
                          world: World,
                          gameobject: GameObject,
                          persistent: bool,
                          num_entities: int,
                          contains_a: bool,
                          contains_b: bool,
                          contains_c: bool,
                          contains_d: bool,
                          contains_d_two: bool):
        try:
            world.spawn(gameobject, persistent)
            self.fail()
        except DuplicateGameObjectError:
            self.assertEqual(num_entities, world.num_gameobjects())
            self.assertEqual(contains_a, self.goa in world)
            self.assertEqual(contains_b, self.gob in world)
            self.assertEqual(contains_c, self.goc in world)
            self.assertEqual(contains_d, self.god in world)
            self.assertEqual(contains_d_two, self.god_two in world)

    def test_empty_world_persistent_spawn(self):
        self.assert_spawn_pass(self.empty_world, self.goa, True, 1, True, False, False, False, False)
        self.assert_spawn_fail(self.empty_world, self.goa, True, 1, True, False, False, False, False)
        self.assert_spawn_fail(self.empty_world, self.goa, False, 1, True, False, False, False, False)
        self.assert_spawn_pass(self.empty_world, self.gob, False, 2, True, True, False, False, False)
        self.assert_spawn_fail(self.empty_world, self.gob, True, 2, True, True, False, False, False)
        self.assert_spawn_pass(self.empty_world, self.goc, True, 3, True, True, True, False, False)
        self.assert_spawn_fail(self.empty_world, self.goc, True, 3, True, True, True, False, False)
        self.assert_spawn_fail(self.empty_world, self.goc, False, 3, True, True, True, False, False)
        self.assert_spawn_pass(self.empty_world, self.god, False, 4, True, True, True, True, False)

    def test_contains_only_persistent_with_persistent_spawn(self):
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goa, True, 3, True, True, False, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goa, False, 3, True, True, False, True, False)
        self.assert_spawn_pass(self.populated_world_with_only_persistent, self.goc, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goc, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goc, False, 4, True, True, True, True, False)
        self.assert_spawn_pass(self.populated_world_with_only_persistent, self.god_two, False, 5, True, True, True, True, True)

    def test_contains_only_persistent_with_non_persistent_spawn(self):
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goa, True, 3, True, True, False, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goa, False, 3, True, True, False, True, False)
        self.assert_spawn_pass(self.populated_world_with_only_persistent, self.goc, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goc, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_only_persistent, self.goc, False, 4, True, True, True, True, False)
        self.assert_spawn_pass(self.populated_world_with_only_persistent, self.god_two, False, 5, True, True, True, True, True)

    def test_contains_only_non_persistent_with_persistent_spawn(self):
        self.assert_spawn_fail(self.populated_world, self.goa, True, 3, True, True, True, False, False)
        self.assert_spawn_fail(self.populated_world, self.gob, True, 3, True, True, True, False, False)
        self.assert_spawn_fail(self.populated_world, self.goc, True, 3, True, True, True, False, False)
        self.assert_spawn_pass(self.populated_world, self.god, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world, self.god, False, 4, True, True, True, True, False)

    def test_contains_persistent_with_persistent_spawn(self):
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, False, 4, True, True, True, True, False)
        self.assert_spawn_pass(self.populated_world_with_persistent, self.god_two, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god_two, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god_two, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, False, 5, True, True, True, True, True)

    def test_contains_persistent_with_non_persistent_spawn(self):
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, True, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, False, 4, True, True, True, True, False)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, False, 4, True, True, True, True, False)
        self.assert_spawn_pass(self.populated_world_with_persistent, self.god_two, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god_two, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god_two, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, True, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goa, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.gob, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.goc, False, 5, True, True, True, True, True)
        self.assert_spawn_fail(self.populated_world_with_persistent, self.god, False, 5, True, True, True, True, True)

    def test_despawn(self):
        def assert_despawn(gameobject: GameObject,
                           num_entities: int,
                           contains_a: bool,
                           contains_b: bool,
                           contains_c: bool,
                           contains_d: bool):
            self.empty_world.despawn(gameobject)
            self.assertEqual(num_entities, self.empty_world.num_gameobjects())
            self.assertEqual(contains_a, self.goa in self.empty_world)
            self.assertEqual(contains_b, self.gob in self.empty_world)
            self.assertEqual(contains_c, self.goc in self.empty_world)
            self.assertEqual(contains_d, self.god in self.empty_world)

        def assert_fail(gameobject: GameObject,
                        num_entities: int,
                        contains_a: bool,
                        contains_b: bool,
                        contains_c: bool,
                        contains_d: bool):
            try:
                self.empty_world.despawn(gameobject)
                self.fail()
            except ValueError:
                self.assertEqual(num_entities, self.empty_world.num_gameobjects())
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

        assert_fail(self.goa,
                    0,
                    False,
                    False,
                    False,
                    False)

        self.empty_world.spawn(self.goa, True)
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
        self.empty_world.spawn(self.goc, True)
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
        self.empty_world.spawn(self.gob, True)
        self.empty_world.spawn(self.god, True)
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
            self.assertEqual(expected_entity.__dict__, self.empty_world.get_gameobject(index).__dict__)

        def assert_fail(lowest_fail_index: int):
            def fail(index):
                try:
                    self.empty_world.get_gameobject(index)
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

        assert_fail(0)

        self.empty_world.spawn(self.gob)
        assert_get(self.gob, 0)
        assert_fail(1)

        self.empty_world.despawn(self.gob)
        assert_fail(0)

        self.empty_world.spawn(self.goc, True)
        self.empty_world.spawn(self.god, True)
        assert_get(self.god, 1)
        assert_get(self.goc, 0)
        assert_fail(2)

        self.empty_world.despawn(self.goc)
        assert_get(self.god, 0)
        assert_fail(1)

        self.empty_world.despawn(self.god)
        assert_fail(0)

        self.empty_world.spawn(self.goc)
        self.empty_world.spawn(self.god, True)
        assert_get(self.god, 0)
        assert_get(self.goc, 1)
        assert_fail(2)

        self.empty_world.despawn(self.goc)
        assert_get(self.god, 0)
        assert_fail(1)

        self.empty_world.spawn(self.goa)
        self.empty_world.spawn(self.gob, True)
        self.empty_world.spawn(self.goc)
        assert_get(self.god, 0)
        assert_get(self.goa, 2)
        assert_get(self.gob, 1)
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

        self.empty_world.spawn(self.goa, True)
        assert_get(self.goa, 0)
        assert_get(self.goc, 1)
        assert_fail(2)

        self.empty_world.despawn(self.goc)
        assert_get(self.goa, 0)
        assert_fail(1)

        self.empty_world.despawn(self.goa)
        assert_fail(0)

        self.empty_world.spawn(self.gob)
        assert_get(self.gob, 0)
        assert_fail(1)

        self.empty_world.spawn(self.goc, True)
        assert_get(self.goc, 0)
        assert_get(self.gob, 1)
        assert_fail(2)

        self.empty_world.spawn(self.god)
        assert_get(self.goc, 0)
        assert_get(self.gob, 1)
        assert_get(self.god, 2)
        assert_fail(3)

        self.empty_world.spawn(self.goa, True)
        assert_get(self.goc, 0)
        assert_get(self.goa, 1)
        assert_get(self.gob, 2)
        assert_get(self.god, 3)
        assert_fail(4)

        self.empty_world.despawn(self.goc)
        assert_get(self.goa, 0)
        assert_get(self.gob, 1)
        assert_get(self.god, 2)
        assert_fail(3)

        self.empty_world.spawn(self.goc)
        assert_get(self.goa, 0)
        assert_get(self.gob, 1)
        assert_get(self.god, 2)
        assert_get(self.goc, 3)
        assert_fail(4)

        self.empty_world.despawn(self.goc)
        assert_get(self.goa, 0)
        assert_get(self.gob, 1)
        assert_get(self.god, 2)
        assert_fail(3)

        self.empty_world.spawn(self.goc, True)
        assert_get(self.goa, 0)
        assert_get(self.goc, 1)
        assert_get(self.gob, 2)
        assert_get(self.god, 3)
        assert_fail(4)

    def test_goto_room(self):
        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(3, self.empty_world.num_gameobjects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(3, self.empty_world.num_gameobjects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        self.empty_world.spawn(self.god)

        self.empty_world.goto_room(self.empty_room)
        self.assertFalse(0, self.empty_world.num_gameobjects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)

        gox = GOA(Sprite('x'), 88, 2)
        self.empty_world.spawn(gox)

        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(4, self.empty_world.num_gameobjects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertTrue(self.god in self.empty_world)
        self.assertFalse(gox in self.empty_world)

        self.empty_world.goto_room(self.empty_room)
        self.assertEqual(1, self.empty_world.num_gameobjects())
        self.assertFalse(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)
        self.assertTrue(gox in self.empty_world)

        self.empty_world.spawn(self.goa)

        self.empty_world.goto_room(self.populated_room)
        self.assertEqual(4, self.empty_world.num_gameobjects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertTrue(self.gob in self.empty_world)
        self.assertTrue(self.goc in self.empty_world)
        self.assertTrue(self.god in self.empty_world)
        self.assertFalse(gox in self.empty_world)

        self.empty_world.goto_room(self.empty_room)
        self.assertEqual(2, self.empty_world.num_gameobjects())
        self.assertTrue(self.goa in self.empty_world)
        self.assertFalse(self.gob in self.empty_world)
        self.assertFalse(self.goc in self.empty_world)
        self.assertFalse(self.god in self.empty_world)
        self.assertTrue(gox in self.empty_world)

    def test_goto_room_persistent(self):
        self.populated_world_with_persistent.goto_room(self.empty_room)
        self.assertEqual(1, self.populated_world_with_persistent.num_gameobjects())
        self.assertFalse(self.goa in self.populated_world_with_persistent)
        self.assertFalse(self.gob in self.populated_world_with_persistent)
        self.assertFalse(self.goc in self.populated_world_with_persistent)
        self.assertTrue(self.god in self.populated_world_with_persistent)
        self.assertFalse(self.god_two in self.populated_world_with_persistent)

        self.populated_world_with_persistent.spawn(self.goa)
        self.populated_world_with_persistent.spawn(self.god_two, True)

        self.populated_world_with_persistent.goto_room(self.populated_room)
        self.assertEqual(5, self.populated_world_with_persistent.num_gameobjects())
        self.assertTrue(self.goa in self.populated_world_with_persistent)
        self.assertTrue(self.gob in self.populated_world_with_persistent)
        self.assertTrue(self.goc in self.populated_world_with_persistent)
        self.assertTrue(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.god_two in self.populated_world_with_persistent)

        self.populated_world_with_persistent.despawn(self.god)
        self.populated_world_with_persistent.despawn(self.goa)

        self.populated_world_with_persistent.goto_room(self.empty_room)
        self.assertEqual(2, self.populated_world_with_persistent.num_gameobjects())
        self.assertTrue(self.goa in self.populated_world_with_persistent)
        self.assertFalse(self.gob in self.populated_world_with_persistent)
        self.assertFalse(self.goc in self.populated_world_with_persistent)
        self.assertFalse(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.god_two in self.populated_world_with_persistent)

        self.populated_world_with_persistent.spawn(self.gob, True)

        try:
            self.populated_world_with_persistent.goto_room(self.populated_room)
            self.fail()
        except DuplicateGameObjectError:
            pass

        self.assertEqual(3, self.populated_world_with_persistent.num_gameobjects())
        self.assertTrue(self.goa in self.populated_world_with_persistent)
        self.assertTrue(self.gob in self.populated_world_with_persistent)
        self.assertFalse(self.goc in self.populated_world_with_persistent)
        self.assertFalse(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.god_two in self.populated_world_with_persistent)

        self.populated_room.despawn(self.gob)

        self.populated_world_with_persistent.goto_room(self.populated_room)
        self.assertEqual(3, self.populated_world_with_persistent.num_gameobjects())
        self.assertFalse(self.goa in self.populated_world_with_persistent)
        self.assertTrue(self.gob in self.populated_world_with_persistent)
        self.assertTrue(self.goc in self.populated_world_with_persistent)
        self.assertFalse(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.god_two in self.populated_world_with_persistent)

        self.populated_world_with_persistent.spawn(self.goa, True)
        self.populated_world_with_persistent.despawn(self.goc)
        self.populated_world_with_persistent.spawn(self.goc, True)

        try:
            self.populated_world_with_persistent.goto_room(self.empty_room)
            self.fail()
        except DuplicateGameObjectError:
            pass

        self.assertEqual(4, self.populated_world_with_persistent.num_gameobjects())
        self.assertTrue(self.goa in self.populated_world_with_persistent)
        self.assertTrue(self.gob in self.populated_world_with_persistent)
        self.assertTrue(self.goc in self.populated_world_with_persistent)
        self.assertFalse(self.god in self.populated_world_with_persistent)
        self.assertTrue(self.god_two in self.populated_world_with_persistent)


if __name__ == '__main__':
    unittest.main()
