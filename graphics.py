#imports
import pygame
from PIL import Image
import tkinter as tk


#the actual board
img = Image.open("Chess Graphics/chess graphics/chess board/chessboard.jpg")
img = img.resize((748, 748))
img.save('Chess Graphics/chess graphics/chess board/chessboard.jpg')

#putting the image on the board
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess Graphics/chess graphics/chess board/chessboard.jpg')
chessboard = pygame.image.load("Chess Graphics/chess graphics/chess board/chessboard.jpg").convert()
x = 10
y = 10
screen.blit(chessboard, (x, y))
pygame.display.flip()  #shows the chessboard

running = True
while (running): #press end game then loop stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()




