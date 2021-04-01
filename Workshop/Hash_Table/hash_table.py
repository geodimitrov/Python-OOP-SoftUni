class HashTable:
    def __init__(self):
        self.__capacity = 4
        self.keys = [None] * self.__capacity
        self.values = [None] * self.__capacity

    @property
    def length(self):
        return len([key for key in self.keys if key])

    def __getitem__(self, key):
        index = self.keys.index(key)
        return self.values[index]

    def __setitem__(self, key, value):
        if key in self.keys:
            current_index = self.keys.index(key)
            self.values[current_index] = value
        else:
            index = self.hash(key)
            self.values[index] = value
            self.keys[index] = key

    def __len__(self):
        return self.__capacity

    def __repr__(self):
        return ", ".join(
            [f'{self.keys[i]}: {self.values[i]}'
            for i in range(len(self.keys))
            if self.keys[i] is not None]
        )

    def __validate_index(self, index):
        if index == self.__capacity:
            index = 0
        if self.keys[index] is None:
            return index
        return self.__validate_index(index + 1)

    def hash(self, key):
        if self.length == self.__capacity:
            self.keys += [None] * self.__capacity
            self.values += [None] * self.__capacity
            self.__capacity *= 2
        index = sum([ord(char) for char in key]) % self.__capacity
        avail_index = self.__validate_index(index)
        return avail_index

    def add(self, key, value):
        self[key] = value

    def get(self, key):
        value_index = self.keys.index(key)
        return self.values[value_index]


table = HashTable()

# table["name"] = "Peter"
# print(table)
# table["name"] = "George"
# print(table)
# table["age"] = 25
# table["occupation"] = "clerk"
# table["favorite food"] = "pizza"
# table["town"] = "Sofia"
# table["town"] = "Burgas"
# table.add("movie", "Pulp Fiction")
# print(table)
#
# print(table.get("name"))
# print(table["age"])
# print(len(table))

table.add("Key1", "value1")
print(table)