from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    MEMBERS = 2
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, self.MEMBERS)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. \
Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n\
--- Appliances monthly cost: {self.get_appliances_monthly_cost(self):.2f}$"