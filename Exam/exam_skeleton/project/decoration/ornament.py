from project.decoration.base_decoration import BaseDecoration

class Ornament(BaseDecoration):
    default_comfort = 1
    default_price = 5.0

    def __init__(self):
        super().__init__(self.default_comfort, self.default_price)