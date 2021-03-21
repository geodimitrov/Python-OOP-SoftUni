class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.keys = [key for key in self.dict]
        self.index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        self.index += 1
        return (key, self.dict[key])


# test code
result = dictionary_iter({1: "One", 2: "Two"})
for x in result:
    print(x)