from power_ups.power_up import PowerUp
from shooting_strategies.simple_shot import SimpleShot


class ShootingPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.strategy = SimpleShot()

    def set_player(self, player):
        if self.player is None:
            super().set_player(player)
            player.set_shooting_strategy(self.strategy)

    def destroy(self):
        if self.player is not None:
            self.player.set_shooting_strategy(SimpleShot())
        super().destroy()
