import unittest
from project.card.trap_card import TrapCard

class TrapCardTests(unittest.TestCase):

    def test_trap_card_init__expect_initialization(self):
        card = TrapCard("OrcSlayer")
        self.assertEqual("OrcSlayer", card.name)
        self.assertEqual(120, card.damage_points)
        self.assertEqual(5, card.health_points)


if __name__ == "__main__":
    unittest.main()