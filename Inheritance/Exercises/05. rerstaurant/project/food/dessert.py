from project.food.food import Food

class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories


# dessert = Dessert("K", 2.5, 100, 1000)
# print(dessert.__dict__)