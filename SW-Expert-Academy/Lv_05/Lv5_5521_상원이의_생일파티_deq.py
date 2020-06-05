from collections import deque

T = int(input())

def bfs(v):
    deq = deque()
    deq.append(v) # enQueue
    visited[v] = 1

    while len(deq) !=0 :
        v = deq.popleft()   # deque
        if visited[v] > 3: # 가지치기
            return

        for w in G[v]:
            if not visited[w]:
                deq.append(w)
                visited[w] = visited[v] + 1

for t in range(1, T+1):
    N, M = map(int, input().split())
    G = {i: [] for i in range(1, N+1)} # 인접 리스트
    visited = [0] * (N+1)
    ans = 0

    for i in range(M):
        u, v  = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    
    bfs(1)

    for i in range(N+1):
        if visited[i] == 2 or visited[i] == 3:
            ans +=1

    print('#{} {}'.format(t, ans))