class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        index = self.start
        if index > self.end:
            raise StopIteration
        self.start += 1
        return index

#test code
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)