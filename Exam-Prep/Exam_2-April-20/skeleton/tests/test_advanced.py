import unittest

from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):

    def test_advanced_init__expect_initialization(self):
        advanced_player = Advanced("Chochko")
        self.assertEqual("Chochko", advanced_player.username)
        self.assertEqual(250, advanced_player.health)

if __name__ == "__main__":
    unittest.main()