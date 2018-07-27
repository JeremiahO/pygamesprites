# Pygame template - skeleton for a new pygame project

import pygame
import random
import os

# First thing we need to do is tell pygame to make a window by dimension
WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colours
White = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up folders for game assets
# Windows: C:\Users\jerry\Desktop\PyGames
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "imgs")

# Classes

class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"alienGreen_jump.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x +=5
        if self.rect.left > WIDTH:
           self.rect.right = 0

# Next thing were going to do is pygame.init() this initialize our pygame
pygame.init()

# We also want to include mixer this allows sounds in our game
pygame.mixer.init()

# Now we can create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Determine the size of the screen
pygame.display.set_caption("My Game") # Determines the title of the game at the top of the screen
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


# Game loop

# Were are using this to control our game, running or not running
running = True
while running:

    # Keep loop running at right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display - Imanginary whiteboard
    pygame.display.flip()

pygame.quit()
