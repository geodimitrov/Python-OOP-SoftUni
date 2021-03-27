import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Colombo", 5, 100, 10)
        self.enemy = Hero("Ork", 3, 70, 10)

    def test_hero_init__expect_initialization(self):
        self.assertEqual("Colombo", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_hero_battle__if_fighting_yourself__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle__if_hero_health_less_or_equal_to_0__expect_exception(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle__if_enemy_health_less_or_equal_to_0__expect_exception(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_hero_battle_outcome__if_hero_and_enemy_health_less_or_equal_to_0__expect_draw_msg(self):
        self.hero.health = 5
        self.enemy.health = 5
        expected = "Draw"
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)

    def test_hero_battle_outcome__if_enemy_health_less_or_equal_to_0__expect_win_msg(self):
        self.enemy.health = 10
        expected = "You win"
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(75, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_hero_battle_outcome__if_hero_health_less_or_equal_to_0__expect_lose_msg(self):
        self.hero.health = 15
        expected = "You lose"
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)
        self.assertEqual(4, self.enemy.level)
        self.assertEqual(25, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_hero_str__expect_str_message(self):
        expected_msg = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_msg = self.hero.__str__()
        self.assertEqual(expected_msg, actual_msg)

if __name__ == "__main__":
    unittest.main()