#Pygame template

import pygame
import random
from settings import *

pygame.init()
pygame.mixer.init() #this is for handle sound
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(TITLE)
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
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *AFTER* Drawing everything, flip the display
    pygame.display.flip()

pygame.quit()