#imports
import pygame
from PIL import Image
import tkinter as tk

# initialize pygame
pygame.init()

# define constants for the screen width and height
screen_width = 1376
screen_height = 768

# create the screen object; size determined by screen_width and screen_height
screen = pygame.display.set_mode((screen_width, screen_height))

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




#LOGIC PORTION
#def piece_location(letter, number, piece):
    #print("klajshdklfhas")

#grid on the chess board
class Gamestate():
    def __init__(self):
        self.board = [
        ["bR", "bKn", "bB", "bQ", "bK", "bB", "bKn", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wKn", "wB", "wQ", "wK", "wB", "wKn", "wR"]]
    self.whiteToMove = True
    self.moveLog = []
