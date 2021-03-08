class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0

#Test Code
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)
print(second_room.take_room(2))
print(second_room.guests)