import unittest
from project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):

    def test_magic_card_init__expect_initialization(self):
        card = MagicCard("OrcSlayer")
        self.assertEqual("OrcSlayer", card.name)
        self.assertEqual(5, card.damage_points)
        self.assertEqual(80, card.health_points)


if __name__ == "__main__":
    unittest.main()