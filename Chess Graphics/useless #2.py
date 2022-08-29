#Actual chess brain things
import pygame
pygame.init()

# define constants for the screen width and height
screen_width = 1376
screen_height = 768

# create the screen object; size determined by screen_width and screen_height
screen = pygame.display.set_mode((screen_width, screen_height))

#testing
board = [['  ' for i in range(8)] for i in range(8)] #https://levelup.gitconnected.com/chess-python-ca4532c7f5a4
scale = 94

wPImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wP.jpg')
wKImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wK.jpg')
wQImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wQ.png')
wRImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wR.jpg')
wKnImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wKn.jpg')
wBImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/wB.jpg')
bPImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bP.jpg')
bKImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bK.jpg')
bQImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bQ.jpg')
bRImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bR.jpg')
bKnImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bKn.jpg')
bBImg = pygame.image.load('/Chess Graphics/chess graphics/chess pieces/bB.jpg')

gameDisplay = pygame.display.set_mode((display_width, display_height)) #source it https://pythonprogramming.net/displaying-images-pygame/
gameDisplay.blit(wPImg, (x, y))

board = [["bR", "bKn", "bB", "bQ", "bK", "bB", "bKn", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wKn", "wB", "wQ", "wK", "wB", "wKn", "wR"]]

piece_dict = {"wP": wPImg,
             "wK": wKImg,
             "wQ": wQImg,
             "wR": wRImg,
             "wKn": wKnImg,
             "wB": wBImg,
             "bP": bPImg,
             "bK": bKImg,
             "bQ": bQImg,
             "bR": bRImg,
             "bKn": bKnImg,
             "bB": bBImg}
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] != None:
            screen.blit(piece_dict[y][x], (scale*x, scale*y))

while True:
    pygame.display.update()
    pygame.time.Clock.tick(60)





