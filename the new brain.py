#Actual chess brain things
import pygame
from PIL import Image
pygame.init()

# define constants for the screen width and height
screen_width = 1376
screen_height = 768

# create the screen object; size determined by screen_width and screen_height
screen = pygame.display.set_mode((screen_width, screen_height))

#board create
#board = [['  ' for i in range(8)] for i in range(8)] #https://levelup.gitconnected.com/chess-python-ca4532c7f5a4
scale = 94
clock = pygame.time.Clock()

wPImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wP.png')
wKImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wK.png')
wQImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wQ.png')
wRImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wR.png')
wKnImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wKn.png')
wBImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/wB.png')
bPImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bP.png')
bKImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bK.png')
bQImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bQ.png')
bRImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bR.png')
bKnImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bKn.png')
bBImg = pygame.image.load('Chess Graphics/chess graphics/chess pieces/bB.png')



gameDisplay = pygame.display.set_mode((800, 800)) #source it https://pythonprogramming.net/displaying-images-pygame/

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

    #MOVEMENT ALGORITHMS
def movePiece(source_square_x, source_square_y, destination_square_x, destination_square_y):
    temp_source = 0
    temp_dest = 0
    board[source_square_x][destination_square_x] = temp_source
    board[source_square_y][destination_square_y] = temp_dest
    temp_source = board[source_square_x][destination_square_x]
    temp_dest = board[source_square_y][destination_square_y]

screen.fill((248, 240, 198))
#the actual board #check if i got this from somewhere
chessboard = pygame.image.load("Chess Graphics/chess graphics/chess board/chessboard.jpg").convert()
screen.blit(chessboard, (10, 10))

x_offset = 27
y_offset = 27

for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x] != None:
            screen.blit(piece_dict[board[y][x]], (x_offset + scale*x, y_offset + scale*y))

#all this code until quit i got from here https://levelup.gitconnected.com/chess-python-ca4532c7f5a4
running = True
while (running): #press end game then loop stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()



