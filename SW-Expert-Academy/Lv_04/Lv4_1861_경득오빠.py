# 나보다 더 간결해서 코드 뜯어보기!!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maximum = 0
    value = None
    for i in range(N):
        for j in range(N):
            x, y = i, j
            cnt = 1
            while 1:
                flag = 0
                for k in range(4):
                    if 0 <= x + dx[k] < N and 0 <= y + dy[k] < N and room[x+dx[k]][y+dy[k]] == room[x][y]+1:
                        x += dx[k]
                        y += dy[k]
                        cnt += 1
                        flag = 1
                        break
                if flag == 0:
                    visited[i][j] = cnt #visited에 뭐를 저장하는거지??
                    break
                elif visited[x][y] != 0:
                    visited [i][j] += visited[x][y] + cnt - 1
                    break
            if visited[i][j] > maximum:
                maximum = visited[i][j]
                value = room[i][j]
            elif visited[i][j] == maximum:
                value = min(value, room[i][j])
    print(f'#{tc} {value} {maximum}')