import pygame

#creates a pygame project
pygame.init()

screen = pygame.display.set_mode((400,500))
screen.fill("red")

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()