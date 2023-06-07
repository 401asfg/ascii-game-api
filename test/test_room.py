import unittest

from ascii_renderer import Sprite

from ascii_game_api import Room, GameObject, DuplicateGameObjectError


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

    goc_two: GOC
    goc_three: GOC

    empty_room: Room
    populated_room: Room

    def setUp(self) -> None:
        self.sprite_a = Sprite("a")
        self.sprite_b = Sprite("b")
        self.sprite_c = Sprite("c")
        self.sprite_d = Sprite("d")

        self.goa = GOA(self.sprite_a, self.XA, self.YA)
        self.gob = GOB(self.sprite_b, self.XB, self.YB)
        self.goc = GOC(self.sprite_c, self.XC, self.YC)
        self.god = GOD(self.sprite_d, self.XD, self.YD)

        self.goc_two = GOC(self.sprite_a, self.XC, self.YC)
        self.goc_three = GOC(self.sprite_b, self.XC, self.YC, depth=4)

        self.populated_room = Room((self.goa, self.gob, self.goc))
        self.empty_room = Room()

    def test_init(self):
        self.assertEqual(3, self.populated_room.num_gameobjects())
        self.assertTrue(self.goa in self.populated_room)
        self.assertTrue(self.gob in self.populated_room)
        self.assertTrue(self.goc in self.populated_room)

        self.assertFalse(self.god in self.populated_room)

        self.assertEqual(0, self.empty_room.num_gameobjects())
        self.assertFalse(self.goa in self.empty_room)
        self.assertFalse(self.gob in self.empty_room)
        self.assertFalse(self.goc in self.empty_room)
        self.assertFalse(self.god in self.empty_room)

        try:
            Room((self.goa, self.gob, self.goc, self.goa))
            self.fail()
        except DuplicateGameObjectError:
            pass

    def test_spawn(self):
        def assert_spawn(
            gameobject: GameObject,
            num_entities: int,
            contains_a: bool,
            contains_b: bool,
            contains_c: bool,
            contains_d: bool,
        ):
            self.empty_room.spawn(gameobject)
            self.assertEqual(num_entities, self.empty_room.num_gameobjects())
            self.assertEqual(contains_a, self.goa in self.empty_room)
            self.assertEqual(contains_b, self.gob in self.empty_room)
            self.assertEqual(contains_c, self.goc in self.empty_room)
            self.assertEqual(contains_d, self.god in self.empty_room)

        def assert_fail(
            gameobject: GameObject,
            num_entities: int,
            contains_a: bool,
            contains_b: bool,
            contains_c: bool,
            contains_d: bool,
        ):
            try:
                self.empty_room.spawn(gameobject)
                self.fail()
            except DuplicateGameObjectError:
                self.assertEqual(num_entities, self.empty_room.num_gameobjects())
                self.assertEqual(contains_a, self.goa in self.empty_room)
                self.assertEqual(contains_b, self.gob in self.empty_room)
                self.assertEqual(contains_c, self.goc in self.empty_room)
                self.assertEqual(contains_d, self.god in self.empty_room)

        assert_spawn(self.goa, 1, True, False, False, False)

        assert_fail(self.goa, 1, True, False, False, False)

        assert_spawn(self.goc, 2, True, False, True, False)

        assert_fail(self.goc, 2, True, False, True, False)

        assert_fail(self.goa, 2, True, False, True, False)

        assert_spawn(self.gob, 3, True, True, True, False)

        assert_fail(self.goa, 3, True, True, True, False)

        assert_fail(self.gob, 3, True, True, True, False)

        assert_fail(self.goc, 3, True, True, True, False)

        assert_spawn(self.god, 4, True, True, True, True)

        assert_fail(self.goa, 4, True, True, True, True)

        assert_fail(self.gob, 4, True, True, True, True)

        assert_fail(self.goc, 4, True, True, True, True)

        assert_fail(self.god, 4, True, True, True, True)

    def test_despawn(self):
        def assert_despawn(
            gameobject: GameObject,
            num_entities: int,
            contains_a: bool,
            contains_b: bool,
            contains_c: bool,
            contains_d: bool,
        ):
            self.empty_room.despawn(gameobject)
            self.assertEqual(num_entities, self.empty_room.num_gameobjects())
            self.assertEqual(contains_a, self.goa in self.empty_room)
            self.assertEqual(contains_b, self.gob in self.empty_room)
            self.assertEqual(contains_c, self.goc in self.empty_room)
            self.assertEqual(contains_d, self.god in self.empty_room)

        def assert_fail(
            gameobject: GameObject,
            num_entities: int,
            contains_a: bool,
            contains_b: bool,
            contains_c: bool,
            contains_d: bool,
        ):
            try:
                self.empty_room.despawn(gameobject)
                self.fail()
            except ValueError:
                self.assertEqual(num_entities, self.empty_room.num_gameobjects())
                self.assertEqual(contains_a, self.goa in self.empty_room)
                self.assertEqual(contains_b, self.gob in self.empty_room)
                self.assertEqual(contains_c, self.goc in self.empty_room)
                self.assertEqual(contains_d, self.god in self.empty_room)

        assert_fail(self.goa, 0, False, False, False, False)

        self.empty_room.spawn(self.goa)
        assert_despawn(self.goa, 0, False, False, False, False)

        assert_fail(self.goa, 0, False, False, False, False)

        self.empty_room.spawn(self.gob)
        self.empty_room.spawn(self.goc)
        assert_despawn(self.gob, 1, False, False, True, False)

        assert_fail(self.goa, 1, False, False, True, False)

        assert_fail(self.gob, 1, False, False, True, False)

        self.empty_room.spawn(self.goa)
        self.empty_room.spawn(self.gob)
        self.empty_room.spawn(self.god)
        assert_despawn(self.goa, 3, False, True, True, True)

        assert_fail(self.goa, 3, False, True, True, True)

        assert_despawn(self.goc, 2, False, True, False, True)

        assert_fail(self.goa, 2, False, True, False, True)

        assert_fail(self.goc, 2, False, True, False, True)

        assert_despawn(self.gob, 1, False, False, False, True)

        assert_fail(self.goa, 1, False, False, False, True)

        assert_fail(self.gob, 1, False, False, False, True)

        assert_fail(self.goc, 1, False, False, False, True)

        assert_despawn(self.god, 0, False, False, False, False)

        assert_fail(self.goa, 0, False, False, False, False)

        assert_fail(self.gob, 0, False, False, False, False)

        assert_fail(self.goc, 0, False, False, False, False)

        assert_fail(self.god, 0, False, False, False, False)

    def test_get_gameobject(self):
        def assert_get(expected_entity: GameObject, index: int):
            self.assertEqual(
                expected_entity.__dict__, self.empty_room.get_gameobject(index).__dict__
            )

        def assert_fail(lowest_fail_index: int):
            def fail(index):
                try:
                    self.empty_room.get_gameobject(index)
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

        self.empty_room.spawn(self.gob)
        assert_get(self.gob, 0)
        assert_fail(1)

        self.empty_room.despawn(self.gob)
        assert_fail(0)

        self.empty_room.spawn(self.goc)
        self.empty_room.spawn(self.god)
        assert_get(self.god, 1)
        assert_get(self.goc, 0)
        assert_fail(2)

        self.empty_room.despawn(self.goc)
        assert_get(self.god, 0)
        assert_fail(1)

        self.empty_room.spawn(self.goa)
        self.empty_room.spawn(self.gob)
        self.empty_room.spawn(self.goc)
        assert_get(self.god, 0)
        assert_get(self.goa, 1)
        assert_get(self.gob, 2)
        assert_get(self.goc, 3)
        assert_fail(4)

        self.empty_room.despawn(self.gob)
        assert_get(self.god, 0)
        assert_get(self.goa, 1)
        assert_get(self.goc, 2)
        assert_fail(3)

        self.empty_room.despawn(self.god)
        assert_get(self.goa, 0)
        assert_get(self.goc, 1)
        assert_fail(2)

        self.empty_room.despawn(self.goa)
        assert_get(self.goc, 0)
        assert_fail(1)

        self.empty_room.spawn(self.goa)
        assert_get(self.goa, 1)
        assert_get(self.goc, 0)
        assert_fail(2)

        self.empty_room.despawn(self.goc)
        assert_get(self.goa, 0)
        assert_fail(1)

        self.empty_room.despawn(self.goa)
        assert_fail(0)

    def test_get_gameobjects(self):
        def assert_pass(self, expected_gameobjects, room, x, y):
            self.assertEqual(expected_gameobjects, room.get_gameobjects(x, y))

        def assert_pass_for_range(
            expected_gameobjects, room, min_x, max_x, min_y, max_y
        ):
            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    assert_pass(expected_gameobjects, room, x, y)

        assert_pass_for_range((), self.empty_room, -100, 100, -100, 100)

        min_y = -100
        max_y = 100

        def assert_pass_area(expected_gameobjects, min_x, x, y):
            assert_pass_for_range((), self.populated_room, min_x, x, min_y, max_y)
            assert_pass_for_range((), self.populated_room, x, x + 1, min_y, y)
            assert_pass_for_range((), self.populated_room, x, x + 1, y + 1, max_y)
            assert_pass(expected_gameobjects, self.populated_room, x, y)

        assert_pass_area((self.goc,), -100, -9, -1)
        assert_pass_area((self.goa,), -8, 0, 0)
        assert_pass_area((self.gob,), 1, 4, 19)
        assert_pass_for_range((), self.populated_room, 5, 100, -100, 100)

        self.populated_room.spawn(self.god)

        assert_pass_area((self.goc,), -100, -9, -1)
        assert_pass_area((self.goa,), -8, 0, 0)
        assert_pass_area((self.gob,), 1, 4, 19)
        assert_pass_area((self.god,), 5, 97, 24)
        assert_pass_for_range((), self.populated_room, 98, 100, -100, 100)

        self.populated_room.despawn(self.gob)

        assert_pass_area((self.goc,), -100, -9, -1)
        assert_pass_area((self.goa,), -8, 0, 0)
        assert_pass_area((self.god,), 1, 97, 24)
        assert_pass_for_range((), self.populated_room, 98, 100, -100, 100)

        self.populated_room.spawn(self.goc_two)

        assert_pass_area((self.goc, self.goc_two), -100, -9, -1)
        assert_pass_area((self.goa,), -8, 0, 0)
        assert_pass_area((self.god,), 1, 97, 24)
        assert_pass_for_range((), self.populated_room, 98, 100, -100, 100)

        self.populated_room.spawn(self.goc_three)

        assert_pass_area((self.goc, self.goc_two, self.goc_three), -100, -9, -1)
        assert_pass_area((self.goa,), -8, 0, 0)
        assert_pass_area((self.god,), 1, 97, 24)
        assert_pass_for_range((), self.populated_room, 98, 100, -100, 100)


if __name__ == "__main__":
    unittest.main()
