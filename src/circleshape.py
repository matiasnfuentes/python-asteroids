import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.just_spawned = True

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        self.position += self.velocity * dt

        # Skip bounce logic while the shape is off-screen right after spawning.
        # There may be edge cases where the shape isn't fully inside the screen
        # during its lifetime and therefore doesn't bounce back inside the screen,
        # but this is acceptable.

        if self.just_spawned:
            fully_inside = (
                self.radius <= self.position.x <= SCREEN_WIDTH - self.radius
                and self.radius <= self.position.y <= SCREEN_HEIGHT - self.radius
            )
            if fully_inside:
                self.just_spawned = False
        else:
            # Bounce on horizontal borders
            if self.position.x < 0 or self.position.x > SCREEN_WIDTH:
                self.velocity.x *= -1
                self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))

            # Bounce on vertical borders
            if self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
                self.velocity.y *= -1
                self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))

    def is_colliding(self, other_shape):
        distance_between_shapes = self.position.distance_to(other_shape.position)

        if distance_between_shapes <= self.radius + other_shape.radius:
            return True

        return False
