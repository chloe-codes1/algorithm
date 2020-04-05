# 0 북쪽
# 1 동쪽 
# 2 남쪽
# 3 서쪽

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r,c,d):
    global count

    nr = r + dr[d]
    nc = c + dc[d]

    if  0<= nr <= row and 0 <= nc <= col:
        if room[nr][nc] == 0:
            count += 1
            nd = d
        else:
            if d:
                nd=d-1
            else:
                nd = 3
        clean(nr,nc,d)


row, col = map(int, input().split())
r,c,d = map(int, input().split())
room = [ list(map(int, input().split())) for _ in range(row)]
visited =  [ [0]*col for _ in range(row)]
count = 1

clean(r,c,d)

print(count)


