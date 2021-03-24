from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    MEMBERS = 1

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, self.MEMBERS)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
