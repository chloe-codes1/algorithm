T = 10

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dfs(i,j):
    s = []
    visited =  [ [0]*100 for _ in range(100)]
    s.append((i,j))
    visited[i][j] = 1
    while s:
        i,j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4): 
            nr = i + dr[k]
            nc = j + dc[k]

            if maze[nr][nc] != '1' and visited[nr][nc] == 0: 
                s.append((nr,nc))    
                visited[nr][nc] = 1

    return 0


for _ in range(T):
    case = int(input())
    maze = [ list(input()) for _ in range(100) ]
    si, sj = -1, -1

    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        
        if si != -1:
            break

    print('#{} {}'.format(case, dfs(si, sj)))