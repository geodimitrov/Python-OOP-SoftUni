class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    @staticmethod
    def sufficient_fuel(fuel, fuel_consumption, distance):
        return fuel >= fuel_consumption * distance

    def drive(self, kilometers):
        if self.sufficient_fuel(self.fuel, self.fuel_consumption, kilometers):
            self.fuel -= self.fuel_consumption * kilometers