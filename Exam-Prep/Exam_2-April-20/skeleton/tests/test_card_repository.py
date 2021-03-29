import unittest
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class CardRepoTests(unittest.TestCase):

    def setUp(self):
        self.card_repo = CardRepository()
        self.card = MagicCard("Slayer")

    def test_card_repo_init__expect_initialization(self):
        self.assertEqual(0, self.card_repo.count)
        self.assertEqual([], self.card_repo.cards)

    def test_card_repo_add__if_card_exists__expect_exception(self):
        self.card_repo.add(self.card)
        with self.assertRaises(ValueError) as ex:
            self.card_repo.add(self.card)
        self.assertEqual("Card Slayer already exists!", str(ex.exception))

    def test_card_repo_add__if_card_does_not_exist__expect_correct_result(self):
        self.card_repo.add(self.card)
        self.assertEqual(1, self.card_repo.count)

    def test_card_repo_remove__if_card_empty_str__expect_exception(self):
        with self.assertRaises(ValueError):
            self.card_repo.remove("")

    def test_card_repo_remove__if_card_not_empty_str__expect_correct_result(self):
        self.card_repo.add(self.card)
        self.card_repo.remove("Slayer")
        self.assertEqual(0, self.card_repo.count)

    def test_card_repo_find__to_return_correct_result(self):
        self.card_repo.add(self.card)
        expected = self.card
        actual = self.card_repo.find("Slayer")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()