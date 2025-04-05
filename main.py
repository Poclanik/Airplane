import pygame

from src.constants import MAX_FPS, DISPLAY_SIZE

def game(display, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
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

