import pygame
from player import Player

pygame.init()

SWIDTH = 800
SHEIGHT = 600
TITLE = 'Bullet Hell'

if __name__ == '__main__':
    screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
    pygame.display.set_caption(f'{TITLE: ^{SWIDTH/3.5}}')
    clock = pygame.time.Clock()
    player = Player(400, 300)

    while True:
        keys = pygame.key.get_pressed()
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit

        # ...
        player.move(keys)

        screen.fill((0, 0, 0))  # Fill the display with a solid color

        player.draw(screen)
        # Render the graphics here.

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)
