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

paddle_speed = 2
paddle_y = Height / 2 - 50

def draw():
    global paddle_y
    screen.fill(black)
    
    #Net
    for i in range(0, Height, 25):
        pygame.draw.rect(screen, white, [Width / 2 - 2.5, i, 5, 10])
        
    #Paddles
    pygame.draw.rect(screen, white, [10, paddle_y, 10, 100])
    pygame.draw.rect(screen, white, [Width - 20, Height / 2 - 50, 10, 100])
    
    #Ball
    pygame.draw.rect(screen, white, [Width / 2 - 5, Height / 2 - 5, 10, 10])
    
    #Score
    font = pygame.font.Font("src/font.ttf", 50)
    text = font.render("0", True, white)
    screen.blit(text, (Width / 2 - 50, 10))
    text = font.render("0", True, white)
    screen.blit(text, (Width / 2 + 25, 10))
    
    #FPS
    font = pygame.font.Font("src/font.ttf", 20)
    text = font.render(str(int(clock.get_fps())), True, white)
    screen.blit(text, (10, Height - 30))
    
    pygame.display.flip()

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle_y += paddle_speed
    
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > Height - 100:
        paddle_y = Height - 100
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw()
    clock.tick(60)