class Everland:

    def __init__(self):
        self.rooms = []

    def get_monthly_consumptions(self):
        total_monthly_consumption = sum(room.get_room_monthly_expenses(room) for room in self.rooms)
        return f"Monthly consumption: {total_monthly_consumption:.2f}$."

    def add_room(self, room):
        self.rooms.append(room)

    def pay_for_room(self, room):
        monthly_expenses = room.get_room_monthly_expenses(room)

        if room.budget < monthly_expenses:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

        room.budget -= monthly_expenses
        return f"{room.family_name} paid {monthly_expenses:.2f}$ and have {room.budget:.2f}$ left."

    def pay(self):
        return "\n".join(self.pay_for_room(room) for room in self.rooms)

    def status(self):
        return f"Total population: {sum(room.members_count for room in self.rooms)}\n" \
             + "\n".join(room.__repr__() for room in self.rooms)