class Everland:
    def __init__(self):
        self.rooms = []

    @staticmethod
    def get_room_monthly_expenses(room):
        return room.expenses * 30 + room.room_cost

    @staticmethod
    def get_appliances_monthly_cost(room):
        return sum(appl.cost for appl in room.appliances) * 30

    @staticmethod
    def get_children_info(room):
        counter = 1
        result = ""
        for child in room.children:
            result += f"--- Child {counter} monthly cost: {child.cost * 30:.2f}$\n"
            counter += 1
        return result

    @staticmethod
    def get_room_status(room):
        if room.children:
            return f"{room.family_name} with {room.members_count} members. \
Budget: {room.budget:.2f}$, Expenses: {room.expenses * 30:.2f}$\n" \
+ f"{Everland.get_children_info(room)}" + f"--- Appliances monthly cost: \
{Everland.get_appliances_monthly_cost(room):.2f}$"
        return f"{room.family_name} with {room.members_count} members. \
Budget: {room.budget:.2f}$, Expenses: {room.expenses * 30:.2f}$\n" \
+ f"--- Appliances monthly cost: {Everland.get_appliances_monthly_cost(room):.2f}$"

    def pay_for_room(self, room):
        monthly_expenses = self.get_room_monthly_expenses(room)

        if room.budget < monthly_expenses:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

        room.budget -= monthly_expenses
        return f"{room.family_name} paid {monthly_expenses:.2f}$ and have {room.budget:.2f}$ left."


    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_monthly_consumption = sum(self.get_room_monthly_expenses(room) for room in self.rooms)
        return f"Monthly consumption: {total_monthly_consumption:.2f}$."

    def pay(self):
        return "\n".join(self.pay_for_room(room) for room in self.rooms)

    def status(self):
        return f"Total population: {sum(room.members_count for room in self.rooms)}\n" \
             + "\n".join(self.get_room_status(room) for room in self.rooms)