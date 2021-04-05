class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_obj(id, objects):
        return [obj for obj in objects if obj.id == id][0]

    def add_customer(self, customer):
        if customer not in self. customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_obj(subscription_id, self.subscriptions)
        customer = self.get_obj(subscription.customer_id, self.customers)
        trainer = self.get_obj(subscription.trainer_id, self.trainers)
        plan = [plan for plan in self.plans if plan.trainer_id == trainer.id][0]
        equipment = self.get_obj(plan.equipment_id, self.equipment)
        return f"{subscription.__repr__()}\n" + f"{customer.__repr__()}\n" \
        + f"{trainer.__repr__()}\n" + f"{equipment.__repr__()}\n" + f"{plan.__repr__()}"