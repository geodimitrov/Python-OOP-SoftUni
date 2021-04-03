from project.people.child import Child

class Room:
    def __init__(self, name, budget: float, members_count):
        self.family_name = name
        self.budget = budget        # FLOAT
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

    @property
    def total_monthly_cost(self):
        return self.expenses * 30 + self.room_cost

    @property
    def monthly_appliances_cost(self):
        return sum(a.get_monthly_expense() for a in self.appliances)

    def get_room_info(self):
        return f"{self.family_name} with {self.members_count} members. \
Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" + \
f"--- Appliances monthly cost: {self.monthly_appliances_cost:.2f}$"

    def calculate_expenses(self, *args):
        return sum([el.cost for arg in args for el in arg])