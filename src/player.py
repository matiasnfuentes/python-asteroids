import sys
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
import pygame

from life import Life
from shooting_strategies.simple_shot import SimpleShot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shooting_strategy = SimpleShot()
        self.lives = [Life(10, 10), Life(40, 10), Life(70, 10)]
        self.speed = PLAYER_SPEED

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_shooting_strategy(self, shooting_strategy):
        self.shooting_strategy = shooting_strategy

    def reset_attributes(self):
        self.speed = PLAYER_SPEED
        self.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

        # Wrap position horizontally
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        # Wrap position vertically
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    def update(self, dt):
        self.shooting_strategy.update(dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
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
