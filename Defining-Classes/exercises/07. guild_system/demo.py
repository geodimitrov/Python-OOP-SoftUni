from project.pokemon import Pokemon
from project.trainer import Trainer

import unittest


class PokemonTest(unittest.TestCase):
    def test_pokemon_init(self):
        pokemon = Pokemon("Pesho", 90)
        message = pokemon.pokemon_details()
        expected = "Pesho with health 90"
        self.assertEqual(message, expected)

    def test_trainer_init(self):
        trainer = Trainer("Stamat")
        message = f"{trainer.name} 0"
        expected = f"Stamat 0"
        self.assertEqual(message, expected)

    def test_adding_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        message = trainer.add_pokemon(pokemon)
        expected = "Caught Pesho with health 90"
        self.assertEqual(message, expected)

    def test_adding_already_addded_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        trainer.add_pokemon(pokemon)
        message = trainer.add_pokemon(pokemon)
        expected = "This pokemon is already caught"
        self.assertEqual(message, expected)

    def test_releasing_pokemon(self):
        trainer = Trainer("Stamat")
        pokemon = Pokemon("Pesho", 90)
        trainer.add_pokemon(pokemon)
        message = trainer.release_pokemon("Pesho")
        expected = "You have released Pesho"
        self.assertEqual(message, expected)

    def test_releasing_pokemon_that_is_not_caught(self):
        trainer = Trainer("Stamat")
        message = trainer.release_pokemon("Pesho")
        expected = "Pokemon is not caught"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()