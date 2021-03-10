class Guild:
    players = []

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in Guild.players:
            Guild.players.append(player)
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        else:
            if player not in self.players:
                return f"Player {player.name} is in another guild."
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        player = [player for player in self.players if player.name == player_name]
        if not player:
            return f"Player {player_name} is not in the guild."
        player.guild = "Unaffiliated"
        self.players.remove(player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join(player.player_info() for player in self.players)


# Test code
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())