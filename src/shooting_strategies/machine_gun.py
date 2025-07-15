from constants import MACHINEGUN_SHOOT_COOLDOWN_BOOST, PLAYER_SHOOT_COOLDOWN
from shooting_strategies.shooting_strategy import ShootingStrategy


class MachineGun(ShootingStrategy):
    def __init__(self):
        super().__init__()

    def shoot(self, position, rotation):
        super().shoot(
            position, rotation, PLAYER_SHOOT_COOLDOWN * MACHINEGUN_SHOOT_COOLDOWN_BOOST
        )
