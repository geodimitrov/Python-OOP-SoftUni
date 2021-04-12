from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
    valid_decoration_types = ["Ornament", "Plant"]
    valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def create_aquarium_and_return_it(a_type, a_name):
        if a_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(a_name)
        else:
            aquarium = SaltwaterAquarium(a_name)
        return aquarium

    @staticmethod
    def create_decoration_and_return_it(d_type):
        if d_type == "Ornament":
            decoration = Ornament()
        else:
            decoration = Plant()
        return decoration

    @staticmethod
    def create_fish_and_return_it(fish_type, fish_name, fish_species, fish_price):
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, fish_price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, fish_price)
        return fish

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.valid_aquarium_types:
            return "Invalid aquarium type."
        self.aquariums.append(self.create_aquarium_and_return_it(aquarium_type, aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.valid_decoration_types:
            return "Invalid decoration type."
        self.decorations_repository.add(self.create_decoration_and_return_it(decoration_type))
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if decoration_type not in [deco.__class__.__name__ for deco in self.decorations_repository.decorations]:
            return f"There isn't a decoration of type {decoration_type}."

        if aquarium_name in [a.name for a in self.aquariums]:
            decoration = [deco for deco in self.decorations_repository.decorations if decoration_type == deco.__class__.__name__][0]
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.valid_fish_types:
            return f"There isn't a fish of type {fish_type}."
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        fish = self.create_fish_and_return_it(fish_type, fish_name, fish_species, price)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium_value = sum(fish.price for fish in aquarium.fish) + sum(deco.price for deco in aquarium.decorations)
        return f"The value of Aquarium {aquarium.name} is {aquarium_value:.2f}."

    def report(self):
        return "\n".join(str(aquarium) for aquarium in self.aquariums)