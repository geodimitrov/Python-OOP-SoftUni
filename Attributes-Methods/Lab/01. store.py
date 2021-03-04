class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @staticmethod
    def from_size(name, type, size):
        capacity = size // 2
        return Store(name, type, capacity)


    def add_item(self, item_name: str):
        if sum([key for key in self.items.keys()]) + 1 > self.capacity:
            return "Not enough capacity in the store"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if item_name in self.items and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the store"
        return f"Cannot remove {amount} {item_name}"


    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# Test Code
first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)
print(first_store.name)
print(second_store.name)
print(second_store.capacity)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))