T = 10

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def dfs1(i,j):
    if maze[i][j] == '3':
        return 1
    else:
        maze[i][j] = '1' #벽으로 채우기
                         # -> 이렇게 하는 이유는 이동 경로를 출력하는게 아니라 도착지만 찾으면 되는 미로이므로 visited를 만들지 않고
                         #    벽으로 만들어서 지워버리기!!

                         # but, 이 문제는 테두리에 벽으로 감싸있어서 이렇게 푸는게 가능!

        for k in range(4):
            nr = i +dr[k]
            nc = j +dc[k]

            if maze[nr][nc] != '1': # 벽이 아닌 칸이 있으면,
                if dfs1(nr, nc) == 1: #이동
                    return 1
        return 0 #나 3 못찾았어...라고 윗단에 알려주기


def dfs2(i,j):
    s = []
    visited =  [ [0]*16 for _ in range(16)]
    s.append((i,j))
    visited[i][j] = 1
    while s:
        i,j = s.pop()
        if maze[i][j] == '3':
            return 1
        for k in range(4): #4방향으로 주변 칸 탐색
            nr = i + dr[k]
            nc = j + dc[k]

            if maze[nr][nc] != '1' and visited[nr][nc] == 0: #벽이 아니고 방문 안한 칸 있으면,
                s.append((nr,nc))    #방문할 칸 목록에 push
                visited[nr][nc] = 1

    return 0

for _ in range(T):
    case = int(input())
    maze = [ list(input()) for _ in range(16) ]
    si, sj = -1, -1

    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                si, sj = i, j
                break
        
        #제대로 찾았는지 확인 & for문 빠져나가는용
        if si != -1:
            break
    
    print('#{} {}'.format(case, dfs1(si,sj)))
