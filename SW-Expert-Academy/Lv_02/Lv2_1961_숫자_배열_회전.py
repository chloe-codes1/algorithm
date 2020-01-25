# N x N 행렬이 주어질 때,

# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


# [제약 사항]

# N은 3 이상 7 이하이다.

# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,

# 다음 N 줄에는 N x N 행렬이 주어진다.

# [출력]

# 출력의 첫 줄은 '#t'로 시작하고,

# 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())

for t in range(1,T+1):
    print('#{}'.format(t))

    N = int(input())
    
    array_90 = [[0]*N for _ in range(N)]
    array_180 = [[0]*N for _ in range(N)]
    array_270 = [[0]*N for _ in range(N)]


    input_array= [[0]*N for _ in range(N)]
    
    for n in range(N):
        input_array[n] = list(map(int, input().split()))

    #90도 회전
    for r in range(N):
        for c in range(N):
            array_90[c][N-1-r] = input_array[r][c]

    #180도 회전
    for r in range(N):
        for c in range(N):
            array_180[N-1-r][N-1-c] = input_array[r][c]

    #270도 회전
    for r in range(N):
        for c in range(N):
            array_270[N-1-c][r] = input_array[r][c]
    
    
    for i in range(N):
        print(''.join(map(str, array_90[i])), end=' ')
        print(''.join(map(str, array_180[i])), end=' ')
        print(''.join(map(str, array_270[i])))
