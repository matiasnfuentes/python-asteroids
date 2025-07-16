from constants import SPEED_BOOST
from power_ups.power_up import PowerUp


class SpeedBoost(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_sprite("../assets/images/speed_power_up.png")

    def set_player(self, player):
        if self.player is None:
            super().set_player(player)
            self.boost_player_values(True)

    def destroy(self):
        if self.player is not None:
            self.boost_player_values(False)
        super().destroy()

    def boost_player_values(self, boost: bool):
        factor = SPEED_BOOST if boost else 1 / SPEED_BOOST
        self.player.max_speed *= factor
        self.player.acceleration *= factor
