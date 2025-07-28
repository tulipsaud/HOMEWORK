import pygame
import sys
pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Movement")
white = (255, 255, 255)
blue = (0, 0, 255)
sprite = pygame.Rect(300, 200, 40, 40)
speed = 5

running = True
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite.x += speed
    if keys[pygame.K_UP]:
        sprite.y -= speed
    if keys[pygame.K_DOWN]:
        sprite.y += speed
    pygame.draw.rect(screen, blue, sprite)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
