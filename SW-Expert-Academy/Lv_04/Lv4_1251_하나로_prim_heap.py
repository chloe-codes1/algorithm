import heapq
 
T = int(input())
 
for t in range(1, T+1):
    N = int(input()) # 섬의 개수

    weight = [float('inf')] * N # 가중치 
    visited = [0] * N # 방문 체크
    P = list(range(N))  # 부모
    pq = [] # 우선순위 큐

    X = list(map(int, input().split())) # 섬의 x 좌표
    Y = list(map(int, input().split())) # 섬의 y 좌표

    tax = float(input()) # 환경 부담 세율
    cost = [[0] * N for _ in range(N)] # 섬들 간의 비용
 
    # 비용 구하기
    for i in range(0, N-1):
        for j in range(i+1, N):
            cost[i][j] = cost[j][i] = ((X[j] - X[i]) ** 2 + (Y[j] - Y[i]) ** 2) * tax

    weight[0] = 0
    heapq.heappush(pq, (weight[0], 0))
    result = 0
    
    # 우선순위 큐가 비어있지 않은 동안 반복
    while pq:
        c, u = heapq.heappop(pq)  # c: 비용, u: 정점
        if visited[u]: # 방문 했으면 넘어가기
            continue
        visited[u] = 1 # 방문 했다고 표시 후
        result += c # 비용 합에 추가
 
        for v in range(N):  
            if not visited[v] and weight[v] > cost[u][v]:
                weight[v] = cost[u][v]
                P[v] = u
                heapq.heappush(pq, (weight[v], v))
     
    print('#{} {}'.format(t, round(result))) # 반올림쓰