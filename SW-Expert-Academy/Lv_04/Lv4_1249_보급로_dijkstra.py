
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def check(x,y):
    if x < 0 or y < 0 or x > N-1 or y> N-1:
        return False
    if visited[x][y]:
        return False
    return True

def dijkstra(q):
  
  # 출발점 선정
  dist[x][y] = 0
  heapq.heappush(heqp, (dist[x][y], x, y))  # (가중치, x, y)   =>  enQueue

  while heap:
      d, x, y = heapq.heappop(heaqp)
        if x == N-1 and y == N-1:
            return
        visited[x][y] = 1

        for i in range(4): # 최소값(x,y)에 인접한 정점들 중에서
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문가능하고 가중치 업데이트 된다면
            if check(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                heapq.heappush(heap, (dist[nx][ny], nx, ny))


T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [ list(map(int, input())) for _ in range(N) ]
    INF = float('inf')
    dist = [ [INF]*N for _ in range(N) ] # 가중치
    visited = [[0]* N for _ in range(N)] # 방문 체크
    heapq = []  # heap (우선순위 큐)
    dijkstra(0,0)
    print(f'#{t} {dist[N-1][N-1]}')
