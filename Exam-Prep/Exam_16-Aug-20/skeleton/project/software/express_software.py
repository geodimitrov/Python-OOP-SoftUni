from project.software.software import Software


class ExpressSoftware(Software):
    __TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, self.__TYPE, capacity_consumption, memory_consumption * 2)
