class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @classmethod
    def get_class_type(cls):
        return Lion.__name__

    def get_needs(self):
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"