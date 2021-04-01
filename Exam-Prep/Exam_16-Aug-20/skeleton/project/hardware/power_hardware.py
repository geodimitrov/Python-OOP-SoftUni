from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = "Power"

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.TYPE, capacity * 0.25, memory * 1.75)