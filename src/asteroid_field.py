from enum import Enum, auto
import pygame
import random
from asteroid import Asteroid
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    POWER_UP_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from power_ups.machine_gun import MachineGun
from power_ups.power_up import PowerUp
from power_ups.shield import Shield
from power_ups.speed_boost import SpeedBoost
from power_ups.triple_shot import TripleShot


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    power_ups = [Shield, SpeedBoost, TripleShot, MachineGun]

    def __init__(self, asteroids_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.asteroid_spawn_timer = 0.0
        self.power_up_spawn_timer = 0.0
        self.asteroids_group = asteroids_group

    def update_spawn_timers(self, dt):
        self.asteroid_spawn_timer += dt
        self.power_up_spawn_timer += dt

    def get_radom_position_and_velocity(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))

        return position, velocity

    def spawn(self, entity_type):
        new_entity = None
        position, velocity = self.get_radom_position_and_velocity()

        if entity_type == EntityType.ASTEROID:
            self.asteroid_spawn_timer = 0.0
            kind = random.randint(1, ASTEROID_KINDS)
            radius = ASTEROID_MIN_RADIUS * kind
            new_entity = Asteroid(position.x, position.y, radius)

        elif entity_type == EntityType.POWER_UP:
            self.power_up_spawn_timer = 0.0
            power_up = random.choice(self.power_ups)
            new_entity = power_up(position.x, position.y)

        new_entity.velocity = velocity

    def update(self, dt):
        self.update_spawn_timers(dt)

        # spawn a new asteroid at a random edge
        if self.asteroid_spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn(EntityType.ASTEROID)

        # spawn a new power-up at a random edge only if there's no power-up in the field
        if (
            self.power_up_spawn_timer > POWER_UP_SPAWN_RATE
            and PowerUp.can_spawn_power_up
        ):
            self.spawn(EntityType.POWER_UP)

    def clean_field(self):
        for asteroid in self.asteroids_group:
            asteroid.kill()


class EntityType(Enum):
    ASTEROID = auto()
    POWER_UP = auto()
