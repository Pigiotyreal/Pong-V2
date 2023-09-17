import pygame
import sys

pygame.init()

Width = 1280
Height = 720

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pong V2")

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.display.flip()
    clock.tick(60)