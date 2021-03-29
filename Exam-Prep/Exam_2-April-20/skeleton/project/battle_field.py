from project.player.beginner import Beginner


class BattleField:
    @staticmethod
    def validate_player(player):
        if player.is_dead:
            raise ValueError("Player is dead!")

    @staticmethod
    def check_player_type(player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30

    @staticmethod
    def deal_damage(player1, player2):
        for card in player1.card_repository.cards:
            if player2.is_dead:
                return
            player2.take_damage(card.damage_points)

    @staticmethod
    def attack(attacker, enemy):
        BattleField.deal_damage(attacker, enemy)
        if enemy.is_dead:
            return
        BattleField.deal_damage(enemy, attacker)
        if attacker.is_dead:
            return

    def fight(self, attacker, enemy):
        self.validate_player(attacker)
        self.validate_player(enemy)
        self.check_player_type(attacker)
        self.check_player_type(enemy)
        attacker.add_bonus_health_points()
        enemy.add_bonus_health_points()
        self.attack(attacker, enemy)