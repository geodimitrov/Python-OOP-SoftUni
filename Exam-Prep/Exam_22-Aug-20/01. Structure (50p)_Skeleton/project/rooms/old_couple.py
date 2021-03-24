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
