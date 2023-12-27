import pygame
from player import Player
from bullet import Bullet

pygame.init()

S_WIDTH = 800
S_HEIGHT = 600
TITLE = 'Bullet Hell'

if __name__ == '__main__':
    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    pygame.display.set_caption(f'{TITLE: ^{S_WIDTH / 3.5}}')
    clock = pygame.time.Clock()
    player = Player(400, 300)

    bullets = []

    while True:
        keys = pygame.key.get_pressed()
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit

        m_x, m_y = pygame.mouse.get_pos()

        # TODO implement timer
        new_bullet = Bullet(player.posX + player.size / 2, player.posY + player.size / 2, m_x, m_y)
        bullets.append(new_bullet)

        player.move(keys)

        for bullet in bullets:
            bullet.move()

        # ===================================================================================== #

        bullets_to_remove = []
        for i, bullet in enumerate(bullets):
            if bullet.posX < 0 or bullet.posX > S_WIDTH:
                bullets_to_remove.append(i)

            if bullet.posY < 0 or bullet.posY > S_HEIGHT:
                bullets_to_remove.append(i)

        for i in bullets_to_remove:
            try:
                bullets.pop(i)
            except IndexError:
                continue
        # ===================================================================================== #

        screen.fill((0, 0, 0))  # Fill the display with a solid color

        for bullet in bullets:
            bullet.draw(screen)

        player.draw(screen)

        # Render the graphics here.

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)
