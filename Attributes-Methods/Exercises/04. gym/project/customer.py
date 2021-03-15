class Customer:
    id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.id
        Customer.id += 1


    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.id

# test code
# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# customer2 = Customer("Pepi", "Bulgaria Blvd", "pepi93@gmail.com")
# print(customer)
# print(customer2)
# print(Customer.get_next_id())