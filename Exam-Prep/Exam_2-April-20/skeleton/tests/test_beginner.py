import unittest

from project.player.beginner import Beginner


class BeginnerTests(unittest.TestCase):

    def test_beginner_init__expect_initialization(self):
        beginner_player = Beginner("Chochko")
        self.assertEqual("Chochko", beginner_player.username)
        self.assertEqual(50, beginner_player.health)

if __name__ == "__main__":
    unittest.main()