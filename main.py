
# Reference section ----------------------------------------------------------------------------------------------------

# These are the sites I used to help me get a handel on Python and Pycharm
# https://www.youtube.com/watch?v=YWN8GcmJ-jA - for learning how to use pygame
# https://www.youtube.com/watch?v=mDKM-JtUhhc - for learning the best ways to use python

# Brief section --------------------------------------------------------------------------------------------------------

# I am going to make a platform shooter game called Brr, in python.
# BRR is a visual 2d platformer with added combat as a side thingy, I am going to be making this in pygame.

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

# Imports section ------------------------------------------------------------------------------------------------------

# Imports for pygame
import pygame
import sys
from settings import *
from sprites import Tile

# Code section ---------------------------------------------------------------------------------------------------------

# Pygame setup / variables
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 0, 0))
    test_tile.draw(screen)

    pygame.display.update()
    clock.tick(60)
