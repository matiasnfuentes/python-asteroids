import pygame
from circleshape import CircleShape
from constants import (
    POWER_UP_SIZE,
    SHIELD_COLOR,
    SHIELD_DURATION,
    SHIELD_RADIUS,
    SHIELD_WIDTH,
)


class Shield(CircleShape):
    can_spawn_shield = True

    def __init__(self, x, y):
        super().__init__(x, y, SHIELD_RADIUS)
        self.duration = SHIELD_DURATION
        self.player = None
        self.sprite = pygame.image.load("../assets/images/shield.png").convert_alpha()
        self.sprite = pygame.transform.smoothscale(self.sprite, POWER_UP_SIZE)
        self.__class__.can_spawn_shield = False

    def draw(self, screen):
        if self.player is None:
            rect = self.sprite.get_rect(center=self.position)
            screen.blit(self.sprite, rect)
        else:
            pygame.draw.circle(
                screen, SHIELD_COLOR, self.position, self.radius, SHIELD_WIDTH
            )

    def update(self, dt):
        if self.position.x < 0 or self.position.y < 0:
            self.destroy()

        if self.player is None:
            self.position += self.velocity * dt
        elif self.duration > 0:
            self.position = self.player.position
            self.duration -= dt
        else:
            self.destroy()

    def set_player(self, player):
        self.player = player

    def destroy(self):
        self.kill()
        self.__class__.can_spawn_shield = True

    def is_protecting_player(self):
        return self.player is not None
