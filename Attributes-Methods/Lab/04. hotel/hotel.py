class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        instance_name = f"{stars_count} stars Hotel"
        return cls(instance_name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        pass


    def free_room(self, room_number):
        return

    def print_status(self):
        pass
