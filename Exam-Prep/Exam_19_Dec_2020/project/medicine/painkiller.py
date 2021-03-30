from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    HEALTH_INCREASE = 20

    def __init__(self):
        super().__init__(self.HEALTH_INCREASE)

    def __str__(self):
        return "painkiller"