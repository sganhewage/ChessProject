#Actual chess brain things
import pygame
import chess
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

chess_map_from_true_y_to_board_y = {
   0: "8",
   1: "7",
   2: "6",
   3: "5",
   4: "4",
   5: "3",
   6: "2",
   7: "1"}

chess_map_from_board_y_to_true_y = {
   8: "0",
   7: "1",
   6: "2",
   5: "3",
   4: "4",
   3: "5",
   2: "6",
   1: "7"}

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
    # A function(positionString, board) that returns the all possible moves of a rook stood on a given position
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
    # A function(positionString, board) that returns the all possible moves of a bishop stood on a given position
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
# A function(positionString, board) that returns the all possible moves of a king stood on a given position
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
# A function(positionString, board) that returns the all possible moves of a pawn stood on a given position
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

def draw_board(board):
    screen.blit(chessboard, (10, 10))
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != None:
                screen.blit(piece_dict[board[y][x]], (x_offset + scale*x, y_offset + scale*y))
"""
def showMoves(pos_moves):
    for move in pos_moves:
        x_cord = x_offset + scale*int(chess_map_from_alpha_to_index[str(move)[0]])
        y_cord = y_offset + scale*int(str(move)[1])
        pygame.draw.circle(screen, (0,0,255), (x_cord, y_cord), 20, 5)
"""
def makeMove(board, playerinputclicks):
    piece_y = playerinputclicks[0][0]
    piece_x = playerinputclicks[0][1]

    if board[piece_y][piece_x] != None:
        dest_y = playerinputclicks[1][0]
        dest_x = playerinputclicks[1][1]

        board_piece_y = chess_map_from_true_y_to_board_y[piece_y]
        alpha_piece_x = chess_map_from_index_to_alpha[piece_x]

        board_dest_y = chess_map_from_true_y_to_board_y[dest_y]
        alpha_dest_x = chess_map_from_index_to_alpha[dest_x]

        pos_moves = []

        if str(board[piece_y][piece_x])[1] == "P":
            if str(board[piece_y][piece_x])[0] == "w":
                #SETUP FOR PROMOTION IMPLEMENTATION
                if piece_y != 0:
                    pos_moves.append(alpha_piece_x+str((int(board_piece_y)+1)))
                    if piece_x != 7:
                        if str(board[piece_y-1][piece_x+1])[0] == "b":
                            pos_moves.append(chess_map_from_index_to_alpha[piece_x+1]+chess_map_from_true_y_to_board_y[piece_y-1])
                    if piece_x != 0:
                        if str(board[piece_y-1][piece_x-1])[0] == "b":
                            pos_moves.append(chess_map_from_index_to_alpha[piece_x-1]+chess_map_from_true_y_to_board_y[piece_y-1])
                    if piece_y == 6:
                        pos_moves.append(alpha_piece_x+"4")
            if str(board[piece_y][piece_x])[0] == "b":
                #SETUP FOR PROMOTION IMPLEMENTATION
                if piece_y != 7:
                    pos_moves.append(alpha_piece_x+str((int(board_piece_y)-1)))
                    if piece_x != 7:
                        if str(board[piece_y+1][piece_x+1])[0] == "w":
                            pos_moves.append(chess_map_from_index_to_alpha[piece_x+1]+chess_map_from_true_y_to_board_y[piece_y+1])
                    if piece_x != 7:
                        if str(board[piece_y+1][piece_x-1])[0] == "w":
                            pos_moves.append(chess_map_from_index_to_alpha[piece_x-1]+chess_map_from_true_y_to_board_y[piece_y+1])
                    if piece_y == 1:
                        pos_moves.append(alpha_piece_x+"5")
            #pos_moves = getPawnMoves(alpha_piece_x+board_piece_y, board)

        if str(board[piece_y][piece_x])[1] == "R":
            pos_moves = getRookMoves(alpha_piece_x+board_piece_y, board)
            upper_y_moves = []
            lower_y_moves = []
            left_x_moves = []
            right_x_moves = []
            for move in pos_moves:
                if str(move)[0] == alpha_piece_x and int(str(move)[1]) > int(board_piece_y):
                    upper_y_moves.append(move)
                if str(move)[0] == alpha_piece_x and int(str(move)[1]) < int(board_piece_y):
                    lower_y_moves.append(move)
                if str(move)[1] == board_piece_y and chess_map_from_alpha_to_index[str(move)[0]] > piece_x:
                    right_x_moves.append(move)
                if str(move)[1] == board_piece_y and chess_map_from_alpha_to_index[str(move)[0]] < piece_x:
                    left_x_moves.append(move)
            lower_y_moves.reverse()
            left_x_moves.reverse()
            

        if str(board[piece_y][piece_x])[1] == "Q":
            pos_moves = getQueenMoves(alpha_piece_x+board_piece_y, board) 

        if str(board[piece_y][piece_x])[1] == "B":
            pos_moves = getBishopMoves(alpha_piece_x+board_piece_y, board)

        if str(board[piece_y][piece_x])[1] == "K":
            if len(str(board[piece_y][piece_x])) == 3:
                pos_moves = getKnightMoves(alpha_piece_x+board_piece_y, board)
            else:
                pos_moves = getKingMoves(alpha_piece_x+board_piece_y, board)

        #showMoves(pos_moves)

        for i in pos_moves:
            if(i == alpha_dest_x+board_dest_y):
                if board[piece_y][piece_x] != None:
                    if str(board[dest_y][dest_x])[0] == str(board[piece_y][piece_x])[0]:
                        pass
                    elif str(board[dest_y][dest_x])[0] != str(board[piece_y][piece_x])[0]:
                        board[dest_y][dest_x] = board[piece_y][piece_x]
                        board[piece_y][piece_x] = None
                    else:
                        board[dest_y][dest_x] = board[piece_y][piece_x]
                        board[piece_y][piece_x] = None
            else:
                pass
    return board

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
            
            selectedsquare = (row, col)
            playerinputclicks.append(selectedsquare)
            if selectedsquare == (row, col):
                selectedsquare = ()
                #playerinputclicks = []
                if len(playerinputclicks) >= 2:
                    board = makeMove(board, playerinputclicks)
                    selectedsquare = ()
                    playerinputclicks = []

            #if len(playerinputclicks) == 2: #storing the moves

    draw_board(board)
    pygame.display.update()
    clock.tick(60)
pygame.quit()