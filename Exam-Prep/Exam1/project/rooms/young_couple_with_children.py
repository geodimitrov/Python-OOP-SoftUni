from appliances.fridge import Fridge
from appliances.laptop import Laptop
from appliances.tv import TV
from rooms.room import Room

class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, * children):
        super().__init__(family_name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30
        self.children = children
        self.appliances = [TV(), Fridge(), Laptop()]
        self.expenses = self.calculate_expenses(self.children) \
                        + (self.calculate_expenses(self.appliances) * self.members_count)

    def __repr__(self):
        children_info = ""
        counter = 1
        appliances_monthly_cost = (self.calculate_expenses(self.appliances) * self.members_count) * 30
        for child in self.children:
            children_info += f"--- Child {counter} monthly cost: {child.cost * 30:.2f}$\n"
            counter += 1

        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" \
                + children_info + f"--- Appliances monthly cost: {appliances_monthly_cost:.2f}$\n"