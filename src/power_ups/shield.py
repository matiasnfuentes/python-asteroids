import pygame
from constants import SHIELD_COLOR, SHIELD_WIDTH
from power_ups.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_sprite("../assets/images/shield.png")
        self.__class__.can_spawn_power_up = False

    def draw(self, screen):
        if self.player:
            pygame.draw.circle(
                screen, SHIELD_COLOR, self.position, self.radius, SHIELD_WIDTH
            )
        else:
            super().draw(screen)

    def update(self, dt):
        if self.player:
            self.position = self.player.position
        super().update(dt)
