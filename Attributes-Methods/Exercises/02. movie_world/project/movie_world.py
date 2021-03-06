class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        return "".join(f"{customer.__repr__()}\n" for customer in self.customers) + \
               "".join(f"{dvd.__repr__()}\n" for dvd in self.dvds)

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def get_obj_by_id(objects, object_id):
        return [obj for obj in objects if obj.id == object_id][0]

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_obj_by_id(self.customers, customer_id)
        dvd = self.get_obj_by_id(self.dvds, dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_obj_by_id(self.customers, customer_id)
        dvd = self.get_obj_by_id(self.dvds, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        self.dvds.append(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"
