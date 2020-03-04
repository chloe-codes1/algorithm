T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
def move(r, c, s):
    global result
    if len(s) == 7:
        result.add(s)
        return
    else:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if board[nr][nc] == 10:
                continue
            move(nr,nc, s + str(board[nr][nc]))

for t in range(1, T+1):
    size = 6
    board = [ [10] + list(map(int, input().split())) + [10] for _ in range(4)]
    board.insert(0, [10]*size)
    board.append([10]*size)
    result = set()
    for row in range(1, size-1):
        for col in range(1, size-1):
            move(row,col,str(board[row][col]))
    print('#{} {}'.format(t, len(result)))
