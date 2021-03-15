class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def add_obj_to_collection(obj, collection):
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def get_obj(id, objects):
        return [obj for obj in objects if obj.id == id][0]

    def add_customer(self, customer):
        self.add_obj_to_collection(customer, self.customers)

    def add_trainer(self, trainer):
        self.add_obj_to_collection(trainer, self.trainers)

    def add_equipment(self, equipment):
        self.add_obj_to_collection(equipment, self.equipment)

    def add_plan(self, plan):
        self.add_obj_to_collection(plan, self.plans)

    def add_subscription(self, subscription):
        self.add_obj_to_collection(subscription, self.subscriptions)

    def subscription_info(self, subscription_id):
        subscription = self.get_obj(subscription_id, self.subscriptions)
        customer = self.get_obj(subscription.customer_id, self.customers)
        trainer = self.get_obj(subscription.trainer_id, self.trainers)
        plan = [plan for plan in self.plans if plan.trainer_id == trainer.id][0]
        equipment = self.get_obj(plan.equipment_id, self.equipment)
        return f"{subscription.__repr__()}\n" + f"{customer.__repr__()}\n" \
        + f"{trainer.__repr__()}\n" + f"{equipment.__repr__()}\n" + f"{plan.__repr__()}"