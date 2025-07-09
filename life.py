import pygame


class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        original_image = pygame.image.load("./heart.png")
        self.image = pygame.transform.scale(original_image, (40, 40)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
