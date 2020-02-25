T = 10

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def dfs1(r,c):
    if maze[r][c] == '3':
        return 1
    else:
        maze[r][c] = '1'
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if maze[nr][nc] != '1':
                if dfs(nr, nc) == 1:
                    return 1
        return 0

def dfs2(r,c):
    stack = []
    visited = [[0]*102 for _ in range(102)]
    stack.append((r,c))
    visited[r][c] = 1

    while stack:
        if 



for _ in range(1, T+1):
    case = int(input())
    N = 100
    size = N + 2

    # 테두리에 '1'로 벽 만들긔
    maze = [ ['1'] + list(input()) + ['1'] for _ in range(N)]
    maze.insert(0, ['1' for _ in range(size)])
    maze.append(['1' for _ in range(size)])
    
    sr, sc = -1, -1

    for r in range(1,size):
        for c in range(1,size):
            if maze[r][c] == '2':
                sr, sc = r, c
                break
        if sr != -1:
            break

    print('#{} {}'.format(case, dfs2(sr,sc)))
