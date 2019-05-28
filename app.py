import copy
from enum import Enum
from collections import deque
from lib import *

if __name__ == '__main__':
    maxScore = 0 #debug
    W = 5
    H = 5
    emptyBoard = [[None for x in range(W)] for y in range(H)]
    queue = deque([State(emptyBoard, 0, get_pieces_from_file(), 0)])
    plays = []#debug

    rowSearchStart = 4
    colSearchStart = 2

    # Queue loop
    while len(queue) > 0:
        node = queue.popleft()
        board = node.board
        score = node.score
        pieces = node.pieces
        depth = node.depth
        # Input start position loop
        if len(pieces) > 2:
            for row in range(rowSearchStart, len(board)):
                for col in range(colSearchStart, len(board[0])):
                    bC = copy.deepcopy(board)
                    sC = score
                    pC = copy.deepcopy(pieces)
                    dC = depth
                    if bC[row][col] == None:
                        # if depth == 2:
                        #     exit()#debug
                        pos = Point(col, row)
                        bC[pos.y][pos.x] = pC.popleft()
                        bC[pos.y][pos.x].score = 10
                        rangeStartVal = 0
                        dirStack = deque([])
                        # Input direction loop
                        while len(pC) > 0:
                            for i in range(rangeStartVal, 4):
                                # print(dir_to_list(DIR(i)))
                                newPos = pos + dir_to_list(DIR(i))
                                if is_pos_valid(newPos, bC):
                                    pos = newPos
                                    dirStack.append(DIR(i))
                                    rangeStartVal = 0
                                    p = pC.popleft()
                                    p.score = 10 * ((len(dirStack) // 3) + 1)
                                    bC[pos.y][pos.x] = p
                                    # if len(dirStack) >= 12:
                                    # if len(dirStack) == 24:#debug
                                    #     print('Dir: %d'%len(dirStack))#debug
                                    bCC = copy.deepcopy(bC)
                                    sCC = sC + resolve_board(bCC)
                                    pCC = copy.deepcopy(pC)
                                    dCC = dC + 1
                                    tmp = maxScore #debug
                                    maxScore = max(maxScore, sCC) #debug
                                    intermediateMax = intermediate_max(bCC, pCC, sCC)

                                    if  intermediateMax > 3700:
                                        queue.append(State(bCC, sCC, pCC, dCC))

                                    print('D: %d / Q: %d / S: %5d / M: %5d / R:%d, C:%d / P: %2d, I: %2d'%(dCC, len(queue), sCC, maxScore, row, col, len(pCC), intermediateMax)) #debug
                                    break
                            else:
                                pC.appendleft(bC[pos.y][pos.x])
                                bC[pos.y][pos.x] = None
                                if len(dirStack) > 0:
                                    lastDir = dirStack.pop().value
                                    rangeStartVal = lastDir + 1
                                    pos -= dir_to_list(DIR(lastDir))
                                else:
                                    break;
        rowSearchStart = 0
        colSearchStart = 0

    for i in range(len(plays)):
        print('-------------------------------------------------------------')
        print_board(plays[i][0])
        print()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()
        print_board(plays[i][1])
        print('-------------------------------------------------------------')
