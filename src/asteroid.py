import pygame
from circleshape import CircleShape
from constants import (
    ASTEROID_IRREGULARITY,
    ASTEROID_MIN_RADIUS,
    ASTEROID_POINT_COUNT,
    ASTEROID_WIDTH,
)
import random
from explosion import ExplosionEffect
import math


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.points = self.generate_lumpy_shape()

    def generate_lumpy_shape(self):
        angle_step = 2 * math.pi / ASTEROID_POINT_COUNT
        shape_points = []

        for i in range(ASTEROID_POINT_COUNT):
            angle = i * angle_step
            # Base distance from center is radius, varied by irregularity
            offset = random.uniform(
                1 - ASTEROID_IRREGULARITY, 1 + ASTEROID_IRREGULARITY
            )
            dist = self.radius * offset
            x = math.cos(angle) * dist
            y = math.sin(angle) * dist
            shape_points.append((x, y))

        return shape_points

    def draw(self, screen):
        # Translate relative points to screen position
        translated_points = [
            (self.position.x + x, self.position.y + y) for x, y in self.points
        ]
        pygame.draw.polygon(screen, "white", translated_points, ASTEROID_WIDTH)

    def split(self, should_explode=False):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS or should_explode:
            ExplosionEffect(self.position)
            return

        angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

    def get_mask(self):
        size = int(self.radius * 2)
        surface = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.polygon(
            surface,
            (255, 255, 255),
            [(x + self.radius, y + self.radius) for x, y in self.points],
        )
        return pygame.mask.from_surface(surface), (
            self.position.x - self.radius,
            self.position.y - self.radius,
        )

    # Pixel-perfect collision. Beautiful, right? Yeah, but super expensive...
    # This is not performant at all. I'm leaving it this way just for the fanciness,
    # but a better way to detect collisions between irregular shapes should be implemented
    # if this were a real game.

    def is_colliding(self, other_shape):
        # If the other shape has a get_mask method, use mask-based collision
        if hasattr(other_shape, "get_mask"):
            mask1, offset1 = self.get_mask()
            mask2, offset2 = other_shape.get_mask()

            offset = (int(offset2[0] - offset1[0]), int(offset2[1] - offset1[1]))
            return mask1.overlap(mask2, offset) is not None

        # Fallback: use simple circular collision
        distance_between_shapes = self.position.distance_to(other_shape.position)
        return distance_between_shapes <= self.radius + getattr(
            other_shape, "radius", 0
        )
