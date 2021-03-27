import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal("Chocho", "elephant", "trumpet")

    def test_mammal_make_sound__to_return_sound(self):
        expected_msg = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_msg = self.mammal.make_sound()
        self.assertEqual(expected_msg, actual_msg)

    def test_mammal_get_kingdom__to_return_kingdom_attr(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_mammal_info__to_return_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)

    def test_mammal_init__expect_initialization(self):
        self.assertEqual("Chocho", self.mammal.name)
        self.assertEqual("elephant", self.mammal.type)
        self.assertEqual("trumpet", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

if __name__ == "__main__":
    unittest.main()