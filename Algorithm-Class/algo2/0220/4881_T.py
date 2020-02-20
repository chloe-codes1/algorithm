def f(n,k,s):
    global minV
    if n == k:
        if minV > s:
            minV = s
            return
    elif minV <= s:
        return

    else:
        for i in range(k): 
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, s+ data[n][i]) 
                used[i] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = [ list(map(int, input().split())) for _ in range(N)]
    

    length = len(data)
    result = [0] * length
    used = [0] * length
    minV = 10*N
    f(0, length,0)

    print('#{} {}'.format(t,minV))