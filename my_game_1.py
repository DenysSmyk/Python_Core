# pylint: disable=C0321
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game")
# clock = pygame.time.Clock()

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (255, 0, 0), [55, 50, 80, 55])

    pygame.display.update()
# clock.tick(60)