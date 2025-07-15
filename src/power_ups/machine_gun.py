from power_ups.shooting_power_up import ShootingPowerUp
from shooting_strategies.machine_gun import MachineGun as MachineGunStrategy


class MachineGun(ShootingPowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.strategy = MachineGunStrategy()
        self.set_sprite("../assets/images/machine_gun.png")
