#the brains of the chess game

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
