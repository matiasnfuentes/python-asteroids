import pygame
import random
import math

from particle import Particle


class ExplosionEffect(pygame.sprite.Sprite):
    def __init__(self, pos):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.particles = []

        for _ in range(30):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(100, 300)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append(Particle(pos, (vx, vy)))

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)

    def update(self, _):
        if all(not p.is_alive() for p in self.particles):
            self.kill()
