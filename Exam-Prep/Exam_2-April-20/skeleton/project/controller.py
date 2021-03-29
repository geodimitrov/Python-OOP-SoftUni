from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository

class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    @staticmethod
    def get_player(username, repository):
        return [p for p in repository if p.username == username][0]

    @staticmethod
    def get_card(name, repository):
        return [c for c in repository if c.name == name][0]

    def add_player(self, type, username):
        if type == "Beginner":
            player = Beginner(username)
        else:
            player = Advanced(username)
        self.player_repository.players.append(player)
        self.player_repository.count += 1
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.cards.append(card)
        self.card_repository.count += 1
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.get_player(username, self.player_repository.players)
        card = self.get_card(card_name, self.card_repository.cards)
        player.card_repository.cards.append(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.get_player(attack_name, self.player_repository.players)
        enemy = self.get_player(enemy_name, self.player_repository.players)
        BattleField().fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        return "".join(f"{player.__repr__()}\n" for player in self.player_repository.players) \
    + "".join(f"{card.__repr__()}\n" for card in self.card_repository.cards)