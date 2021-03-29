from abc import ABC
from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username, health):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"Username: {self.username} - Health: {self.health} - Cards {self.card_repository.count}"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string. ")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value

    @property
    def is_dead(self):
        return self.health <= 0

    @property
    def bonus_health_points(self):
        return sum(card.health_points for card in self.card_repository.cards)

    def add_bonus_health_points(self):
        self.health += self.bonus_health_points

    def take_damage(self, damage_points):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points