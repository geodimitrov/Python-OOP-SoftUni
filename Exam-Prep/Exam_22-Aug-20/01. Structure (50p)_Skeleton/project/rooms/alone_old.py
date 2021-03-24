from project.rooms.room import Room


class AloneOld(Room):
    MEMBERS = 1

    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, self.MEMBERS)
        self.room_cost = 10

