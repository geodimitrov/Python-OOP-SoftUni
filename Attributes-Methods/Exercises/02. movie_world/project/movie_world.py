class MovieWorld:
    def __init__(self, name):
        self.customers = []
        self.dvds = []

    def __repr__(self):
        pass

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def get_customer()

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        pass

    def return_dvd(self, customer_id, dvd_id):
        customer = get_customer()
