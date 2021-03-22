class sequence_repeat:
    def __init__(self, sequence, number):
        self.seq = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration()

        if self.index == len(self.seq):
            self.index = 0

        char = self.seq[self.index]
        self.index += 1
        self.number -= 1

        return char

# test code
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')