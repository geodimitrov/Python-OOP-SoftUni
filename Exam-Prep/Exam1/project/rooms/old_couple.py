from appliances.fridge import Fridge
from appliances.stove import Stove
from appliances.tv import TV
from rooms.room import Room

class OldCouple(Room):
    MEMBERS = 2

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, OldCouple.MEMBERS)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()]
        self.expenses = self.calculate_expenses(self.appliances) * self.members_count

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" \
            + f"--- Appliances monthly cost: {self.expenses * 30:.2f}$\n"