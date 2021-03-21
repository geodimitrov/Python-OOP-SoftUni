class Child:
    def __init__(self, food_cost, *toys_cost):
        self.cost = float(food_cost + sum(toys_cost))