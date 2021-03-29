from abc import ABC

class Card(ABC):
    def __init__(self, name, damage_points, health_points):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"### Card: {self.name} - Damage: {self.damage_points}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Card's name cannot be an empty string.")
        self.__name = value

    @property
    def damage_points(self):
        return self.__damage_points

    @damage_points.setter
    def damage_points(self, value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        self.__damage_points = value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self.__health_points = value