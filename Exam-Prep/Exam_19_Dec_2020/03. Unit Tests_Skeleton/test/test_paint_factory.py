import unittest
from project.factory.paint_factory import PaintFactory

class PaintFactoryTests(unittest.TestCase):

    def setUp(self):
        self.factory = PaintFactory("A Factory", 3)

    def test_paint_factory_init__expect_initialization(self):
        self.assertEqual("A Factory", self.factory.name)
        self.assertEqual(3, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_paint_factory_add_ingredient__if_ingredient_not_valid__expect_exception(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("WHITE", 2)

    def test_paint_factory__add_ingredient__if_not_enough_space__expect_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 5)

    def test_paint_factory__add_ingredient__if_valid_ingredient_and_enough_space__expect_correct_result(self):
        self.factory.add_ingredient("white", 1)
        self.assertEqual(1, self.factory.ingredients["white"])

    def test_paint_factory_remove_ingredient(self):
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("WHITE", 2)

        self.factory.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 3)

        self.factory.remove_ingredient("white", 2)
        self.assertEqual(0, self.factory.ingredients["white"])

    def test_paint_factory_products_property__expect_correct_result(self):
        self.factory.add_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.factory.products)

    def test_factory_can_add__expect_correct_result(self):
        values = 2
        self.assertTrue(self.factory.can_add(values))

if __name__ == "__main__":
    unittest.main()