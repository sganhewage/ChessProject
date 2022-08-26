# imports
import pygame
from PIL import Image

# initialize pygame
pygame.init()

# define constants for the screen width and height
screen_width = 800
screen_height = 800

# create the screen object; size determined by screen_width and screen_height
screen = pygame.display.set_mode((screen_width, screen_height))

#the actual board
img = Image.open("Chess Graphics/chess graphics/chess board/chessboard.jpg")
img.show()
