from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30
        self.children = children
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(children) + self.calculate_expenses(self.appliances)


# couple = YoungCoupleWithChildren("Pep", 100, 250, Child(10, 1, 2), Child(11, 3))
# print(couple.expenses)