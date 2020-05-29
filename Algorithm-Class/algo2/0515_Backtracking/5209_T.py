def f(n,k,s): # n: n번 공장에 대해 만들 물건을 결정, k: 전체 공장 수, s: n-1 공장까지 생산 비용 
    global MIN
    if n == k:
        # 모든 결정이 끝나면,
        if MIN > s:
            MIN = s
    elif s >= MIN:
        return
    else:
        for i in range(k): # 아직 결정되지 않은 물건이면,
            if not used[i]:
                used[i] = 1
                f(n+1, k, s+plant[i][n])
                used[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    plant = [ list(map(int, input().split())) for _ in range(N)]
    MIN = float('inf')
    used = [0]*N