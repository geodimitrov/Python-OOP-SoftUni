class DecorationRepository:
    def __init__(self):
        self.decorations = []

    @staticmethod
    def get_obj_by_type(objects, obj_type):
        result = [obj for obj in objects if obj.__class__.__name__ == obj_type]
        return result

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        decorations = self.get_obj_by_type(self.decorations,decoration_type)
        if decorations:
            return decorations[0]
        return "None"