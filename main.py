import pygame
import random

pygame.init()
running = True
game_active = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode((950,600))
positions=[(200,480),(250,480),(300,480),(350,480),(400,480)]
back_ground_surf = pygame.transform.scale(pygame.image.load('assets/basketball court.png').convert_alpha(),(950,600 ))
back_ground_rect = back_ground_surf.get_rect(topleft=(0,0))

player_surf = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/Sprite_black_player.png').convert_alpha(),(70,180)),True,False)
player_rect = player_surf.get_rect(midbottom = (400,480))
ball_surf = pygame.image.load('assets/basketball ball.png').convert_alpha()
ball_rect = ball_surf.get_rect(center = player_rect.center)
hopper_surf = pygame.transform.scale(pygame.image.load('assets/hooooooop.png').convert_alpha(),(180,300))
hopper_rect = hopper_surf.get_rect(midbottom = (720, 480))

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)
            player_rect.x += 1
            if player_rect.collidepoint(mouse_pos):
                screen.blit(ball_surf,ball_rect)

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(back_ground_surf,back_ground_rect)
    screen.blit(player_surf,player_rect)
    screen.blit(hopper_surf, hopper_rect)
    pygame.draw.rect(screen,'Blue',player_rect,5)
    pygame.draw.rect(screen,'Green',hopper_rect,5)
    clock.tick(60)
    """if pygame.mouse.get_pressed()[0]:
        player_rect.x += 1"""
    pygame.display.update()