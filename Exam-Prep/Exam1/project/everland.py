from people.child import Child
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren

class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        room_cost_monthly = sum([room.room_cost for room in self.rooms])
        room_expenses_monthly = sum([room.expenses for room in self.rooms]) * 30
        return f"Monthly consumption: {room_expenses_monthly + room_cost_monthly:.2f}$."

    def pay(self):
        for room in self.rooms:
            if room.budget < room.expenses * 30 + room.room_cost:
                result = f"{room.family_name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
            else:
                room.budget -= room.expenses * 30 + room.room_cost
                result = f"{room.family_name} paid {room.expenses * 30 + room.room_cost}$ and have {room.budget}$ left."

    def status(self):
        total_population = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        room_info = "".join(f"{room.__repr__()}" for room in self.rooms)
        return total_population + room_info


everland = Everland()
young_couple = YoungCouple("Johnsons", 150, 205)
# print(young_couple.__dict__)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
# print(young_couple_with_children.__dict__)
everland.add_room(young_couple)
everland.add_room(young_couple_with_children)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())