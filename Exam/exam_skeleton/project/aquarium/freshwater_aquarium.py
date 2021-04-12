from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    default_capacity = 50
    fish_type = "FreshwaterFish"

    def __init__(self, name: str):
        super().__init__(name, self.default_capacity)

    def add_fish(self, fish):
        if self.avail_capacity == 0:
            return "Not enough capacity."

        if not fish.__class__.__name__ == self.fish_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."