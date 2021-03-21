from appliances.tv import TV
from rooms.room import Room

class AloneYoung(Room):
    MEMBERS = 1

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, AloneYoung.MEMBERS)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)

    def __repr__(self):
        return f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}$\n" \
                + f"--- Appliances monthly cost: {self.expenses * 30:.2f}$\n"
