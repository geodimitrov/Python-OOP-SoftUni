
class Everland:
    def __init__(self):
        self.rooms = []

    def pay_for_room(self, room):

        if room.budget < room.total_monthly_cost:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

        room.budget -= room.total_monthly_cost
        return f"{room.family_name} paid {room.total_monthly_cost:.2f}$ and have {room.budget:.2f}$ left."

    def get_total_population(self):
        return sum(r.members_count for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_monthly_consumption = sum([r.total_monthly_cost for r in self.rooms])
        return f"Monthly consumption: {total_monthly_consumption:.2f}$."

    def pay(self):
        return "\n".join([self.pay_for_room(r) for r in self.rooms])

    def status(self):
        return f"Total population: {self.get_total_population()}\n" \
    + "\n".join(r.get_room_info() for r in self.rooms)