import pygame
from constants import PLAYER_SHOOT_COOLDOWN, TRIPLE_SHOT_ROTATION
from shooting_strategies.shooting_strategy import ShootingStrategy
from shot import Shot


class TripleShot(ShootingStrategy):
    def shoot(self, position, rotation, shot_cooldown=PLAYER_SHOOT_COOLDOWN):
        if self.shot_cooldown > 0:
            return

        angles = [
            rotation,
            rotation + TRIPLE_SHOT_ROTATION,
            rotation - TRIPLE_SHOT_ROTATION,
        ]

        for angle in angles:
            shot = Shot(position.x, position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(angle) * self.shot_speed

        self.shot_cooldown = shot_cooldown
