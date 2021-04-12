from project.decoration.base_decoration import BaseDecoration

class Plant(BaseDecoration):
    default_comfort = 5
    default_price = 10.0

    def __init__(self):
        super().__init__(self.default_comfort, self.default_price)