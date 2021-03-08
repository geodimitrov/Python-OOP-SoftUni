class Keeper:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def get_class_type(cls):
        return Keeper.__name__

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"