
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, millilitres):
       if self.quantity + millilitres <= self.size:
           self.quantity += millilitres

    def status(self):
        return self.size - self.quantity


# Examples
cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())