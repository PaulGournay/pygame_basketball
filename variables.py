import pygame
import random
import math
from pygame.time import get_ticks
from pygame import mixer


running = True
game_active = True


clock = pygame.time.Clock()
screen = pygame.display.set_mode((950, 600))
positions = [(200, 480), (250, 480), (300, 480), (350, 480), (400, 480)]
back_ground_surf1 = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(), (950, 600))
back_ground_rect = back_ground_surf.get_rect(topleft=(0, 0))
player_surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player.png').convert_alpha(), (70, 180)), True, False)
player_rect = player_surf.get_rect(midbottom=(400, 480))
player_animation_surf = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation1.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation2.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation3.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation4.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation5.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation6.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation7.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation8.png').convert_alpha(), (70, 180)), True, False),pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player_animated/Sprite_black_player_animation9.png').convert_alpha(), (70, 180)), True, False)]
ball_surf = pygame.transform.scale(pygame.image.load('assets/basketball ball.png').convert_alpha(), (50, 50))
ball_rect = ball_surf.get_rect(center=(400, 480))
hopper_surf = pygame.transform.scale(pygame.image.load('assets/hooooooop.png').convert_alpha(), (180, 300))
hopper_rect = hopper_surf.get_rect(midbottom=(714, 480))
power_gauge_surf = pygame.image.load('assets/power_gauge.png').convert_alpha()
power_gauge_rect = power_gauge_surf.get_rect(center=(320, 520))
arrow_power_gauge_surf = pygame.transform.scale(pygame.image.load('assets/gauge_arrow.png').convert_alpha(),(40,40))
arrow_power_gauge_rect = arrow_power_gauge_surf.get_rect(center=(260, 540))
hitbox_hooper_surf = pygame.image.load('assets/hopper_hit_box.png').convert_alpha()
hitbox_hopper_rect1 = hitbox_hooper_surf.get_rect(topleft = (hopper_rect.topleft[0]+5,hopper_rect.topleft[1]+20))
hitbox_hopper_rect2 = hitbox_hooper_surf.get_rect(topleft = (hopper_rect.topleft[0]+105,hopper_rect.topleft[1]+20))
hitbox_score_surf = pygame.image.load('assets/hitbox_score.png').convert_alpha()
hitbox_score_rect = hitbox_score_surf.get_rect(topleft = (hopper_rect.topleft[0]+45,hopper_rect.topleft[1]+60))
animation_counter = 0
animation_speed = 100
# all ball values(parameters):
bounce_count = 0
x_ini = player_rect.x+70
y_ini = player_rect.y+90
x_val = x_ini
y_val = y_ini
x_pre = x_ini
y_pre = y_ini
mass = 100
time = 0
time2 = 0
time3 = 0
retention = 0.95
gravity = 0.5
shoot = False
angle = 10.0
speed = 10.0
memo_speed=speed
trajectory = False
bouncetest = False
played_test = False
#  parameters for gauge
a=1
b=-1
c=1
arrow_x = 260
arrow_y = 540
# text
color = 'black'
pygame.font.init()
score = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)
my_font_1 = pygame.font.SysFont('Comic Sans MS', 50)
score_font = pygame.font.Font('assets/font_score.TTF',50)
text_font = pygame.font.Font('assets/font_score.TTF',30)
text1 = text_font.render("Angle : {}".format(angle), True,color)
text2 = text_font.render("Speed : {}".format(speed), True,color)