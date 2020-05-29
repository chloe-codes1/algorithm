
board = [ [0]*20 for _ in range(20) ]

N = int(input())

for n in range(1, N+1):
    row1, col1, row2, col2 = map(int, input().split())
    for i in range(row1, row1 + row2 ):
        for j in range(col1, col1+ col2):
            board[i][j] = n

result = [ [0] for _ in range(N) ]

for n in range(1, N+1):
    for b in range(20):
        result[n-1][0] += board[b].count(n)


for r in result:
    print(*r)