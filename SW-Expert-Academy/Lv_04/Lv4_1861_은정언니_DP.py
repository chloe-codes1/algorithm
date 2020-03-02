# 은정언니 DP느낌 코드!


def update(visit, r, c):
    global max_visit, max_visit_num
    if visit > max_visit:
        max_visit = visit
        max_visit_num = rooms[r][c]
    elif visit == max_visit:
        if rooms[r][c] < max_visit_num:
            max_visit_num = rooms[r][c]
def f(r, c, N, visit, start_r, start_c):
    if max_visit_from_here[r][c] is not None:
        visit += max_visit_from_here[r][c] - 1
        update(visit, r, c)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] - rooms[r][c] == 1:
            f(nr, nc, N, visit+1, start_r, start_c)
            break
    else:
        update(visit, start_r, start_c)
T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    max_visit_from_here = [[None]*N for _ in range(N)]
    max_visit = 0
    max_visit_num = 0
    for r in range(N):
        for c in range(N):
            f(r, c, N, 1, r, c)
    print('#{} {} {}'.format(tc, max_visit_num, max_visit))    