import pygame


# Переменные для окна
MAX_FPS = 60
DISPLAY_SIZE = 800, 600

# События
SHOOT_EVENT = pygame.event.custom_type()
SPAWN_EVENT = pygame.event.custom_type()

# Переменные игрока
HEALTH_BAR_WIDTH = 150
PLAYER_HEALTH = 100
PLAYER_SPEED = 7.5

# Переменные врага
ENEMY_DAMAGE = 10
ENEMY_SPEED = 5

# Переменные пули
BULLET_SPPED = 10
