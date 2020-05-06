T = int(input())

def f(r,c,s):
    global MIN
    if r == N-1 and c ==N-1:
        if MIN > s + nums[r][c]:
            MIN = s + nums[r][c]
    elif MIN <= s:
        return
    else:
        if r+1<N:
            f(r+1, c, s+nums[r][c])
        if c+1 < N:
            f(r, c+1, s+nums[r][c])

for t in range(1, T+1):
    N = int(input())
    nums = [ list(map(int, input().split())) for _ in range(N)]
    MIN = float('inf')
    f(0,0,0)
    print('#{} {}'.format(t, MIN))    