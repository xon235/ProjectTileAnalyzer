import copy
from enum import Enum
from collections import deque

W = 5
H = 5

if __name__ == '__main__':
    maxScore = 0 #debug

    emptyBoard = [[None for x in range(W)] for y in range(H)]
    queue = deque([State(emptyBoard, 0, get_pieces_from_file())])

    # Queue loop
    while len(queue) > 0:
        node = queue.popleft()
        board = node.board
        score = node.score
        pieces = node.pieces
        # Input start position loop
        for row in range(H):
            for col in range(W):
                if board[row][col] == None:
                    pos = [row, col]
                    board[pos[0]][pos[1]] = pieces.popleft()
                    board[pos[0]][pos[1]].score = 10
                    rangeStartVal = 0
                    dirStack = deque([])
                    # Input direction loop
                    while True:
                        for i in range(rangeStartVal, 4):
                            newPos = pos + dir_to_list(DIR(i))
                            if is_pos_valid(newPos, board):
                                pos = newPos
                                dirStack.append(DIR(i))
                                rangeStartVal = 0
                                p = pieces.popleft()
                                p.score = 10 * ((len(dirStack) // 3) + 1)
                                board[pos[0]][pos[1]] = p
                                if len(dirStack) >= 2:
                                    bC = copy.deepcopy(board)
                                    sC = score + resolve_board(boardClone)
                                    pC = copy.deepcopy(pieces)
                                    maxScore = max(maxScore, sC) #debug
                                    print(maxScore) #debug
                                    queue.append(State(bC, sC, pC))
                                break
                        else:
                            board[pos[0]][pos[1]] = None
                            if len(dirStack) > 0:
                                lastDir = dirStack.pop().value
                                rangeStartVal = lastDir + 1
                                pos -= dir_to_list(DIR(lastDir))
                            else:
                                break;

class State:
    def __init__(self, board, score, pieces):
        self.board = copy.deepcopy(board)
        self.score = score
        self.pieces = pieces

class Piece:
    def __init__(self, color, score):
        self.color = color
        self.score = score

class DIR(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class COLOR(Enum):
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4

def dir_to_list(dir):
    if dir == DIR.UP:
        return [-1, 0]
    elif dir == DIR.RIGHT:
        return [0, 1]
    elif dir == DIR.DOWN:
        return [1, 0]
    else:
        return [0, -1]

def get_pieces_from_file():#Test passed
    pieces = deque([])
    f = open("pieces.csv", 'r')
    lines = f.readlines()
    for line in lines:
        pieces.append(Piece(COLOR(int(line)), 0))
    f.close()
    return pieces

def is_inside_board(pos, board):#Test passed
    width = len(board[0])
    height = len(board)
    if pos[0] < 0 or pos[0] >= width:
        return False
    elif pos[1] < 0 or pos[1] >= height:
        return False
    else:
        return True

def is_pos_valid(pos, board):#Test passed
    if is_inside_board(pos, board):
        if board[pos[0]][pos[1]] == None:
            return True
    return False

def same_adjacent_color(row, col, board):

    ps = []
    dst = [row, col]
    if board[dst[0]][dst[1]] != None:
        for i in range(0, 4):
            newRow = dst[0] + dir_to_list(DIR(i))[0]
            newCol = dst[1] + dir_to_list(DIR(i))[1]
            trg = (newRow, newCol)
            if is_inside_board(trg, board) and board[trg[0]][trg[1]] != None:
                if board[dst[0]][dst[1]].color == board[trg[0]][trg[1]].color:
                    ps.append(trg)
    return ps

def resolve_board(board):#Test passed
    score = 0
    while True:
        toDestroy = set([])
        for row in range(H):
            for col in range(W):
                ps = same_adjacent_color(row, col, board)
                if  len(ps) > 1:
                    toDestroy.add((row, col))
                    for p in ps:
                        toDestroy.add(p)

        if len(toDestroy) == 0:
            break

        print(toDestroy)

        for p in toDestroy:
            score += board[p[0]][p[1]].score
            board[p[0]][p[1]] = None

        for col in range(W):
            for row in reversed(range(H)):
                if board[row][col] == None:
                    for i in reversed(range(0, row)):
                        if board[i][col] != None:
                            board[row][col] = board[i][col]
                            board[i][col] = None
                            break
    return score
