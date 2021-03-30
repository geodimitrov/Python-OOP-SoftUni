from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.medicine.painkiller import Painkiller
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []  # survivor objects
        self.supplies = []  # supply objects
        self.medicine = []  # medicine objects
    
    @property
    def food(self):
        food_objects = [item for item in self.supplies if item.__class__.__name__ == "FoodSupply"]
        if not food_objects:
            raise IndexError("There are no food supplies left!")
        return food_objects

    @property
    def water(self):
        water_objects = [item for item in self.supplies if item.__class__.__name__ == "WaterSupply"]
        if not water_objects:
            raise IndexError("There are no water supplies left!")
        return water_objects

    @property
    def painkillers(self):
        painkillers = [item for item in self.medicine if item.__class__.__name__ == "Painkiller"]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers
    
    @property
    def salves(self):
        salves = [item for item in self.medicine if item.__class__.__name__ == "Salve"]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def get_medicine(self, medicine_type):
        for medicine in reversed(self.medicine):
            if medicine.__class__.__name__ == medicine_type:
                self.medicine.remove(medicine)
                return medicine

    def get_sustenance(self, sustenance_type):
        for supply in reversed(self.supplies):
            if supply.__class__.__name__ == sustenance_type:
                self.supplies.remove(supply)
                return supply

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            medicine_to_apply = self.get_medicine(medicine_type)
            medicine_to_apply.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type):
        if survivor.needs_sustenance:
            sustenance_to_apply = self.get_sustenance(sustenance_type)
            sustenance_to_apply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def reduce_survivors_needs(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

    def sustain_survivors(self):
        for survivor in self.survivors:
            self.sustain(survivor, "WaterSupply")
            self.sustain(survivor, "FoodSupply")

    def next_day(self):
        self.reduce_survivors_needs()
        self.sustain_survivors()