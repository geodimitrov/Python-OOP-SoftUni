class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = count

    def __iter__(self):
        return self

    def __next__(self):
        index = self.start
        if self.start < 0:
            raise StopIteration
        self.start -= 1
        return index


#test code
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")