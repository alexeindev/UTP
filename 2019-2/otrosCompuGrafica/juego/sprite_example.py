#Pygame template

import pygame
import random
import os

width = 800
height = 600
fps = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

game_folder = os.path.dirname(__file__)
img_folder =os.path.join(game_folder,"img")

class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
        self.image.set_colorkey(BLACK) #Color to ignore
        self.rect = self.image.get_rect() #encloses the sprite
        self.rect.center = (width/2 , height/2)
        self.y_speed = 5
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > height:
            self.y_speed = -5
        if self.rect.right > width:
            self.rect.right = 0
        if self.rect.top < 0:
            self.y_speed = 5

pygame.init()
pygame.mixer.init() #this is for handle sound
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites.draw 
player = Player()
all_sprites.add(player)

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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *AFTER* Drawing everything, flip the display
    pygame.display.flip()

pygame.quit()