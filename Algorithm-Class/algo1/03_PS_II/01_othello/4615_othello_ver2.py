

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    board = [ list( 0 for _ in range(N) ) for _ in range(N)]

    mark = [2,1,1,2]
    for i in range(N//2-1 ,N//2 +1):
        for j in range(N//2-1, N//2 +1):
            board[i][j] = mark.pop()

    for _ in range(M):
        x, y, color = map(int, input().split())
        board[y-1][x-1] = color

        for i in range(8):

            willChanged = []
            found = False

            row = y -1 + dr[i]
            col = x -1 + dc[i]


            if row not in range(N) or col not in range(N):
                continue
            
            status = board[row][col]

            while status != 0:

                if status != color:
                    willChanged.append([row, col])
                elif status == color:
                    found = True
                    break
            
                
                row += dr[i]
                col += dc[i]

                if row not in range(N) or col not in range(N):
                    break

                status = board[row][col]
            
            if found:
                for w in willChanged:
                    board[w[0]][w[1]] = color



    black = 0
    white = 0

    for b in board:
        black += b.count(1)
        white += b.count(2)
                


    print('#{} {} {}'.format(t, black, white))                    
