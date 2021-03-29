import unittest
from project.controller import Controller

class ControllerTests(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_controller_add_player__expect_correct_result(self):
        expected_msg = f"Successfully added player of type Advanced with username: Pepi"
        actual_msg = self.controller.add_player("Advanced", "Pepi")
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual(1, self.controller.player_repository.count)

    def test_controller_add_card__expect_correct_result(self):
        expected_msg = "Successfully added card of type MagicCard with name: Cun"
        actual_msg = self.controller.add_card("Magic", "Cun")
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual(1, self.controller.card_repository.count)

    def test_controller_add_player_card__expect_correct_result(self):
        self.controller.add_player("Advanced", "Pepi")
        self.controller.add_card("Magic", "Cun")
        expected_msg = "Successfully added card: Cun to user: Pepi"
        actual_msg = self.controller.add_player_card("Pepi", "Cun")
        self.assertEqual(expected_msg, actual_msg)

    def test_controller_fight__expect_execution(self):
        expected_msg = f"Attack user health {attacker.health} - Enemy user health {enemy.health}"
    #
    # def test_controller_report

if __name__ == "__main__":
    unittest.main()