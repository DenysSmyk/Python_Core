import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("My plane")
clock = pygame.time.Clock()

x = 700
y = 450
width = 40
height = 60
vol = 15

run = True
#clock = pygame.time.Clock()

while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 530:
        x = x - vol
    if keys[pygame.K_RIGHT] and x < 1500:
        x = x + vol
    if keys[pygame.K_UP] and y > 380:
        y = y - vol
    if keys[pygame.K_DOWN] and y < 1000:
        y = y + vol

    #without trace
    screen.fill((0, 0, 0))

    plane_surf = pygame.image.load('img/plane.png')
    plane_rect = plane_surf.get_rect(bottomright=(x, y), )
    screen.blit(plane_surf, plane_rect)

    # pygame.draw.rect(screen, (255, 0, 0), [x, y, width, height])
    pygame.display.update()
    #clock.tick(60)