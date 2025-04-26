from random import randint

import pygame

from src.constants import MAX_FPS, DISPLAY_SIZE, SHOOT_EVENT, SPAWN_EVENT
from src.player import Player
from src.enemy import Enemy
from src.bullet import Bullet

def game(display, clock):
    coords = DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] - 50
    image = pygame.Surface((50, 50))
    image.fill( (255, 0, 0,) )
    player = Player(image, coords, 4, 100)

    bullet_image = pygame.Surface([20, 20])
    bullet_image.fill('green')
    bullets = list()

    enemy_image = pygame.Surface((50, 50))
    enemy_image.fill("red")
    enemies = list()

    difficulty = 0
    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)


    
    

    while True:

        difficulty += clock.get_time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                b = Bullet(
                    bullet_image,
                    player.rect.midtop,
                    10
                )
                bullets.append(b) 
            elif event.type == SPAWN_EVENT:
                millis = round(2000 - difficulty / 70)
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)
                e = Enemy(
                    round(10 + difficulty / 7000),
                    enemy_image,
                    [randint(50, DISPLAY_SIZE[0] - 50), 
                    -enemy_image.height],
                    5 + difficulty / 35000
                )
                enemies.append(e)

                
        player.update()
        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for i in enemies.copy():
            i.update()
            if not i.alive:
                enemies.remove(i)




        display.fill( (0, 0, 0) )
    
        player.render(display)
        for a in bullets:
            a.render(display)
            player.render(display)
        for a in enemies:
            a.render(display)
        

        
        
            
        pygame.display.update()
        clock.tick(MAX_FPS)




def main():
    pygame.init()

    display = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption('Shooter')
    clock = pygame.time.Clock()

    while True:
        game(display, clock)

if __name__ == '__main__':
    main()



