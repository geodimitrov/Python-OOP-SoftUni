from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, self.TYPE, capacity_consumption * 1.5, memory_consumption * 0.5)