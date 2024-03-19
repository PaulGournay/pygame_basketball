import pygame
import random
import math
from pygame.time import get_ticks
from pygame import mixer
pygame.init()
running = True
game_active = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode((950, 600))
positions = [(200, 480), (250, 480), (300, 480), (350, 480), (400, 480)]
back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
back_ground_rect = back_ground_surf.get_rect(topleft=(0, 0))
arrow_surf = pygame.image.load('assets/arrow.png').convert_alpha()
arrow_surf2 = pygame.transform.scale_by(arrow_surf, 1.5)
arrow_rect = arrow_surf.get_rect(midbottom=(470, 400))
player_surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player.png').convert_alpha(), (70, 180)), True, False)
player_rect = player_surf.get_rect(midbottom=(400, 480))
ball_surf = pygame.transform.scale(pygame.image.load('assets/basketball ball.png').convert_alpha(), (80, 80))
ball_rect = ball_surf.get_rect(midbottom=(400, 480))
hopper_surf = pygame.transform.scale(pygame.image.load('assets/hooooooop.png').convert_alpha(), (180, 300))
hopper_rect = hopper_surf.get_rect(midbottom=(720, 480))

# all ball values(parameters):
x_ini = player_rect.x+30
y_ini = player_rect.y+50
x_val=x_ini
y_val=y_ini
x_pre= x_ini
y_pre=y_ini
mass = 100
time=0
retention = 0.95
gravity = 0.5
shoot = False
angle = 0.0
speed = 10.0

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and not shoot:
            if event.key == pygame.K_UP:
                angle += 10
                print(angle)
            elif event.key == pygame.K_DOWN:
                angle -= 10
                print(angle)
            elif event.key == pygame.K_RIGHT:
                speed += 1
                print(speed)
            elif event.key == pygame.K_LEFT and speed >= 10:
                speed -= 1
                print(speed)
            elif event.key == pygame.K_SPACE:
                shoot = True
                ball_Sound = mixer.Sound('assets/throw_sound.wav')
                ball_Sound.play()
                time = 0  # Reset time after shooting
    """for time in range(0,30,5):
        x_pre = (x_ini + math.cos(math.radians(angle)) * speed * time)
        y_pre = (y_ini - (math.sin(math.radians(angle)) * speed * time) + 0.5 * gravity * time ** 2)
        pygame.draw.circle(back_ground_surf,'white',(x_pre,y_pre),5)"""

    if shoot == True:
        # Calculate location
        x_val = (x_ini + math.cos(math.radians(angle)) * speed * time)
        y_val = (y_ini - (math.sin(math.radians(angle)) * speed * time) + 0.5 * gravity * time ** 2)

        if y_val + ball_surf.get_height() >= back_ground_surf.get_height() + 30:
            # Implement bounce
            y_val = back_ground_surf.get_height() - ball_surf.get_height()
            speed *= retention  # Reduce speed due to bounce
            angle = -angle  # Reverse angle (simulate bounce)
            x_ini = x_val
            y_ini = y_val
            time = 0
        elif x_val + ball_surf.get_width() >= back_ground_surf.get_width():
            # Reset ball position and shoot
            x_val = player_rect.x + 30
            y_val = player_rect.y + 50
            shoot = False

            # Reset other parameters
            angle = 0.0
            speed = 10.0
            x_ini = player_rect.x + 30
            y_ini = player_rect.y + 50
            time = 0

        time += 1  # Increment time

    screen.blit(back_ground_surf, back_ground_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(hopper_surf, hopper_rect)
    screen.blit(arrow_surf, arrow_rect)
    screen.blit(ball_surf, (x_val, y_val))
    pygame.draw.rect(screen, 'Blue', player_rect, 5)
    pygame.draw.rect(screen, 'Green', hopper_rect, 5)
    clock.tick(60)
    pygame.display.update()
