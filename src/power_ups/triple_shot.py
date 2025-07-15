from power_ups.shooting_power_up import ShootingPowerUp
from shooting_strategies.triple_shot import TripleShot as TripleShotStrategy


class TripleShot(ShootingPowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.strategy = TripleShotStrategy()
        self.set_sprite("../assets/images/triple_shot.png")
