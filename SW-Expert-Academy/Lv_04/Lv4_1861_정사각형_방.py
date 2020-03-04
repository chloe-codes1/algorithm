from collections import deque

T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def get_path(r,c,d):
    global SUM
    visited[r][c] = True
    queue.append((r,c,d))

    while queue:
        current = queue.popleft()

        dead_end = True

        for k in range(4):
            nr = current[0] + dr[k]
            nc = current[1] + dc[k]
            nd = current[2] + 1
            if rooms[nr][nc]:
                if visited[nr][nc] == 0 and rooms[current[0]][current[1]] +1 == rooms[nr][nc]:
                    visited[nr][nc] = 1
                    dead_end = False
                    queue.append((nr,nc,nd))
            
        if dead_end == True:
            SUM = current[2]
            break

for t in range(1, T+1):
    N = int(input())
    size = N + 2
    rooms = [ [0] + list(map(int, input().split())) +[0] for _ in range(N) ]
    rooms.insert(0, [0]*size)
    rooms.append([0]*size)

    result = 0
    start = 0 

    for row in range(1, N+1):
        for col in range(1, N+1):
            visited = [[0]*size for _ in range(size)]
            SUM = 0
            queue = deque()
            get_path(row,col,1)
            if result < SUM:
                result = SUM
                start = rooms[row][col]
            elif result == SUM and rooms[row][col]< start:
                start = rooms[row][col]

    print('#{} {} {}'.format(t,start, result))        

