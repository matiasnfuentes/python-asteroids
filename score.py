import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.Font(None, 36)
        self.position = pygame.Vector2(x, y)
        self.score = 0
        self.set_text_surface()

    def draw(self, screen):
        screen.blit(self.text_surface, self.position)

    def update(self, _):
        self.set_text_surface()

    def increase(self):
        self.score += 1

    def set_text_surface(self):
        self.text_surface = self.font.render(
            f"Current score: {self.score}", True, (255, 255, 255)
        )
