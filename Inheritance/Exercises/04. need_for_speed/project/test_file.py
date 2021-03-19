from project.family_car import FamilyCar
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.vehicle import Vehicle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
car = SportCar(50, 150)
print(SportCar.DEFAULT_FUEL_CONSUMPTION)
car.drive(3)
print(car.fuel)
motorcycle = RaceMotorcycle(100, 97)
motorcycle.drive(5)
print(motorcycle.fuel)