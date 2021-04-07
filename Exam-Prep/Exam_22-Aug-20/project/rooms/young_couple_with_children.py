from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    default_room_members = 2
    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, self.default_room_members + len(children))
        self.appliances = YoungCoupleWithChildren.appliances * self.members_count
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)

    @property
    def appliances_monthly_cost(self):
        return sum(appl.get_monthly_expense() for appl in self.appliances)

    @staticmethod
    def get_children_info(children):
        result = ""
        for i in range(len(children)):
            child = children[i]
            result += f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$\n"

        return result

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$\n" \
        + self.get_children_info(self.children) + f"--- Appliances monthly cost: {self.appliances_monthly_cost:.2f}$"