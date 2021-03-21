from project.food.main_dish import MainDish

class Salmon(MainDish):
    __GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.__GRAMS)


# test code
# dish = Salmon("Bla", 11.50)
# print(dish.grams)