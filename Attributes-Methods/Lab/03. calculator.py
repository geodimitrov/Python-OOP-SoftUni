
class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        product = 1
        for num in args:
            product *= num
        return product

    @staticmethod
    def divide(*args):
        product = args[0]
        for num in args[1:]:
            product /= num
        return product

    @staticmethod
    def subtract(*args):
        product = args[0]
        for num in args[1:]:
            product -= num
        return product

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
print(Calculator.divide(6, 3, 2))