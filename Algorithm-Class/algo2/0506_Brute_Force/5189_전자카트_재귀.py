T = int(input())

def f(d, s, t):
    global MIN
    if t > MIN:
        return
    if d == N:
        t += field[s][0]
        if MIN > t:
            MIN = t
        return
    else:
        for i in range(N):
            if not visited[i] and field[s][i]:
                visited[i] = 1
                f(d+1,i, t + field[s][i])
                visited[i] = 0

for t in range(1, T+1):
    N = int(input())
    field = [ list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    MIN = float('inf')
    visited[0]=1
    f(1, 0, 0)
    print('#{} {}'.format(t, MIN))

