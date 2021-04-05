class Equipment:
    __id = 0

    def __init__(self, name):
        self.name = name
        Equipment.__id += 1
        self.id = Equipment.__id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.__id + 1