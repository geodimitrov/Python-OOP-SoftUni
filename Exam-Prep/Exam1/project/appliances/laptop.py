from project.appliances.appliance import Appliance

class Laptop(Appliance):
    LAPTOP_COST = 1.0

    def __init__(self):
        super().__init__(Laptop.LAPTOP_COST)
