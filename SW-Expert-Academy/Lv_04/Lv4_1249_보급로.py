from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def dijkstra(q):
    global visited
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 안벗어나게 잡아용
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] > visited[r][c] + MAP[nr][nc]:
                    # 복구 작업시간이 더 적은 경로의 합으로 업데이트 해용
                    visited[nr][nc] = min(visited[nr][nc], visited[r][c] + MAP[nr][nc])
                    q.append((nr,nc))

T = int(input())
for t in range(1,T+1):
    N = int(input())
    MAP = [ list(map(int, input())) for _ in range(N) ]
    INF = float('inf')
    visited = [ [INF]*N for _ in range(N) ]
    visited[0][0] = 0
    q = deque()
    start = (0,0)
    q.append(start)
    dijkstra(q)
    print(f'#{t} {visited[N-1][N-1]}')
