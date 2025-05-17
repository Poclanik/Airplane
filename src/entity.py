import pygame


class Entity:
    def __init__(self, image, coords, speed):
        self.image = image.copy()
        self.rect = self.image.get_rect(center=coords)
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def kill(self):
        self.alive = False

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def collide_entity(self, other):
        return pygame.sprite.collide_mask(self, other)
