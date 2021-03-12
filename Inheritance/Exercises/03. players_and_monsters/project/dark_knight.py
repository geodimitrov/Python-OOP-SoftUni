from project.knight import Knight
class DarkKnight(Knight):
    def __repr__(self):
        return f"{self.username} of type {DarkKnight.__name__} has level {self.level}"