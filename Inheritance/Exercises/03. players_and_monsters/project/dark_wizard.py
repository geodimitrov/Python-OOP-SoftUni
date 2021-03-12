from project.wizard import Wizard
class DarkWizard(Wizard):
    def __repr__(self):
        return f"{self.username} of type {DarkWizard.__name__} has level {self.level}"