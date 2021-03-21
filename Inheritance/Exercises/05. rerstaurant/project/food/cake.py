from project.food.dessert import Dessert


class Cake(Dessert):
    __GRAMS = 250
    __CALORIES = 1000
    __PRICE = 5

    def __init__(self, name):
        super().__init__(name, Cake.__PRICE, Cake.__GRAMS, Cake.__PRICE)