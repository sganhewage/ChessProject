#imports
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

#putting the image on the board
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess Graphics/chess graphics/chess board/chessboard.jpg')
chessboard = pygame.image.load("Chess Graphics/chess graphics/chess board/chessboard.jpg").convert()
x = 100
y = 30
screen.blit(chessboard, (x, y))
pygame.display.flip()  #shows the chessboard

running = True
while (running): #press end game then loop stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()