#Pygame template

import pygame
import random

width = 360
height = 480
fps = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init() #this is for handle sound
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites.draw 

# Game Loop
running = True
while running:
    # keep loop running at the rigth spped
    clock.tick(fps)
    # Process input
    for event in pygame.event.get():
        # for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *AFTER* Drawing everything, flip the display
    pygame.display.flip()

pygame.quit()