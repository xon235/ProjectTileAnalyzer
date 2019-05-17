from app import *

def print_board(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == None:
                print('|           ', end='')
            else:
                print('|%-6s%4d '%(b[i][j].color.name, b[i][j].score), end='')
        print('|')

pieces = get_pieces_from_file()
print(pieces[0].color.name)
board = [[None for x in range(5)] for y in range(5)]

count = 0
for i in range(5):
    count += 1
    board[0][i] = pieces.popleft()
    board[0][i].score = 10 * (((count-1) // 3) + 1)

for i in reversed(range(5)):
    count += 1
    board[1][i] = pieces.popleft()
    board[1][i].score = 10 * (((count-1) // 3) + 1)

for i in range(5):
    count += 1
    board[2][i] = pieces.popleft()
    board[2][i].score = 10 * (((count-1) // 3) + 1)

for i in reversed(range(5)):
    count += 1
    board[3][i] = pieces.popleft()
    board[3][i].score = 10 * (((count-1) // 3) + 1)
# print(is_pos_valid([4, 4], board))
# print(is_pos_valid([1, 8], board))
# print(is_pos_valid([8, 1], board))
# print(is_pos_valid([1, -1], board))
for i in range(5):
    count += 1
    board[4][i] = pieces.popleft()
    board[4][i].score = 10 * (((count-1) // 3) + 1)

print_board(board)
print(resolve_board(board))
print_board(board)

# print(is_inside_board([1, 1], board))
# print(is_inside_board([1, 8], board))
# print(is_inside_board([8, 1], board))
# print(is_inside_board([1, -1], board))
