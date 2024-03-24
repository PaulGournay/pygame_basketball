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
back_ground_surf1 = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
back_ground_rect = back_ground_surf.get_rect(topleft=(0, 0))
arrow_surf = pygame.image.load('assets/arrow.png').convert_alpha()
arrow_surf2 = pygame.transform.scale_by(arrow_surf, 1.5)
arrow_rect = arrow_surf.get_rect(midbottom=(470, 400))
player_surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player.png').convert_alpha(), (70, 180)), True, False)
player_rect = player_surf.get_rect(midbottom=(400, 480))
ball_surf = pygame.transform.scale(pygame.image.load('assets/basketball ball.png').convert_alpha(), (50, 50))
ball_rect = ball_surf.get_rect(center=(400, 480))
hitbox1_surf = pygame.image.load('assets/hitbox1.png').convert_alpha()
hitbox1_rect = hitbox1_surf.get_rect(center=(720, 480))
hitbox2_surf = pygame.image.load('assets/hitbox2.png').convert_alpha()
hitbox2_rect = hitbox1_surf.get_rect(center=(720, 500))


hopper_surf = pygame.transform.scale(pygame.image.load('assets/hooooooop.png').convert_alpha(), (180, 300))
hopper_rect = hopper_surf.get_rect(midbottom=(720, 480))
bounce_sound = mixer.Sound('assets/Spring-Boing.wav')
ball_Sound = mixer.Sound('assets/throw_sound.wav')
hitbox_hooper_surf = pygame.image.load('assets/hopper_hit_box.png').convert_alpha()
hitbox_hopper_rect1 = hitbox_hooper_surf.get_rect(topleft = (hopper_rect.topleft[0]+5,hopper_rect.topleft[1]+20))
hitbox_hopper_rect2 = hitbox_hooper_surf.get_rect(topleft = (hopper_rect.topleft[0]+105,hopper_rect.topleft[1]+20))
hitbox_score_surf = pygame.image.load('assets/hitbox_score.png').convert_alpha()
hitbox_score_rect = hitbox_score_surf.get_rect(topleft = (hopper_rect.topleft[0]+45,hopper_rect.topleft[1]+35))
# all ball values(parameters):
bounce_count = 0
x_ini = player_rect.x+30
y_ini = player_rect.y+50
x_val = x_ini
y_val = y_ini
x_pre = x_ini-30
y_pre = y_ini
mass = 100
time = 0
time2 = 0
retention = 0.95
gravity = 0.5
shoot = False
angle = 10.0
speed = 10.0
trajectory = False
bouncetest=False

# text
color = 'black'
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = my_font.render("Angle : {}".format(angle), True,color)
text2 = my_font.render("Speed : {}".format(speed), True,color)
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and not shoot:
            if event.key == pygame.K_UP:
                angle += 5
                trajectory = True
                print(angle)
            elif event.key == pygame.K_DOWN:
                angle -= 5
                trajectory = True
                print(angle)
            elif event.key == pygame.K_RIGHT:
                speed += 1
                trajectory = True
                print(speed)
            elif event.key == pygame.K_LEFT and speed >= 10:
                speed -= 1
                trajectory = True
                print(speed)
            elif event.key == pygame.K_SPACE:
                shoot = True
                ball_Sound.play()
                time = 0  # Reset time after shooting
            text1 = my_font.render("Angle : {} ".format(angle), True, color)
            text2 = my_font.render("Speed : {}".format(speed), True, color)
    for time2 in range(0,60,3):
        if bouncetest==False:
            x_pre = (x_ini+40 + math.cos(math.radians(angle)) * speed * time2)
            y_pre = (y_ini+40 - (math.sin(math.radians(angle)) * speed * time2) + 0.5 * gravity * time2 ** 2)
            pygame.draw.circle(back_ground_surf,'white',(x_pre,y_pre),5)

    mouse = pygame.mouse
    if mouse.get_pressed()[0]:
        print(mouse.get_pos())


    if shoot == True:
        # Calculate location
        x_val = (x_ini + math.cos(math.radians(angle)) * speed * time)
        y_val = (y_ini - (math.sin(math.radians(angle)) * speed * time) + 0.5 * gravity * time ** 2)

        if y_val + ball_surf.get_height() >= back_ground_surf.get_height()+10:
            # Implement bounce
            bounce_sound.play()
            bouncetest=True
            bounce_count+=1
            y_val = back_ground_surf.get_height() - ball_surf.get_height()
            speed *= retention  # Reduce speed due to bounce
            angle = -angle  # Reverse angle (simulate bounce)
            x_ini = x_val
            y_ini = y_val
            time = 0
            print(bounce_count)
        if ball_rect.colliderect(hitbox_hopper_rect1) or ball_rect.colliderect(hitbox_hopper_rect2):
            # Implement bounce or any other action
            bounce_sound.play()
            bouncetest=True
            bounce_count += 1
            y_val = hopper_rect.top - ball_surf.get_height()-30  # Set y_val to the top of the hopper hitbox
            speed *= 0.7  # Reduce speed due to bounce
            angle = -angle  # Reverse angle (simulate bounce)
            x_ini = x_val
            y_ini = y_val
            time = 0
            print(bounce_count)


        elif x_val + ball_surf.get_width() >= back_ground_surf.get_width() or bounce_count>=3:
            # Reset ball position and shoot
            x_val = player_rect.x + 30
            y_val = player_rect.y + 50
            shoot = False
            bounce_count+=1

            # Reset other parameters
            angle = 0.0
            speed = 10.0
            x_ini = player_rect.x + 30
            y_ini = player_rect.y + 50
            time = 0
            bounce_count=0
            bouncetest=False
        time += 1  # Increment time

    ball_rect.center = (x_val, y_val)
    if trajectory :
        back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
    screen.blit(hitbox1_surf, hitbox1_rect)
    screen.blit(hitbox_score_surf, hitbox_score_rect)
    screen.blit(hitbox_hooper_surf,hitbox_hopper_rect2)
    screen.blit(hitbox_hooper_surf,hitbox_hopper_rect1)
    screen.blit(back_ground_surf, back_ground_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(hopper_surf, hopper_rect)
    screen.blit(ball_surf, ball_rect)


    screen.blit(text1, (50, 510))
    screen.blit(text2, (41, 470))

    pygame.draw.rect(screen, 'Blue', hitbox1_rect, 5)
    pygame.draw.rect(screen, 'Green', hopper_rect, 5)

    pygame.draw.rect(screen, 'Red', hitbox_hopper_rect1,5)
    pygame.draw.rect(screen,'Red',hitbox_hopper_rect2,5)
    pygame.draw.rect(screen,'Yellow',hitbox_score_rect)
    trajectory = False
    clock.tick(60)
    pygame.display.update()
