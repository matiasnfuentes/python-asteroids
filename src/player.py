import sys
from circleshape import CircleShape
from constants import (
    ASTEROID_FIELD_FRICTION,
    PLAYER_ACCELERATION,
    PLAYER_MAX_SPEED,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
import pygame

from direction import Direction
from life import Life
from shooting_strategies.simple_shot import SimpleShot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = PLAYER_ACCELERATION
        self.max_speed = PLAYER_MAX_SPEED
        self.shooting_strategy = SimpleShot()
        self.lives = [Life(10, 10), Life(40, 10), Life(70, 10)]

    def set_shooting_strategy(self, shooting_strategy):
        self.shooting_strategy = shooting_strategy

    def reset_attributes(self):
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, direction: Direction):
        if direction:
            direction_vector = pygame.Vector2(0, 1).rotate(self.rotation)
            self.velocity += direction_vector * self.acceleration * direction.value * dt

        # Apply friction slowing down the starship
        self.velocity *= ASTEROID_FIELD_FRICTION

        if self.velocity.length() > self.max_speed:
            self.velocity = self.velocity.normalize() * self.max_speed

        self.position += self.velocity * dt

        # Wrap around screen horizontally
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        # Wrap around screen vertically
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    def update(self, dt):
        self.shooting_strategy.update(dt)
        keys = pygame.key.get_pressed()
        direction = None

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            direction = Direction.FORWARDS
        if keys[pygame.K_s]:
            direction = Direction.BACKWARDS

        self.move(dt, direction)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        self.shooting_strategy.shoot(self.position, self.rotation)

    def lose_life(self):
        if len(self.lives) <= 1:
            print("Game over!")
            sys.exit()

        self.reset_attributes()
        self.lives.pop().kill()

    def get_mask(self):
        size = int(self.radius * 2)
        surface = pygame.Surface((size, size), pygame.SRCALPHA)

        # Get world-space triangle points
        world_points = self.triangle()

        # Convert points to local surface coordinates
        local_points = [
            (
                point.x - (self.position.x - self.radius),
                point.y - (self.position.y - self.radius),
            )
            for point in world_points
        ]

        # Draw triangle to surface
        pygame.draw.polygon(surface, (255, 255, 255), local_points)

        mask = pygame.mask.from_surface(surface)

        return mask, (self.position.x - self.radius, self.position.y - self.radius)
