from random import randint
import pygame

from src.constants import (
    MAX_FPS,
    DISPLAY_SIZE,
    SHOOT_EVENT,
    SPAWN_EVENT,
    HEALTH_BAR_WIDTH,
    PLAYER_HEALTH,
    PLAYER_SPEED,
    ENEMY_DAMAGE,
    ENEMY_SPEED,
    BULLET_SPPED,
)
from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy
from src.utils import laod_image, get_path


def game(display, clock):
    asteroid_image = laod_image("assets", "images", "bomb.webp", size=[164, 164])
    background_image = laod_image(
        "assets", "images", "pole.jpg", size=DISPLAY_SIZE
    )
    player_image = laod_image("assets", "images", "player.jpg", size=[96, 96])
    shot_image = laod_image("assets", "images", "shot.png", size=[64, 64])

    shot_sound = pygame.Sound(get_path("assets", "sounds", "shot.wav"))
    death_sound = pygame.Sound(get_path("assets", "sounds", "death.wav"))
    explosion_sound = pygame.Sound(get_path("assets", "sounds", "explosion.wav"))

    # Изменить громкость звука:
    # shot_sound.set_volume(0.5)

    coords = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    player = Player(player_image, coords, PLAYER_SPEED, PLAYER_HEALTH)

    bullets = list()
    enemies = list()

    difficulty = 0
    score = 0
    font = pygame.Font(get_path("assets", "fonts", "pixel.ttf"), 24)
    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)

    while player.health > 0:
        difficulty += clock.get_time()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == SHOOT_EVENT:
                shot_sound.play()
                b = Bullet(shot_image, player.rect.midtop, BULLET_SPPED)
                bullets.append(b)

            elif event.type == SPAWN_EVENT:
                millis = max(750, round(2000 - difficulty / 70))
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)

                new_image = pygame.transform.rotozoom(
                    asteroid_image,
                    randint(0, 360),
                    1 + randint(-10, 10) / 100,
                )

                e = Enemy(
                    round(ENEMY_DAMAGE + difficulty / 7_000),
                    new_image,
                    [randint(50, DISPLAY_SIZE[0] - 50), -new_image.height],
                    ENEMY_SPEED + difficulty / 35_000,
                )
                enemies.append(e)

        # Обновление игровых объектов
        player.update()

        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for i in enemies.copy():
            i.update()
            if not i.alive:
                enemies.remove(i)

        for b in bullets:
            for e in enemies:
                if b.collide_entity(e):
                    explosion_sound.play()
                    b.kill()
                    e.kill()
                    score += 1
                if b.collide_entity(e):
                    explosion_sound.play()
                    player.speed = max(player.speed * 0.95, 3.5 )


        for e in enemies:
            if e.collide_entity(player):
                death_sound.play()
                player.get_damage(e.damage)
                e.kill()

        # Обновление экрана
        display.fill("black")
        display.blit(background_image, (0, 0))

        player.render(display)
        for u in bullets:
            u.render(display)
        for u in enemies:
            u.render(display)

        #                             цвет      x   y        ширина      высота
        pygame.draw.rect(display, (100, 0, 0), [10, 10, HEALTH_BAR_WIDTH, 20])
        width = int(player.health / PLAYER_HEALTH * HEALTH_BAR_WIDTH)
        pygame.draw.rect(display, (255, 0, 0), [10, 10, width, 20])
        pygame.draw.rect(display, (175, 0, 0), [8, 8, HEALTH_BAR_WIDTH + 4, 24], 2)

        image_score = font.render(str(score), True, (50, 200, 50))
        rect_score = image_score.get_rect(midtop = [DISPLAY_SIZE[0]/2, 10])

        display.blit(image_score, rect_score)

        pygame.display.update()
        clock.tick(MAX_FPS)


def show_lose(display, clock):
    running = True

    font = pygame.Font(get_path("assets", "fonts", "pixel.ttf"), 64)
    text = font.render("YOU LOSE!", True, (255, 50, 50))
    display.blit(text, text.get_rect(center=[DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False

        clock.tick(MAX_FPS)


def main():
    pygame.init()

    display = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption("Shooter")
    clock = pygame.time.Clock()

    pygame.mixer.music.load(get_path("assets", "music", "background-1.mp3"))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while True:
        game(display, clock)
        show_lose(display, clock)


if __name__ == "__main__":
    main()
