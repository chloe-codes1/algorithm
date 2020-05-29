T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = [ list(map(int, input().split())) for _ in range(N)]
    MIN = float('inf')
    SUM = nums[0][0]
    s = []
    r = c = nr = nc = 0
    s.append((r,c,SUM))
    while s:
        (r, c, SUM) = s.pop()
        for (dr,dc) in ((1,0), (0,1)):
            nr = r + dr
            nc = c + dc
            if N<= nr or nr < 0 or N <= nc or nc <0:
                continue
            val = SUM + nums[nr][nc]
            if nr == N-1 and nc == N-1:
                if MIN > val:
                    MIN = val 
            elif MIN > val:
                s.append((nr,nc,val))

    print('#{} {}'.format(t, MIN))  