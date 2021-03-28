from project.player.player import Player


class Beginner(Player):
    INITIAL_HEALTH = 50

    def __init__(self, username):
        super().__init__(username, self.INITIAL_HEALTH)

# player = Beginner("Chochko")
# # print(player.__dict__)
# print(player.__class__.__name__)