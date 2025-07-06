import pygame
from constants import *
from player import Player

def main():
    pygame.init()
          
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = create_player()

    game_loop(player)

def create_player():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    return Player(x, y)

def game_loop(player):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
