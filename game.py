import pygame

pygame.init()

width, height = 1280, 780
screen = pygame.display.set_mode((width,height))
pygame.display.get_caption("")
clock = pygame.time.Clock()
running = True

while running:
    
    # user clicks X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.display.flip()


pygame.quit