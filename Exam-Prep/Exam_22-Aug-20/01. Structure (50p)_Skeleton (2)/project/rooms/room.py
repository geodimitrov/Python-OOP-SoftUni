from abc import ABC, abstractmethod

class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def get_room_monthly_expenses(room):
        return room.expenses * 30 + room.room_cost

    @staticmethod
    def get_appliances_monthly_cost(room):
        return sum(appl.cost for appl in room.appliances) * 30

    def calculate_expenses(self, *args):
        return sum(obj.cost for el in args for obj in el)