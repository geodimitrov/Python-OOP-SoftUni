class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.end = step * count

    def __iter__(self):
        return self

    def __next__(self):
        index = self.start
        if index >= self.end:
            raise StopIteration
        self.start += self.step
        return index


numbers = take_skip(10, 5)
for number in numbers:
    print(number)