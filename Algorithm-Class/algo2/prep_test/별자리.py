dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,-1,-1,-1,0,1,1,1]

T = int(input())

def find(r,c):
    global count
    s = []
    s.append((r,c))
    visited[r][c] = 1
    while s:
        r,c = s.pop()
        for k in range(8):
            nr = r+dr[k]
            nc = c+dc[k]
            if sky[nr][nc] == 1 and not visited[nr][nc]:
                s.append((nr,nc))
                visited[nr][nc] =1
    count+= 1
    return         

for t in range(1, T+1):
    sky = [[0] + list(map(int,input().split())) + [0] for _ in range(10)]
    #벽 만들기~
    side = 12
    sky.insert(0, [0]*side)
    sky.append([0]*side)
    visited = list( [0]*side for _ in range(side))
    count = 0
    for r in range(12):
        for c in range(12):
            if not visited[r][c] and sky[r][c] == 1:
                find(r,c)
    print('#{} {}'.format(t,count))