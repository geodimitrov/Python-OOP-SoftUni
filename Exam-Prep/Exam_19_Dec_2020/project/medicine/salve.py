from project.medicine.medicine import Medicine


class Salve(Medicine):
    HEALTH_INCREASE = 50

    def __init__(self):
        super().__init__(self.HEALTH_INCREASE)

    def __str__(self):
        return "salve"