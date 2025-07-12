import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_WIDTH
import random

from explosion import ExplosionEffect


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            ExplosionEffect(self.position)
            return

        angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2
