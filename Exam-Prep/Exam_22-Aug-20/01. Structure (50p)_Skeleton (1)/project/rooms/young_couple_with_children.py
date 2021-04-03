from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.people.child import Child

class YoungCoupleWithChildren(Room):
    __MEMBERS = 2

    def __init__(self, family_name, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, YoungCoupleWithChildren.__MEMBERS + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    def get_children_info(self):
        result = ""
        counter = 1
        for child in self.children:
            result += f"--- Child {counter} monthly cost: {child.monthly_cost:.2f}$\n"
            counter += 1
        return result

    def get_room_info(self):
        return f"{self.family_name} with {self.members_count} members. \
Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" \
+ self.get_children_info() + \
f"--- Appliances monthly cost: {self.monthly_appliances_cost:.2f}$"