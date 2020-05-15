def f(n, s):
    global MIN
    if n==N:
        if MIN > s:
            MIN =s
    elif s >= MIN: # 가지치기 - 호출 횟수 확 줄여줌
        return
    else:
        for i in range(N):
            if col[i] == 0:
                col[i] = 1
                f(n+1, s + plant[n][i])
                col[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    plant = [ list(map(int, input().split())) for _ in range(N)]
    col = [0]*N
    MIN = float('inf')
    f(0,0)
    print('#{} {}'.format(t,MIN))