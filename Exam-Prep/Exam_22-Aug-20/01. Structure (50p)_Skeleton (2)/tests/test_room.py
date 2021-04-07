import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Testov", 200, 2)

    def test_room_init__expect_to_set_attrs(self):
        self.assertEqual("Testov", self.room.family_name)
        self.assertEqual(200, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertListEqual([], self.room.children)
        self.assertTrue(hasattr(self.room, "expenses"))

    def test_room_expenses_prop__if_value_is_negative__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -5
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_room_expenses_prop__if_value_is_non_negative__expect_to_set_prop(self):
        self.room.expenses = 150
        self.assertEqual(150, self.room.expenses)

    # def test_room_expenses_prop__set_through_calculate_expenses_method__expect_correct_result(self):
    #     appliances = [TV()]
    #     self.room.calculate_expenses(appliances)
    #     self.assertEqual(45, self.room.expenses)


if __name__ == "__main__":
    unittest.main()