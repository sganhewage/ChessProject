#Actual chess brain things
import pygame
from Chess import ChessEngine
#from PIL import Image
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


"""User Input and Graphics"""

"""MOVEMENT ALGORITHMS"""

"""# Creating Teams for Black and White (https://levelup.gitconnected.com/chess-python-ca4532c7f5a4)
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image
"""
"""
bP = Piece('b', 'P', 'Chess Graphics/chess graphics/chess pieces/bP.png')
wP = Piece('w', 'P', 'Chess Graphics/chess graphics/chess pieces/wP.png')
bK = Piece('b', 'K', 'Chess Graphics/chess graphics/chess pieces/bK.png')
wK = Piece('w', 'K', 'Chess Graphics/chess graphics/chess pieces/wK.png')
bR = Piece('b', 'R', 'Chess Graphics/chess graphics/chess pieces/bR.png')
wR = Piece('w', 'R', 'Chess Graphics/chess graphics/chess pieces/wR.png')
bB = Piece('b', 'B', 'Chess Graphics/chess graphics/chess pieces/bB.png')
wB = Piece('w', 'B', 'Chess Graphics/chess graphics/chess pieces/wB.png')
bQ = Piece('b', 'Q', 'Chess Graphics/chess graphics/chess pieces/bQ.png')
wQ= Piece('w', 'Q', 'Chess Graphics/chess graphics/chess pieces/wQ.png')
bKn = Piece('b', 'Kn', 'Chess Graphics/chess graphics/chess pieces/bKn.png')
wKn = Piece('w', 'Kn', 'Chess Graphics/chess graphics/chess pieces/wKn.png')
"""


#https://impythonist.wordpress.com/2017/01/01/modeling-a-chessboard-and-mechanics-of-its-pieces-in-python/
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

b_capture_list = []
w_capture_list = []

def capture(captured_piece_x, captured_piece_y, board):
    if str(board[captured_piece_x][captured_piece_y])[0] == "b":
        b_capture_list.append(board[captured_piece_x][captured_piece_y])
        board[captured_piece_x][captured_piece_y] = None
    else:
        w_capture_list.append(board[captured_piece_x][captured_piece_y])
        board[captured_piece_x][captured_piece_y] = None




"""THIS WEBSITE HELPED A LOT IN MOVEMENT ALGORITHMS (https://impythonist.wordpress.com/2017/01/01/modeling-a-chessboard-and-mechanics-of-its-pieces-in-python/)"""
# Rook Moves
def getRookMoves(pos, board):
    # A function(positionString, board) that returns the all possible moves of a knight stood on a given position
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    x, y = row, column
    possmoves = []

# Compute the moves in Rank
    for y in range(8):
        if y != column:
            possmoves.append((row, y))

    # Compute the moves in File
    for x in range(8):
        if x != row:
            possmoves.append((x, column))

    possmoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in possmoves]
    possmoves.sort()
    return possmoves

# Knight Moves
def getKnightMoves(pos, board):
    # A function(positionString, board) that returns the all possible moves of a knight stood on a given position
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    x, y = row, column
    possmoves = []
    try:
        temp = board[x + 1][y - 2]
        possmoves.append([x + 1, y - 2])
    except:
        pass
    try:
        temp = board[x + 2][y - 1]
        possmoves.append([x + 2, y - 1])
    except:
        pass
    try:
        temp = board[x + 2][y + 1]
        possmoves.append([x + 2, y + 1])
    except:
        pass
    try:
       temp = board[x + 1][y + 2]
       possmoves.append([x + 1, y + 2])
    except:
        pass
    try:
        temp = board[x - 1][y + 2]
        possmoves.append([x - 1, y + 2])
    except:
        pass
    try:
        temp = board[x - 2][y + 1]
        possmoves.append([x - 2, y + 1])
    except:
        pass
    try:
        temp = board[x - 2][y - 1]
        possmoves.append([x - 2, y - 1])
    except:
        pass
    try:
        temp = board[x - 1][y - 2]
        possmoves.append([x - 1, y - 2])
    except:
        pass

    # Filter all negative values
    temp = [x for x in possmoves if x[0] >= 0 and x[1] >= 0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

# Bishop Moves
def getBishopMoves(pos, board):
    # A function(positionString, board) that returns the all possible moves of a knight stood on a given position
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    x, y = row, column
    possmoves = []

# moving diagonal all 4 ways
    for i in range(8):
        try:
            temp = board[x + i][y + i]
            possmoves.append([x + i, y + i])
        except:
            pass

        try:
            temp = board[x - i][y + i]
            possmoves.append([x - i, y + i])
        except:
            pass

        try:
            temp = board[x + i][y - i]
            possmoves.append([x + i, y - i])
        except:
            pass

        try:
            temp = board[x - i][y - i]
            possmoves.append([x - i, y - i])
        except:
            pass

# Filter all negative values
    temp = [x for x in possmoves if x[0] >= 0 and x[1] >= 0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

"""QUEEN MOVES"""
def getQueenMoves(pos, board):
    bishop_subset = getBishopMoves(pos, board)
    rook_subset = getRookMoves(pos, board)
    Queen_Moves = bishop_subset + rook_subset
    return Queen_Moves

"""King Moves"""
def getKingMoves(pos, board):
# A function(positionString, board) that returns the all possible moves of a knight stood on a given position
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    x, y = row, column
    possmoves = []
    for i in range(-1, 2):
        for j in range (-1, 2):
            if (i != 0) or (j != 0):
                try:
                    temp = board[x + i][y + j]
                    possmoves.append([x + i, y + j])
                except:
                    pass
    # Filter all negative values
    temp = [x for x in possmoves if x[0] >= 0 and x[1] >= 0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

"""PAWN MOVES""" """(https://www.youtube.com/watch?v=F-ZPioOvOaM)"""


def getPawnMoves(pos, board):
# A function(positionString, board) that returns the all possible moves of a knight stood on a given position
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_alpha_to_index[column]
    x, y = row, column
    possmoves = []
    for i in range(-1, 2):
        for j in range (-1, 2):
            if (i != 0) or (j != 0):
                try:
                    temp = board[x + i][y + j]
                    possmoves.append([x + i, y + j])
                except:
                    pass
    # Filter all negative values
    temp = [x for x in possmoves if x[0] >= 0 and x[1] >= 0]
    allPossibleMoves = ["".join([chess_map_from_index_to_alpha[x[1]], str(x[0] + 1)]) for x in temp]
    allPossibleMoves.sort()
    return allPossibleMoves


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

print(str(board[0][0])[0])

#all this code until quit i got from here https://levelup.gitconnected.com/chess-python-ca4532c7f5a4 and https://www.youtube.com/watch?v=o24J3WcBGLg
running = True
selectedsquare = ()
playerinputclicks = []
while (running): #press end game then loop stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            col = location[0] // 100 #sqsize = height // dimesion (8)
            row = location[1] // 100
            if selectedsquare == (row, col):
                selectedsquare = ()
                playerinputclicks = []
            else:
                selectedsquare = (row, col)
                playerinputclicks.append(selectedsquare)
                move = ChessEngine.Move(playerinputclicks[0], playerinputclicks[1], board)
                board.makeMove(move)
                selectedsquare = ()
                playerinputclicks = []
            #if len(playerinputclicks) == 2: #storing the moves


    pygame.display.update()
    clock.tick(60)
pygame.quit()


print(getKnightMoves("e5", board))