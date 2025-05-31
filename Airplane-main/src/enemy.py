from .entity import Entity
from .constants import DISPLAY_SIZE


class Enemy(Entity):
    def __init__(self, damage, image, coords, speed):
        super().__init__(image, coords, speed)
        self.damage = damage

    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()
