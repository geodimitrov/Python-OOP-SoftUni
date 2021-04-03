from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    __MEMBERS = 2

    def __init__(self, family_name, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, YoungCouple.__MEMBERS)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)
