class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        player = [p for p in self.players if p.name == player_name]
        if player:
            return f"Player {player[0].name} has been removed from the guild."
        return f"Player {player[0].name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join([p.player_info() for p in self.players])

#Test Code
# player = Player("George", 50, 100)
# player_2 = Player("Peter", 60, 80)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.assign_player(player_2))
# print(guild.guild_info())