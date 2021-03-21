class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj
        self.index = len(iterable_obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        if self.index < 0:
            raise StopIteration
        self.index -= 1
        return self.iterable[index]

#test code
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)