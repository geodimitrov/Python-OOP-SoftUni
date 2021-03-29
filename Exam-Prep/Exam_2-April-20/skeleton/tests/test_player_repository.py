import unittest
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class PlayerRepoTests(unittest.TestCase):

    def setUp(self):
        self.player_repo = PlayerRepository()
        self.player = Beginner("Misho")

    def test_player_repo_init__expect_initialization(self):
        self.assertEqual(0, self.player_repo.count)
        self.assertEqual([], self.player_repo.players)

    def test_player_repo_add__if_player_exists__expect_exception(self):
        self.player_repo.add(self.player)
        with self.assertRaises(ValueError) as ex:
            self.player_repo.add(self.player)

    def test_player_repo_add__if_player_does_not_exist__expect_correct_result(self):
        self.player_repo.add(self.player)
        self.assertEqual(1, self.player_repo.count)

    def test_player_repo_remove__if_player_empty_str__expect_exception(self):
        with self.assertRaises(ValueError):
            self.player_repo.remove("")

    def test_player_repo_remove__if_player_not_empty_str__expect_correct_result(self):
        self.player_repo.add(self.player)
        self.player_repo.remove("Misho")
        self.assertEqual(0, self.player_repo.count)

    def test_player_repo_find__to_return_correct_result(self):
        self.player_repo.add(self.player)
        expected = self.player
        actual = self.player_repo.find("Misho")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()