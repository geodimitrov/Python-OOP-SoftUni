class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_capacity(self):
        return sum(s.capacity_consumption for s in self.software_components)

    @property
    def used_memory(self):
        return sum(s.memory_consumption for s in self.software_components)

    @staticmethod
    def get_obj_by_name(obj_name, list_objects):
        return [obj for obj in list_objects if obj.name == obj_name][0]

    def has_enough_capacity(self, software):
        return self.capacity >= self.used_capacity + software.capacity_consumption

    def has_enough_memory(self, software):
        return self.memory >= self.used_memory + software.memory_consumption

    def install(self, software):
        if not self.has_enough_capacity(software) or not self.has_enough_memory(software):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        software_to_remove = self.get_obj_by_name(software.name, self.software_components)
        self.software_components.remove(software_to_remove)

    def get_installed_components(self, type):
        return len([s for s in self.software_components if s.type == type])

    def get_components_names_as_str(self):
        if self.software_components:
            return ", ".join(s.name for s in self.software_components)

    def __repr__(self):
        return f"Hardware Component - {self.name}\n" \
        + f"Express Software Components: {self.get_installed_components('Express')}\n" \
        + f"Light Software Components: {self.get_installed_components('Light')}\n" \
        + f"Memory Usage: {int(self.used_memory)} / {int(self.memory)}\n" \
        + f"Capacity Usage: {int(self.used_capacity)} / {int(self.capacity)}\n" \
        + f"Type: {self.type}\n" + f"Software Components: {self.get_components_names_as_str()}"
