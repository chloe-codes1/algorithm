
def dfs(n, V, t):
    if n==t:
        return 1
    else:
        visited[n] = 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                if dfs(i, V, t) == 1: # i 노드로 이동
                    return 1
        return 0 #dfs이 1을 return한 적이 없으면 (목적지를 방문하지 못하면)


def dfs2(n, V, t):
    s = []
    s.append(n)     # 시작점 push
    visited[n] = 1  # stack에 저장됨

    while s:        # stack에 방문할 노드(갈림길)가 남아있지 않으면
        n = s.pop()
        if n == t:
            return 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i]==0:    # n번 node에서 갈 수 있는
                s.append(i)
                visited[i] = 1

    return 0


N = int(input())

for n in range(1, N+1):
    V, E = map(int, input().split())

    adj = [[0]*(V+1) for _ in range(V+1) ]
    visited = [0] * (V+1)

    for i in range(E):
        f, t = map(int, input().split())
        adj[f][t] = 1

    start, end = map(int, input().split())       

    print('#{}'.format(n) ,dfs2(start, V, end))