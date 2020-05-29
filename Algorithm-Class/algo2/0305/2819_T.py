T = int(input())

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def find(i,j,n,s):
    if n == 7:
        r.add(s)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni <4 and 0 <= nj < 4:
                find(ni,nj, n+1, s + str(a[ni][nj]))



for t in range(1, T+1):
    a = [ list(map(int, input().split())) for _ in range(4) ]

    r = set()
    for i in range(4):
        for j in range(4):
            find(i,j,0,'')
    
    print('#{} {}'.format(t, len(r)))