from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    property
    def total_population(self):
        return sum(room.members_count for room in self.rooms)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = sum(room.total_monthly_cost for room in self.rooms)
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def pay_for_room(self, room):
        if room.total_monthly_cost > room.budget:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."

        room.budget -= room.total_monthly_cost
        return f"{room.family_name} paid {room.total_monthly_cost}$ and have {room.budget}$ left."

    def pay(self):
        return "\n".join(self.pay_for_room(room) for room in self.rooms)

    def status(self):
        return f"Total population: {self.total_population()}\n" + \
               "\n".join(room.__repr__() for room in self.rooms)