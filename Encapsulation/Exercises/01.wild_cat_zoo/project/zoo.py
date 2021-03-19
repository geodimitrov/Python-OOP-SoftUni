class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    @staticmethod
    def has_enough_space(collection, capacity):
        return len(collection) < capacity

    @staticmethod
    def has_enough_budget(budget, price):
        return price <= budget

    @staticmethod
    def get_sum_workers_salaries(workers):
        result = 0
        for worker in workers:
            result += getattr(worker, "salary")
        return result

    @staticmethod
    def get_sum_animals_needs(animals):
        result = 0
        for animal in animals:
            result += animal.get_needs()
        return result

    @staticmethod
    def get_objects_by_class_type(type, collection):
        return [obj for obj in collection if obj.__class__.__name__ == type]

    def add_to_zoo(self, animal, price):
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def add_animal(self, animal, price):
        if not self.has_enough_space(self.animals, self.__animal_capacity):
            return "Not enough space for animal"
        if not self.has_enough_budget(self.__budget, price):
            return "Not enough budget"
        return self.add_to_zoo(animal, price)

    def hire_worker(self, worker):
        if not self.has_enough_space(self.workers, self.__workers_capacity):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker = [obj for obj in self.workers if obj.name == worker_name]
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salaries = self.get_sum_workers_salaries(self.workers)
        if not self.has_enough_budget(self.__budget, workers_salaries):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_needs = self.get_sum_animals_needs(self.animals)
        if not self.has_enough_budget(self.__budget, animals_needs):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animals_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return f"You have {len(self.animals)} animals\n" \
            + f"----- {len(self.get_objects_by_class_type('Lion', self.animals))} Lions:\n" \
            + "".join(f"{obj.__repr__()}\n" for obj in self.get_objects_by_class_type('Lion', self.animals))\
            + f"----- {len(self.get_objects_by_class_type('Tiger', self.animals))} Tigers:\n" \
            + "".join(f"{obj.__repr__()}\n" for obj in self.get_objects_by_class_type('Tiger', self.animals)) \
            + f"----- {len(self.get_objects_by_class_type('Cheetah', self.animals))} Cheetahs:\n" \
            + "\n".join(obj.__repr__() for obj in self.get_objects_by_class_type('Cheetah', self.animals))

    def workers_status(self):
        return f"You have {len(self.workers)} workers\n" \
            + f"----- {len(self.get_objects_by_class_type('Keeper', self.workers))} Keepers:\n" \
            + "".join(f"{obj.__repr__()}\n" for obj in self.get_objects_by_class_type('Keeper', self.workers))\
            + f"----- {len(self.get_objects_by_class_type('Caretaker', self.workers))} Caretakers:\n" \
            + "".join(f"{obj.__repr__()}\n" for obj in self.get_objects_by_class_type('Caretaker', self.workers)) \
            + f"----- {len(self.get_objects_by_class_type('Vet', self.workers))} Vets:\n" \
            + "\n".join(obj.__repr__() for obj in self.get_objects_by_class_type('Vet', self.workers))