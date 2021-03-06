class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def get_room(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]

    def get_total_guests(self):
        return sum([room.guests for room in self.rooms])

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.get_room(room_number)
        room.take_room(people)

    def free_room(self, room_number):
        room = self.get_room(room_number)
        room.free_room()

    def print_status(self):
        total_guests = self.get_total_guests()
        print(f"Hotel {self.name} has {total_guests} total guests")
        print(f"Free rooms: {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}")
        print(f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}")

# test code
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# hotel.print_status()