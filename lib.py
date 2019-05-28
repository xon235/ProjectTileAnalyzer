import copy
from enum import Enum
from collections import deque

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
            return Point(x, y)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Point):
            x = self.x - other.x
            y = self.y - other.y
            return Point(x, y)
        else:
            raise TypeError

    def __repr__(self):
        return '{x: %d, y: %d}'%(self.x, self.  y)

    def __str__(self):
        return 'Point(x=%d, y=%d)'%(self.x, self.  y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class State:
    def __init__(self, board, score, pieces, depth):
        self.board = copy.deepcopy(board)
        self.score = score
        self.pieces = pieces
        self.depth = depth

class Piece:
    def __init__(self, color, score):
        self.color = color
        self.score = score

    def __deepcopy__(self, memo):
        return Piece(self.color, self.score)

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

def print_board(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == None:
                print('|           ', end='')
            else:
                print('|%-6s%4d '%(b[i][j].color.name, b[i][j].score), end='')
        print('|')

def dir_to_list(dir):
    if dir == DIR.UP:
        return Point(0, -1)
    elif dir == DIR.RIGHT:
        return Point(1, 0)
    elif dir == DIR.DOWN:
        return Point(0, 1)
    else:
        return Point(-1, 0)

def get_pieces_from_file():#Test passed
    pieces = deque([])
    f = open("pieces.csv", 'r')
    lines = f.readlines()
    for line in lines:
        pieces.append(Piece(COLOR(int(line)), 0))
    f.close()
    return pieces

def is_inside_board(pos, board):
    width = len(board[0])
    height = len(board)
    if pos.x < 0 or pos.x >= width:
        return False
    elif pos.y < 0 or pos.y >= height:
        return False
    else:
        return True

def is_pos_valid(pos, board):
    if is_inside_board(pos, board):
        if board[pos.y][pos.x] == None:
            return True
    return False

def same_adjacent_color(row, col, board):
    poses = []
    dst = Point(col, row)
    if board[dst.y][dst.x] != None:
        for i in range(0, 4):
            newY = dst.y + dir_to_list(DIR(i)).y
            newX = dst.x + dir_to_list(DIR(i)).x
            trg = Point(newX, newY)
            if is_inside_board(trg, board) and board[trg.y][trg.x] != None:
                if board[dst.y][dst.x].color == board[trg.y][trg.x].color:
                    poses.append(trg)
    return poses

def resolve_board(board):
    score = 0
    while True:
        for col in range(len(board[0])):
            for row in reversed(range(len(board))):
                if board[row][col] == None:
                    for i in reversed(range(0, row)):
                        if board[i][col] != None:
                            board[row][col] = board[i][col]
                            board[i][col] = None
                            break

        toDestroy = set([])
        for row in range(len(board)):
            for col in range(len(board[0])):
                poses = same_adjacent_color(row, col, board)
                if  len(poses) > 1:
                    toDestroy.add((col ,row))
                    for p in poses:
                        toDestroy.add((p.x, p.y))

        if len(toDestroy) == 0:
            break

        for d in toDestroy:
            p = Point(d[0], d[1])
            score += board[p.y][p.x].score
            board[p.y][p.x] = None
    return score

def score_of_n_pieces(n):
    unit = 10
    quotient = n//3
    remainder = n%3
    pre = unit*3*(quotient*(quotient+1))//2
    post = unit*remainder * (quotient+1)
    return pre + post

def simple_max(board, pieces, score):
    simpleMax = score
    noneCount = 0
    boardSum = 0
    height = len(board)
    width = len(board[0])
    for row in range(height):
        for col in range(width):
            if board[row][col] == None:
                noneCount += 1
            else:
                boardSum += board[row][col].score

    simpleMax += boardSum

    if len(pieces) > noneCount:
        remainPiecesLen = len(pieces) - noneCount
        maxNumOfPiecesOnBoard = width*height
        quotient = (remainPiecesLen)//maxNumOfPiecesOnBoard
        remainder = (remainPiecesLen)%maxNumOfPiecesOnBoard

        simpleMax += quotient * score_of_n_pieces(maxNumOfPiecesOnBoard)
        simpleMax += score_of_n_pieces(remainder)

        simpleMax += score_of_n_pieces(noneCount)
    else:
        simpleMax += score_of_n_pieces(len(pieces))

    return simpleMax

def intermediate_max(board, pieces, score):
    simpleMax = score
    colorCount = {COLOR.RED: 0, COLOR.ORANGE: 0, COLOR.YELLOW: 0, COLOR.GREEN: 0, COLOR.BLUE: 0, None: 0}
    noneCount = 0
    boardSum = 0
    height = len(board)
    width = len(board[0])
    for row in range(height):
        for col in range(width):
            if board[row][col] == None:
                colorCount[None] += 1
            else:
                colorCount[board[row][col].color] += 1
                boardSum += board[row][col].score

    simpleMax += boardSum
    # print(score)
    # print(boardSum)
    # print(colorCount)
    count = 0
    remainCount = 0
    while count < len(pieces):
        remainCount = 0
        for i in range(count, count+colorCount[None]):
            if i < len(pieces):
                colorCount[pieces[i].color] += 1
                count += 1
            else:
                break

        # print()
        # print(count)
        # print(colorCount)

        simpleMax += score_of_n_pieces(colorCount[None])
        for key in colorCount:
            if key != None:
                colorCount[key] %= 3
                remainCount += colorCount[key]

        colorCount[None] = width*height - remainCount
        # print(colorCount)

    # print(remainCount)
    simpleMax -= score_of_n_pieces(remainCount)
    return simpleMax
