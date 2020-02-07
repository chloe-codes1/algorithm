# import sys
# sys.stdin = open("input.txt")

direction = [[-1, -1], [1, 1], [1, -1], [-1, 1], [1, 0], [-1, 0], [0, 1], [0, -1]]


def change(x, y, d, di, board):
    if x not in range(N) or y not in range(N) or not board[x][y]:
        return 0
    elif board[x][y] == d:
        return 1
    result = change(x+di[0], y+di[1], d, di, board)
    if result:
        board[x][y] = d
        return 1
    else:
        return 0

def game(x, y, d, board):
    for di in direction:
        change(x+di[0], y+di[1], d, di, board)
    return board


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = 2
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1

    for _ in range(M):
        x, y, d = map(int, input().split())
        board[x-1][y-1] = d
        board = game(x-1, y-1, d, board)

    count_B, count_W = 0, 0

    for row in board:
        count_B += row.count(1)
        count_W += row.count(2)
    print('#{} {} {}'.format(tc, count_B, count_W))