from constants import SPEED_BOOST
from power_ups.power_up import PowerUp


class SpeedBoost(PowerUp):
    can_spawn_speed_power_up = True

    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_sprite("../assets/images/speed_power_up.png")

    def set_player(self, player):
        if self.player is None:
            player.set_speed(player.get_speed() * SPEED_BOOST)
            super().set_player(player)

    def destroy(self):
        if self.player is not None:
            self.player.set_speed(self.player.get_speed() / SPEED_BOOST)
        super().destroy()
