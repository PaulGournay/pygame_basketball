import pygame

pygame.init()
running = True
game_active = True

screen = pygame.display.set_mode((950,600))

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
            