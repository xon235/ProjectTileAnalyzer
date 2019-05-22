from app import *

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

for i in range(5):
    count += 1
    board[4][i] = pieces.popleft()
    board[4][i].score = 10 * (((count-1) // 3) + 1)

print(resolve_board(board))

# print(is_pos_valid(Point(4, 4), board))
# print(is_pos_valid(Point(1, 8), board))
# print(is_pos_valid(Point(8, 1), board))
# print(is_pos_valid(Point(1, -1), board))
#
# print(is_inside_board(Point(1, 1), board))
# print(is_inside_board(Point(1, 8), board))
# print(is_inside_board(Point(8, 1), board))
# print(is_inside_board(Point(1, -1), board))
