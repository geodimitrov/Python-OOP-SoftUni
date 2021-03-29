from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller

class Bunker:
    def __init__(self):
        self.survivors = []  # survivor objects
        self.supplies = []  # supply objects
        self.medicine = []
    
    @property
    def food(self):
        food_objects = [item for item in self.supplies if isinstance(item, FoodSupply)]
        if not food_objects:
            raise IndexError("There are no food supplies left!")
        return food_objects

    @property
    def water(self):
        water_objects = [item for item in self.supplies if isinstance(item, WaterSupply)]
        if not water_objects:
            raise IndexError("There are no water supplies left!")
        return water_objects

    @property
    def painkillers(self):
        painkillers = [item for item in self.supplies if isinstance(item, Painkiller)]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers
    
    @property
    def salves(self):
        salves = [item for item in self.supplies if isinstance(item, Salve)]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor.name in [s.name for s in self.survivors]:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    @staticmethod
    def get_obj_to_apply_and_to_remove(obj_type, obj_list):
        for obj in reversed(obj_list):
            if obj.__class__.__name__ == obj_type:
                return obj_list.pop(obj_list.index(obj))

    def heal(self, survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine_to_apply = self.get_obj_to_apply_and_to_remove(medicine_type, self.medicine)
            survivor.health += medicine_to_apply.health_increase
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance_to_apply = self.get_obj_to_apply_and_to_remove(sustenance_type, self.supplies)
            survivor.needs += sustenance_to_apply.needs_increase
            return f"{survivor.name} healed successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")