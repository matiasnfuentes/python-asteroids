import pygame
from constants import PLAYER_SHOOT_COOLDOWN, SHOT_SPEED
from shot import Shot


class ShootingStrategy:
    def __init__(self):
        self.shot_cooldown = 0
        self.shot_speed = SHOT_SPEED

    def update(self, dt):
        self.shot_cooldown -= dt

    def shoot(self, position, rotation, shot_cooldown=PLAYER_SHOOT_COOLDOWN):
        if self.shot_cooldown > 0:
            return

        shot = Shot(position.x, position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * self.shot_speed
        self.shot_cooldown = shot_cooldown
