import pygame
import random

from constants import EXPLOSION_PARTICLE_DURATION


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.radius = random.randint(1, 4)
        self.age = 0

    def update(self, dt):
        self.age += dt
        self.pos[0] += self.velocity[0] * dt / 10
        self.pos[1] += self.velocity[1] * dt / 10

    def draw(self, screen):
        if self.is_alive():
            alpha = max(0, 255 * (1 - self.age / EXPLOSION_PARTICLE_DURATION))
            surface = pygame.Surface(
                (self.radius * 2, self.radius * 2), pygame.SRCALPHA
            )
            pygame.draw.circle(
                surface,
                (255, 255, 255, int(alpha)),
                (self.radius, self.radius),
                self.radius,
            )
            screen.blit(surface, (self.pos[0] - self.radius, self.pos[1] - self.radius))
        else:
            self.kill()

    def is_alive(self):
        return self.age < EXPLOSION_PARTICLE_DURATION
