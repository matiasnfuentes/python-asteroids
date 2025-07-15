import pygame
from circleshape import CircleShape
from constants import (
    POWER_UP_RADIUS,
    POWER_UP_SIZE,
    POWER_UP_DURATION,
)


class PowerUp(CircleShape):
    can_spawn_power_up = True

    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.duration = POWER_UP_DURATION
        self.player = None
        PowerUp.can_spawn_power_up = False

    def set_sprite(self, sprite_route):
        self.sprite = pygame.image.load(sprite_route).convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, POWER_UP_SIZE)

    def draw(self, screen):
        if self.player is None:
            screen.blit(self.sprite, self.sprite.get_rect(center=self.position))

    def update(self, dt, update_with_player=None):
        if self.position.x < 0 or self.position.y < 0:
            self.destroy()
            return

        if self.player is None:
            self.position += self.velocity * dt
            return

        if self.duration > 0:
            self.duration -= dt
        else:
            self.destroy()

    def set_player(self, player):
        self.player = player

    def destroy(self):
        self.kill()
        PowerUp.can_spawn_power_up = True

    def is_powering_up_player(self):
        return self.player is not None
