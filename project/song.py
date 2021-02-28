
class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} – {self.length}"

#Test Code
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())