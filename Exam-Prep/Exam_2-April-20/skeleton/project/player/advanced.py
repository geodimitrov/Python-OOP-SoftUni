from project.player.player import Player


class Advanced(Player):
    INITIAL_HEALTH = 250

    def __init__(self, username):
        super().__init__(username, self.INITIAL_HEALTH)

# player = Advanced("Maya")
# print(player.__dict__)