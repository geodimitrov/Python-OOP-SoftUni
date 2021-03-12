from project.dark_wizard import DarkWizard
class SoulMaster(DarkWizard):
    def __repr__(self):
        return f"{self.username} of type {SoulMaster.__name__} has level {self.level}"