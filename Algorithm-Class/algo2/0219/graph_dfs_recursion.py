def dfs1(n, V):
    visited[n] = 1
    print(n, end= ' ')
    
    for i in range(1, V+1):
        if adj[n][i] == 1 and visited[i] == 0: #노드 i가 n에 인접하고 방문 전이면
            dfs1(i, V)

def dfs2(n, V):
    s = []
    s.append(n)     # 시작점 push
    visited[n] = 1  # stack에 저장됨

    while s:        # stack에 방문할 노드(갈림길)가 남아있지 않으면
        n = s.pop()
        print(n, end=' ')
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i]==0:    # n번 node에서 갈 수 있는
                s.append(i)
                visited[i] = 1




V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1) ] #인접 행렬
visited = [0]*(V+1)

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]

    adj[n1][n2] = 1 #방향 그래프일땐 이것만!
    # adj[n2][n1] = 1 #이건 무방향 그래프일때 이거까지 한다!

# dfs1(1, V)
dfs2(1, V)