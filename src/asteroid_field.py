from enum import Enum, auto
import pygame
import random
from asteroid import Asteroid
from constants import *
from shield import Shield


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

    def __init__(self, asteroids_group):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.asteroid_spawn_timer = 0.0
        self.shield_spawn_timer = 0.0
        self.asteroids_group = asteroids_group

    def spawn(self, entity_type, position, velocity, radius=1):
        new_entity = None

        if entity_type == EntityType.ASTEROID:
            new_entity = Asteroid(position.x, position.y, radius)
        elif entity_type == EntityType.SHIELD:
            new_entity = Shield(position.x, position.y)

        new_entity.velocity = velocity

    def update_spawn_timers(self, dt):
        self.asteroid_spawn_timer += dt
        self.shield_spawn_timer += dt

    def get_radom_position_and_velocity(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        return position, velocity

    def update(self, dt):
        self.update_spawn_timers(dt)

        # spawn a new asteroid at a random edge
        if self.asteroid_spawn_timer > ASTEROID_SPAWN_RATE:
            self.asteroid_spawn_timer = 0.0
            position, velocity = self.get_radom_position_and_velocity()
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(
                EntityType.ASTEROID,
                position,
                velocity,
                ASTEROID_MIN_RADIUS * kind,
            )

        # spawn a new shield at a random edge only if there's no shield in the field
        if self.shield_spawn_timer > 1 and Shield.can_spawn_shield:
            self.shield_spawn_timer = 0.0
            position, velocity = self.get_radom_position_and_velocity()
            self.spawn(EntityType.SHIELD, position, velocity)

    def clean_field(self):
        for asteroid in self.asteroids_group:
            asteroid.kill()


class EntityType(Enum):
    ASTEROID = auto()
    SHIELD = auto()
