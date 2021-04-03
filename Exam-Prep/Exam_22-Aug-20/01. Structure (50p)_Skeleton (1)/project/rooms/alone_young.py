from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    __MEMBERS = 1

    def __init__(self, family_name, salary: float):
        super().__init__(family_name, salary, AloneYoung.__MEMBERS)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
