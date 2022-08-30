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
white_piece_list = ["wR", "wKn", "wB", "wQ", "wK", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"]
black_piece_list = ["bR", "bKn", "bB", "bQ", "bK", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"]

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

#assigning each space one the board a value (ex A4)
#https://impythonist.wordpress.com/2017/01/01/modeling-a-chessboard-and-mechanics-of-its-pieces-in-python/
chess_map_from_alpha_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7}

chess_map_from_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"}


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
#https://impythonist.wordpress.com/2017/01/01/modeling-a-chessboard-and-mechanics-of-its-pieces-in-python/
chess_map_from_alpha_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7}

chess_map_from_index_to_alpha = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"}

#https://impythonist.wordpress.com/2017/01/01/modeling-a-chessboard-and-mechanics-of-its-pieces-in-python/
def getKnightMoves(pos, board):
    """ A function(positionString, board) that returns the all possible moves
        of a knight stood on a given position
    """
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = x #chess_map_from_alpha_to_index[column]
    #x,y = row, column
    solutionMoves = []
    try:
        temp = board[x + 1][y - 2]
        solutionMoves.append([x + 1, y - 2])
    except:
        pass
    try:
        temp = board[x + 2][y - 1]
        solutionMoves.append([x + 2, y - 1])
    except:
        pass
    try:
        temp = board[x + 2][y + 1]
        solutionMoves.append([x + 2, y + 1])
    except:
        pass
    try:
       temp = board[x + 1][y + 2]
       solutionMoves.append([x + 1, y + 2])
    except:
        pass
    try:
        temp = board[x - 1][y + 2]
        solutionMoves.append([x - 1, y + 2])
    except:
        pass
    try:
        temp = board[x - 2][y + 1]
        solutionMoves.append([x - 2, y + 1])
    except:
        pass
    try:
        temp = board[x - 2][y - 1]
        solutionMoves.append([x - 2, y - 1])
    except:
        pass
    try:
        temp = board[x - 1][y - 2]
        solutionMoves.append([x - 1, y - 2])
    except:
        pass

    # Filter all negative values
    temp = [x for x in solutionMoves if x[0] >=0 and x[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in temp]
    allPossibleMoves.sort()
    return allPossibleMoves
    print(allPossibleMoves)

    #MOVEMENT ALGORITHMS
#def movePiece(source_square_x, source_square_y, destination_square_x, destination_square_y):
  #  if board[destination_square_x][destination_square_y] == None:
     #   temp_source = 0
     #   temp_dest = 0
     #   board[source_square_x][destination_square_x] = temp_source
    #    board[source_square_y][destination_square_y] = temp_dest
   #     temp_source = board[source_square_x][destination_square_x]
  #      temp_dest = board[source_square_y][destination_square_y]
 #   elif board[destination_square_x][destination_square_y] != None && :
#
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


getKnightMoves(23, board)