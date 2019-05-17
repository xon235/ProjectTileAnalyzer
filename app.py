import copy
from enum import Enum
from collections import deque

W = 5
H = 5

if __name__ == '__main__':
    maxScore = 0 #debug

    emptyBoard = [[PIECE.EMPTY for x in range(W)] for y in range(H)]
    pieces = get_pieces_from_file()
    queue = deque([State(emptyBoard, 0, pieces)])

    # Queue loop
    while len(queue) > 0:
        node = queue.pop()
        board = node.board
        score = node.score
        pieces = node.pieces
        # Input start position loop
        for row in range(5):
            for col in range(5):
                if board[row][col] == PIECE.EMPTY:
                    pos = [row, col]
                    board[pos[0]][pos[1]] = pieces.popleft()
                    rangeStartVal = 0
                    dirStack = deque([])
                    # Input direction loop
                    while True:
                        for i in range(rangeStartVal, 4):
                            newPos = pos + dir_to_vector(DIR(i))
                            if is_pos_valid(newPos, board):
                                pos = newPos
                                dirStack.append(DIR(i))
                                rangeStartVal = 0
                                board[pos[0]][pos[1]] = pieces.popleft()
                                if len(dirStack) >= 2:
                                    bC = copy.deepcopy(board)
                                    sC = score + reslove_board(boardClone)
                                    pC = copy.deepcopy(pieces)
                                    maxScore = max(maxScore, sC) #debug
                                    print(maxScore) #debug
                                    queue.append(State(bC, sC, pC))
                                break
                        else:
                            board[pos[0]][pos[1]] = PIECE.EMPTY
                            if len(dirStack) > 0:
                                lastDir = dirStack.pop().value
                                rangeStartVal = lastDir + 1
                                pos -= dir_to_vector(DIR(lastDir))
                            else:
                                break;


class DIR(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class PIECE(Enum):
    EMPTY = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5

class State:
    def __init__(self, board, score, pieces):
        self.board = copy.deepcopy(board)
        self.score = score
        self.pieces = pieces

def dir_to_vector(dir):
    if dir == DIR.UP:
        return [-1, 0]
    elif dir == DIR.RIGHT:
        return [0, 1]
    elif dir == DIR.DOWN:
        return [1, 0]
    else:
        return [0, -1]

def get_pieces_from_file():
    pieces = deque([])
    f = open("pieces.csv", 'r')
    lines = f.readlines()
    for line in lines:
        pieces.append(PIECE(int(line)))
    f.close()
    return pieces

def is_pos_valid(pos, board):
    width = len(board[0])
    height = len(board)
    if pos[0] < 0 or pos[0] >= width:
        return False
    elif pos[1] < 0 or pos[1] >= height:
        return False
    elif board[pos[0]][pos[1]] != PIECE.EMPTY:
        return False
    else:
        return True

def reslove_board(board):
    score = 0
    return score
