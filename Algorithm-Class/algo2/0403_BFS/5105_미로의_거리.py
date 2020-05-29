from collections import deque

T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def find(r,c,d):
    global count 
    queue.append((r,c,d))
    visited[r][c] = 1

    while queue:
        current = queue.popleft()
        if (current[0], current[1]) == end:
            count = current[2]-2
            break
        else:
            for k in range(4):
                nr = current[0] + dr[k]
                nc = current[1] + dc[k]
                nd = current[2] +1

                if visited[nr][nc] == 0 and maze[nr][nc] != '1':
                    queue.append((nr,nc,nd))
                    visited[nr][nc]=1

for t in range(1, T+1):
    N = int(input())
    size = N+2
    maze = [['1'] + list(input()) + ['1'] for _ in range(N)]
    maze.insert(0, ['1' for _ in range(size)])
    maze.append(['1' for _ in range(size)])

    visited = [ [0]*size for _ in range(size)]

    for r in range(size):
        for c in range(size):
            if maze[r][c] == '2':
                sr, sc = r,c
            if maze[r][c] == '3':
                end = (r,c)
    count = 0
    queue = deque()
    find(sr,sc,1)
    print('#{} {}'.format(t, count))
    

