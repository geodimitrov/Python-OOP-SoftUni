from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    MEMBERS = 2

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. \
Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n\
--- Appliances monthly cost: {self.get_appliances_monthly_cost(self):.2f}$"