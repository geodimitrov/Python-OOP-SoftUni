from project.player.player import Player


class BattleField:

    @staticmethod
    def get_bonus_health_points(player):
        total_bonus_health_points = sum(c.health_points for c in player.card_repository)
        player.health += total_bonus_health_points

    @staticmethod
    def check_player_type(player):
        if player.__class__.__name__ == "Beginner":
            player.health += 40
            for card in player.card_repository:
                card.damage_points += 30

    @staticmethod
    def attack(player1, player2):
        for card in player1.card_repository.cards:
            player2.health -= card.damage_points

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        BattleField.check_player_type(attacker)
        BattleField.check_player_type(enemy)
        BattleField.get_bonus_health_points(attacker)
        BattleField.get_bonus_health_points(enemy)
        while not attacker.is_dead or enemy.is_dead:
            BattleField.attack(attacker, enemy)
            BattleField.attack(enemy, attacker)
            if attacker.is_dead or enemy.is_dead:
                raise ValueError("Player is dead!")