import pygame

pygame.init()

SWIDTH = 800
SHEIGHT = 600
TITLE = 'Bullet Hell'

if __name__ == '__main__':
    screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
    pygame.display.set_caption(f'{TITLE: ^100}')
    clock = pygame.time.Clock()

    while True:
        keys = pygame.key.get_pressed()
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit



        # Do logical updates here.
        # ...

        screen.fill("purple")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)