import pygame
import random
import math
from pygame.time import get_ticks
from pygame import mixer
from variables import *
pygame.init()
running = True
game_active = True
# sound variable
bounce_sound = mixer.Sound('assets/Spring-Boing.wav')
ball_Sound = mixer.Sound('assets/throw_sound.wav')
win_sound = mixer.Sound('assets/yeahoo.wav')
loose_sound = mixer.Sound('assets/wii-sports-bowling-awww.wav')


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
            elif event.key == pygame.K_DOWN:
                angle -= 5
                trajectory = True
            elif event.key == pygame.K_RIGHT:
                speed += 1
                trajectory = True
            elif event.key == pygame.K_LEFT and speed >= 10:
                speed -= 1
                trajectory = True
            elif event.key == pygame.K_SPACE:
                shoot = True
                ball_Sound.play()
                time = 0  # Reset time after shooting
            text1 = my_font.render("Angle : {} ".format(angle), True, color)
            text2 = my_font.render("Speed : {}".format(speed), True, color)
    for time2 in range(0,60,3):
        if bouncetest==False:
            x_pre = (x_ini + math.cos(math.radians(angle)) * speed * time2)
            y_pre = (y_ini - (math.sin(math.radians(angle)) * speed * time2) + 0.5 * gravity * time2 ** 2)
            pygame.draw.circle(back_ground_surf,'white',(x_pre,y_pre),5)

    mouse = pygame.mouse
    if mouse.get_pressed()[0]:
        print(mouse.get_pos())
    mouse = pygame.mouse
    alpha = random.randint(0,len(positions)-1)
    if shoot == False:
        if arrow_x<=382:
            arrow_x+=1
        elif arrow_x:
            arrow_x-=1


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
            y_val = hopper_rect.topleft[1]+20 - ball_surf.get_height()+20  # Set y_val to the top of the hopper hitbox
            speed *= 0.7  # Reduce speed due to bounce
            angle = -angle  # Reverse angle (simulate bounce)
            x_ini = x_val
            y_ini = y_val
            time = 0
            print(bounce_count)
        if ball_rect.colliderect(hitbox_score_rect) and played_test==False :
            win_sound.play()
            played_test=True
            angle = 0.0
            speed = 10.0
            x_ini = player_rect.x + 70
            y_ini = player_rect.y + 90
            time = 0
            bounce_count = 0
            player_rect.midbottom = positions[alpha]
            x_val = player_rect.x + 70
            y_val = player_rect.y + 90
            shoot = False
            bouncetest = False
            played_test = False
            score += 1



        elif x_val + ball_surf.get_width() >= back_ground_surf.get_width() or bounce_count>=3:
            # Reset ball position and shoot
            loose_sound.play()
            shoot = False
            angle = 0.0
            speed = 10.0
            player_rect.midbottom = positions[alpha]
            x_ini = player_rect.x + 70
            y_ini = player_rect.y + 90
            x_val = player_rect.x + 70
            y_val = player_rect.y + 90
            time = 0
            bounce_count=0
            bouncetest=False
            played_test=False

            ball_rect.center = (player_rect.x , player_rect.y )
        time += 1  # Increment time
    text3 = my_font_1.render("{}".format(score), True, 'yellow')
    ball_rect.center = (x_val, y_val)
    if trajectory :
        back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
    screen.blit(hitbox_score_surf, hitbox_score_rect)
    screen.blit(hitbox_hooper_surf,hitbox_hopper_rect2)
    screen.blit(hitbox_hooper_surf,hitbox_hopper_rect1)
    screen.blit(back_ground_surf, back_ground_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(hopper_surf, hopper_rect)
    screen.blit(ball_surf, ball_rect)
    screen.blit(power_gauge_surf, power_gauge_rect)
    screen.blit(arrow_power_gauge_surf, arrow_power_gauge_rect)
    screen.blit(text3, (430,100))
    screen.blit(text1, (50, 510))
    screen.blit(text2, (41, 470))


    """pygame.draw.rect(screen, 'Green', hopper_rect, 5)
    pygame.draw.rect(screen, 'Red', hitbox_hopper_rect1,5)
    pygame.draw.rect(screen,'Red',hitbox_hopper_rect2,5)
    pygame.draw.rect(screen,'Yellow',hitbox_score_rect)"""
    trajectory = False
    clock.tick(60)
    pygame.display.update()
