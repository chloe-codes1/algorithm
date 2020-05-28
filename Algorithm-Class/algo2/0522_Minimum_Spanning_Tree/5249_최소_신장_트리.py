T = int(input())

for t in range(1, T+1):

    V, E = map(int, input().split())
    V +=1
    adj = [[0] * V for _ in range(V)]

    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s][e] = c
        adj[e][s] = c # 무방향 그래프라서

    # key, p(parent), mst 준비
    INF = float('inf')
    key = [INF] *V # key는 무한대로 초기화
    p = [-1] * V   # p(parent)는 -1로 초기화
    mst = [False] * V

    # 시작점 선택 : 0번 선택
    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V:
        # 아직 mst가 아니고, key가 최소인 정점 선택 : u
        MIN = INF
        u = -1
        for i in range(V):
            if not mst[i] and key[i] <MIN:
                MIN = key[i]
                u = i
        # u를 mst로 선택
        mst[u] = True
        result += MIN
        cnt+=1
        # key 값을 갱신
        # u에 인접하고, 아직 mst가 아닌 정점 w에서 key[w] > u - w 가중치  이면 갱신!
        for w in range(V):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u

    print('#{} {}'.format(t,result))     