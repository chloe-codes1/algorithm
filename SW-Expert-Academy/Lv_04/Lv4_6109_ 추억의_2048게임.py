# 2048이라는 추억의 게임을 아는가? 2048은 한 때 유명했던 1인용 게임으로, 격자 위에서 숫자가 적힌

# 타일들을 밀어서 합치고 최종적으로 2048을 만들어 내는 것이 목표인 게임이다.

# 한번 타일을 밀 때는 상하좌우를 정해서 밀어야 한다.

# 방향을 정하면 격자 위에 있는 모든 타일이 그 방향으로 밀린다.

# 만약 어떤 타일이 밀리는 방향에 다른 타일이 있고, 두 타일에 적힌 숫자가 같다면 두 타일은 합쳐져

# 새로운 하나의 타일이 되고 이 타일에 적힌 숫자는 합쳐진 숫자들의 합이 된다.

# 이렇게 합쳐져서 만들어진 새로운 타일은 숫자가 같은 다른 타일이 밀려와도 합쳐져서는 안 된다.

# 만약 같은 숫자가 적힌 타일이 세 개 이상 있을 때는 헷갈리는 경우를 없애기 위해 빨리 벽에 닿게 될 타일을 먼저 민다고

# 생각한다.

# 예를 들어 “2 2 4 2 2 2”가 적힌 타일들이 있을 때, 이 타일들을 왼쪽으로 밀면 결과는 “4 4 4 2 0 0”이 된다.

# 0은 타일이 없는 빈 칸을 나타낸다.

 

# 위의 그림은 4×4 크기의 격자(일반적인 2048 게임)에서 모든 타일을 오른쪽으로 이동시킨 예이다.

# 우리는 2048게임을 N×N 크기의 격자에서 하려고 한다.

# 현재 격자에 어떤 식으로 타일이 있는지 주어지고, 타일들을 이동시킬 방향이 주어질 때,

# 타일을 모두 이동시키고 나면 격자가 어떻게 변할 지 계산하는 프로그램을 작성하라.



# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤20)과 하나의 문자열 S가 공백 하나로 구분되어 주어진다.

# S는 “left”, “right”, “up”, “down”의 넷 중 하나이며 각각 타일들을 왼쪽, 오른쪽, 위쪽, 아래쪽으로 이동시키겠다는 뜻이다.

# 다음 N개의 줄의 i번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다.

# 이 정수들은 0이거나 2이상 1024이하의 2의 제곱수들이다.

# i번째 줄의 j번째 정수는 격자의 위에서 i번째 줄의 왼쪽에서 j번째에 있는 칸에 있는 타일에 어떤 정수가 적혀 있는지 나타내며,

# 0이면 이 칸에 타일이 없음을 의미한다.


# [출력]

# 각 테스트 케이스마다 ‘#t’(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 줄을 띄운 후,

# N줄에 걸쳐 격자의 어떤 위치에 어떤 숫자가 적힌 타일이 있는지 입력 형식과 같은 형식으로 출력한다.




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