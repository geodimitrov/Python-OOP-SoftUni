from project.people.child import Child

class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value


    def calculate_expenses(self, *args):  # args will be lists
        return sum(obj.cost for el in args for obj in el)

    def __repr__(self):
        pass


# room = Room("Lala", 150, 3)
# room.expenses = -18
# print(room.expenses)
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
#
# room.calculate_expenses(child2, child1)
# print(room.expenses)