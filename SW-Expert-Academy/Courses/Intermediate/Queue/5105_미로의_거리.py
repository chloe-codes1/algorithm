from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(r,c,d):
    global result
    visited[r][c] = True
    queue.append((r,c,d))

    while queue:
        position = queue.popleft()

        if position[0] == end[0] and position[1] == end[1]:
            result = position[2] -2
            break
        
        for k in range(4):
            nr = position[0] + dr[k]
            nc = position[1] + dc[k]
            nd = position[2] + 1

            if visited[nr][nc] == False and maze[nr][nc] !='1':
                visited[nr][nc] = True
                queue.append((nr,nc,nd))

T = int(input())
for t in range(1,T+1):
    N = int(input())
    size = N+2
    maze = [ ['1'] + list(input()) + ['1'] for _ in range(N)]
    maze.insert(0, ['1' for _ in range(size)] )
    maze.append(['1' for _ in range(size)])

    for r in range(size):
        for c in range(size):
            if maze[r][c] == '2':
                sr, sc = r, c
            if maze[r][c] == '3':
                end = (r,c)

    visited = [[False]*size for _ in range(size)]
    result = 0
    queue = deque()
    bfs(sr, sc, 1)

    print('#{} {}'.format(t, result))