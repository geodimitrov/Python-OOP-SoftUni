from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    __MILLILITERS = 50
    __PRICE = 3.50

    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
