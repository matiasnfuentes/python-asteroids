import sys
import pygame
from asteroid import Asteroid
from asteroid_field import AsteroidField
from collision_detector import CollisionDetector
from constants import *
from explosion import ExplosionEffect, Particle
from life import Life
from player import Player
from score import Score
from shield import Shield
from shot import Shot


def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable, drawable, asteroids, shots, shields = create_containers()
    game_loop(updatable, drawable, asteroids, shots, shields)


def create_containers():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shields = pygame.sprite.Group()

    Life.containers = (drawable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Score.containers = (updatable, drawable)
    ExplosionEffect.containers = (updatable, drawable)
    Particle.containers = (updatable, drawable)
    Shield.containers = (updatable, drawable, shields)

    return updatable, drawable, asteroids, shots, shields


def game_loop(updatable, drawable, asteroids, shots, shields):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField(asteroids)
    background = pygame.image.load("../assets/images/background.png").convert()
    score = Score(SCREEN_WIDTH - 250, 20)

    collision_detector = CollisionDetector(
        player, asteroids, shots, asteroid_field, score, shields
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background, (0, 0))
        updatable.update(dt)
        collision_detector.detect_collisions()

        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
