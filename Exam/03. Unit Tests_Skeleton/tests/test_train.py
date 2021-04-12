import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):

    def setUp(self):
        self.train = Train("Willy", 10)

    def test_train_init(self):
        self.assertEqual("Willy", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_train_add(self):
        self.train.capacity = 1
        self.train.add("Bobby")
        self.assertIn("Bobby", self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

        with self.assertRaises(ValueError):
            self.train.add("Mickey")

        with self.assertRaises(ValueError) as ex:
            self.train.add("Bobby")

    def test_train_remove(self):
        self.train.add("Bobby")
        self.train.remove("Bobby")
        self.assertNotIn("Bobby", self.train.passengers)
        self.assertEqual(0, len(self.train.passengers))

if __name__ == "__main__":
    unittest.main()