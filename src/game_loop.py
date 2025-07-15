import sys
import pygame

from asteroid import Asteroid
from asteroid_field import AsteroidField
from collision_detector import CollisionDetector
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from explosion import ExplosionEffect
from life import Life
from particle import Particle
from player import Player
from power_ups.power_up import PowerUp
from score import Score
from power_ups.shield import Shield
from shot import Shot


class GameLoop:
    def __init__(self):
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()

        Life.containers = self.drawable
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        Shot.containers = (self.updatable, self.drawable, self.shots)
        Player.containers = (self.updatable, self.drawable)
        Score.containers = (self.updatable, self.drawable)
        ExplosionEffect.containers = (self.updatable, self.drawable)
        Particle.containers = (self.updatable, self.drawable)
        PowerUp.containers = (self.updatable, self.drawable, self.power_ups)
        Shield.containers = (
            self.updatable,
            self.drawable,
            self.power_ups,
            self.shields,
        )

    def start_game(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField(self.asteroids)
        background = pygame.image.load("../assets/images/background.png").convert()
        score = Score(SCREEN_WIDTH - 250, 20)

        collision_detector = CollisionDetector(
            player,
            self.asteroids,
            self.shots,
            asteroid_field,
            score,
            self.power_ups,
            self.shields,
        )

        return screen, background, collision_detector, clock

    def detect_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def execute(self):
        screen, background, collision_detector, clock = self.start_game()
        dt = 0

        while True:
            self.detect_events()

            screen.blit(background, (0, 0))
            self.updatable.update(dt)

            collision_detector.detect_collisions()

            for unit in self.drawable:
                unit.draw(screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000
