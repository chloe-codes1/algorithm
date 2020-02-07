T = int(input())

for t in range(1, T+1):
    N, direction = input().split()

    N = int(N)

    board = [ list( map(str, input().split())) for _ in range(N)]


    if direction == 'up':

        for _ in range(N-1):

            for i in range(N):
                for j in range(N-1):
                    if board[j][i] == '0':
                        board[j][i] = board[j+1][i]
                        board[j+1][i] = '0'

                    else:    
                        if board[j][i] == board[j+1][i] and board[j][i][0] != '+' and board[j+1][i] != '+':
                            board[j][i] = '+' + str(int(board[j][i])*2)
                            board[j+1][i] ='0'


    if direction == 'down':

        for _ in range(N-1):

            for i in range(N-1, -1,-1):
                for j in range(N-1, 0,-1):
                    if board[j][i] == '0':
                        board[j][i] = board[j-1][i]
                        board[j-1][i] = '0'

                    else:    
                        if board[j][i] == board[j-1][i] and board[j][i][0] != '+' and board[j-1][i] != '+':
                            board[j][i] = '+' + str(int(board[j][i])*2)
                            board[j-1][i] ='0'

    if direction == 'left':

        for _ in range(N-1):

            for i in range(N):
                for j in range(N-1):
                    if board[i][j] == '0':
                        board[i][j] = board[i][j+1]
                        board[i][j+1] = '0'

                    else:    
                        if board[i][j] == board[i][j+1] and board[i][j][0] != '+' and board[i][j+1] != '+':
                            board[i][j] = '+' + str(int(board[i][j])*2)
                            board[i][j+1] ='0'

    if direction == 'right':

        for _ in range(N-1):

            for i in range(N-1, -1,-1):
                for j in range(N-1, 0,-1):
                    if board[i][j] == '0':
                        board[i][j] = board[i][j-1]
                        board[i][j-1] = '0'

                    else:    
                        if board[i][j] == board[i][j-1] and board[i][j][0] != '+' and board[i][j-1] != '+':
                            board[i][j] = '+' + str(int(board[i][j])*2)
                            board[i][j-1] ='0'


    for i in range(N):
        for j in range(N):
            if board[i][j][0] == '+':
                board[i][j] = board[i][j][1:]
    
    print('#{}'.format(t))

    for b in range(N):
        print(*board[b])