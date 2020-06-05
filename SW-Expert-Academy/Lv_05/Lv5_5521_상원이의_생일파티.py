T = int(input())

def bfs(v):
    global f, r
    r += 1
    Q[r] = v # enQueue
    visited[v]= 1

    while (f != r): # Not empty
        f +=  1
        v = Q[f] # deQueue
        if visited[v] > 3:
            return
        
        for i in range(N+1):
            if G[v][i] and not visited[i]:
                r += 1
                Q[r] = i
                visited[i] = visited[v] + 1



for t in range(1,T+1):
    N, M = map(int, input().split())
    G =[ [0 for _ in range(N+1)] for _ in range(N+1)] # 인접 행렬
    ans = 0
    Q = [0] * (N*N)
    f = -1 # front
    r = -1 # rear
    visited = [0] * (N+1)
    for i in range(M):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1
    bfs(1)

    for i in range(N+1):
        if visited[i] == 2 or visited[i] == 3:
            ans +=1
    
    print('#{} {}'.format(t, ans))