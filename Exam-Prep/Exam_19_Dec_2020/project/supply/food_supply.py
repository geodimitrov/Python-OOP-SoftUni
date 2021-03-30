from project.supply.supply import Supply

class FoodSupply(Supply):
    NEEDS_INCREASE = 20

    def __init__(self):
        super().__init__(self.NEEDS_INCREASE)

    def __str__(self):
        return "food"