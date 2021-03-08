class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @classmethod
    def get_class_type(cls):
        return Cheetah.__name__

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
