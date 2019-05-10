import copy
from enum import enum
from collections import deque

W = 5
H = 5

class Color(Enum):
    EMPTY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5

class State
    def __init__(self, board, score, pieces):
        self.board = copy.deepcopy(board)
        self.score = score
        self.pieces = pieces

if __name__ == '__main__':
    emptyBoard = [[Color.EMPTY for x in range(W)] for y in range(H)]
    pieces = getPiecesFromFile()
    queue = deque([State(emptyBoard, 0, pieces)])

    while()

def getPiecesFromFile():
    pieces = []
    f = open("pieces.csv", 'r')
    # lines = f.readlines()
    # for line in lines:
    #     print(line)
    f.close()
    return pieces
