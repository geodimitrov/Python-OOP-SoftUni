from abc import ABC, abstractmethod

class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    def avail_capacity(self):
        return self.capacity - len(self.fish)

    def calculate_comfort(self):
        return sum([deco.comfort for deco in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def get_fish_names(self):
        result = [fish.name for fish in self.fish]
        if result:
            return " ".join(result)
        return "none"

    def __str__(self):
        return f'{self.name}:\nFish: {self.get_fish_names()}\n'\
               f"Decorations: {len(self.decorations)}\n"\
               f"Comfort: {self.calculate_comfort()}"