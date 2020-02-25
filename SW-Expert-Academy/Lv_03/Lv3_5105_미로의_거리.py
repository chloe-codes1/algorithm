dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def dfs(r,c,size):



T = int(input())
for t in range(1,T+1):
    N = int(input())
    size = N+2
    maze = [ ['1'] + list(input()) + ['1'] for _ in range(N)]
    maze.insert(0, ['1' for _ in range(size)] )
    maze.append(['1' for _ in range(size)])

    sr, sc = -1,-1

    for r in range(size):
        for c in range(size):
            if maze[r][c] == '2':
                sr, sc = r,c
                break
        if sr != -1:
            break

    print('#{} {}'.format(t, dfs(sr,sc,size)))