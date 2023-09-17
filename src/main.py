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

paddle_speed = 2.5
paddle_y = Height / 2 - 50
ai_paddle_y = Height / 2 - 50
ball_speed = [3, 3]
ball_rect = pygame.Rect(Width / 2 - 5, Height / 2 - 5, 10, 10)
score = [0, 0]

def ai_update():
    global ai_paddle_y
    target_y = ball_rect.centery - 50
    if abs(target_y - ai_paddle_y) > paddle_speed:
        if target_y > ai_paddle_y:
            ai_paddle_y += paddle_speed
        else:
            ai_paddle_y -= paddle_speed

    if ai_paddle_y < 0:
        ai_paddle_y = 0
    if ai_paddle_y > Height - 100:
        ai_paddle_y = Height - 100

def draw():
    global paddle_y, ball_rect, ai_paddle_y
    screen.fill(black)
    
    #Net
    for i in range(0, Height, 25):
        pygame.draw.rect(screen, white, [Width / 2 - 2.5, i, 5, 10])
        
    #Paddles
    paddle1 = pygame.draw.rect(screen, white, [10, paddle_y, 10, 100])
    paddle2 = pygame.draw.rect(screen, white, [Width - 20, ai_paddle_y, 10, 100])
    
    #Ball
    ball_rect.move_ip(ball_speed)
    if ball_rect.colliderect(paddle1) or ball_rect.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]
    elif ball_rect.left < 0:
        ball_speed[0] = -ball_speed[0]
        score[1] += 1
        ball_rect.center = (Width / 2, Height / 2)
    elif ball_rect.right > Width:
        ball_speed[0] = -ball_speed[0]
        score[0] += 1
        ball_rect.center = (Width / 2, Height / 2)
    if ball_rect.top < 0 or ball_rect.bottom > Height:
        ball_speed[1] = -ball_speed[1]
    pygame.draw.rect(screen, white, ball_rect)
    
    #Score
    font = pygame.font.Font("src/font.ttf", 50)
    text = font.render(str(score[0]), True, white)
    screen.blit(text, (Width / 2 - 50, 10))
    text = font.render(str(score[1]), True, white)
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

    ai_update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw()
    clock.tick(60)