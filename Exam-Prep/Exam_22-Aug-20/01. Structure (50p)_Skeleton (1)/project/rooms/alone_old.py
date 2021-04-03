from project.rooms.room import Room


class AloneOld(Room):
    __MEMBERS = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, AloneOld.__MEMBERS)
        self.room_cost = 10