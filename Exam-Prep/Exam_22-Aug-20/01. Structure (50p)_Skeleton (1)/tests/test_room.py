import unittest

from project.people.child import Child
from project.rooms.room import Room


class RoomTest(unittest.TestCase):

    def setUp(self):
        self.room = Room("NAME", 150.0, 2)

    def test_room_init(self):
        self.assertEqual("NAME", self.room.family_name)
        self.assertEqual(150.0, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertListEqual([], self.room.children)

    def test_room_calculate_expenses(self):
        self.room.children.append(Child(1, 2))
        expected = 3
        actual = self.room.calculate_expenses(self.room.children)
        self.assertEqual(expected, actual)

    def test_room_expenses_prop__if_value_is_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1


if __name__ == "__main__":
    test_one()