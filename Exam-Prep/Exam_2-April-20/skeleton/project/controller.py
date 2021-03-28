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

    def add_player(self, type, username):
        if type == "Beginner":
            player = Beginner(username)
        else:
            player = Advanced(username)
        self.player_repository.players.append(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.cards.append(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        card = [c for c in self.card_repository.cards if card_name == c.name][0]
        player = [p for p in self.player_repository.players if username == p.username][0]
        player.card_repository.cards.append(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        pass

    def report(self, player):
        return player.__repr__()