import pygame

from .entity import Entity
from .constants import constants



class Player(Entity):
    def __init__(self, image, coords, speed, health):
        super().__init__(image, coords, speed)
        self.health = health

    def get_damage(self, value):
        self.health -= value

        if self.health <= 0:
            self.kill()
            self.health = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        left = pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]
        right = pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]

        if left != right:
            if left:
                self.move(-self.speed, 0 )
            else:
                self.move(self.speed, 0 )

        just_pressed_keys = pygame.key.get_just_pressed()
        if just_pressed_keys[pygame.k_SPACE]:
            pygame.event.post(pygame.event())
