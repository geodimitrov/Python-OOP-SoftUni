from project.dark_knight import DarkKnight
class BladeKnight(DarkKnight):
    def __repr__(self):
        return f"{self.username} of type {BladeKnight.__name__} has level {self.level}"