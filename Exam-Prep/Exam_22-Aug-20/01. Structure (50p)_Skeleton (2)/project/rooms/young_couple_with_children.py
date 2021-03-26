from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    MEMBERS = 2
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS + len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    @staticmethod
    def get_children_info(room):
        counter = 1
        result = ""
        for child in room.children:
            result += f"--- Child {counter} monthly cost: {child.cost * 30:.2f}$\n"
            counter += 1
        return result

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. \
Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n\
{self.get_children_info(self)}--- Appliances monthly cost: \
{self.get_appliances_monthly_cost(self):.2f}$"