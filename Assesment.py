# https://www.youtube.com/watch?v=YWN8GcmJ-jA

# Brief

# I am going to make a platform shooter game called Brr, in python.
# Brr is a visual 2d platformer with added combat as a side thingy, I am going to be making this in pygame.

# The premise of the game is that you are a prisoner of war and are imprisoned on an enemy warship,
# Your goal is to escape on an escape pod.

# After the loading screen the player has a choice between 2 characters, a melee and a ranger survivor.
# There are going to at least 3 levels and all of them are quite long.
# Once you finish each section in each level you gain a buff to your basic stats.
# Your basic stats are movement speed, jump height, and fire rate.
# There will also be enemy turrets that attack the player, and these may come in various types.

# When you finish the last area the game displays “You Have Escaped!”

# -Player
#  •	One-shot death.
#  •	Is able to move in all directions.
#  •	Melee or ranged attacks.
#  •	Has a changeable movement speed and jump height and fire rate.
# -Turrets
#  •	One-shot death.
#  •	Locked in place.
#  •	Ranged fire.
# -Game world
#  •	Scrolling camera.
#  •	3 areas
#  •	Platforms are stationary, moving or bouncy.
# -User interface
#  •	Loading screen.
#  •	Game menu.
#  •	Character select.

# Imports
import pygame
import sys
from settings import *
from Sprites import Block

# Pygame setup / variables
pygame.int()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
test_block = pygame.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    pygame.display.update()
    clock.tick(60)
