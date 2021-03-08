class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

    def __budget_and_space_for_animal(self, price):
        return self.__budget >= price\
               and len(self.animals) < self.__animal_capacity

    def __space_for_worker(self):
        return len(self.workers) < self.__workers_capacity

    def __enough_budget(self, total_to_pay):
        return self.__budget >= total_to_pay

    def __is_worker(self, worker_to_fire):
        return len(worker_to_fire) > 0

    def add_animal(self, animal, price):
        if self.__budget_and_space_for_animal(price):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.get_class_type()} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if not self.__space_for_worker():
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.get_class_type()} hired successfully"

    def fire_worker(self, worker_name):
        worker_to_fire = [worker for worker in self.workers if worker.name == worker_name]
        if not self.__is_worker(worker_to_fire):
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker_to_fire[0])
        return f"{worker_name} fired successfully"


    def pay_workers(self):
        workers_salaries = sum(getattr(worker, "salary") for worker in self.workers)
        if self.__enough_budget(workers_salaries):
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_needs = sum(animal.get_needs() for animal in self.animals)
        if self.__enough_budget(animal_needs):
            self.__budget -= animal_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if animal.get_class_type() == "Lion"]
        tigers = [animal for animal in self.animals if animal.get_class_type() == "Tiger"]
        cheetahs = [animal for animal in self.animals if animal.get_class_type() == "Cheetah"]
        return f"You have {len(self.animals)} animals"\
        + f"\n----- {len(lions)} Lions:\n" + "\n".join(lion.__repr__() for lion in lions)\
        + f"\n----- {len(tigers)} Tigers:\n" + "\n".join(tiger.__repr__() for tiger in tigers)\
        + f"\n----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetah.__repr__() for cheetah in cheetahs)

    def workers_status(self):
        keepers = [worker for worker in self.workers if worker.get_class_type() == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.get_class_type() == "Caretaker"]
        vets = [worker for worker in self.workers if worker.get_class_type() == "Vet"]
        return f"You have {len(self.workers)} workers"\
        + f"\n----- {len(keepers)} Keepers:\n" + "\n".join(keeper.__repr__() for keeper in keepers)\
        + f"\n----- {len(caretakers)} Caretakers:\n" + "\n".join(caretaker.__repr__() for caretaker in caretakers)\
        + f"\n----- {len(vets)} Vets:\n" + "\n".join(vet.__repr__() for vet in vets)