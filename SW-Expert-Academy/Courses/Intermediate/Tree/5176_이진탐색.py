T = int(input())

for t in range(1, T+1):
    N = int(input())
    nodes = [ i for i in range(1,N+1)]
    L = [0]*(N+1)
    R = [0]*(N+1)
    r = 1
    while r*2 <= N:
        L[r] = r*2
        R[r] = r*2 +1
        r += 1
        if r*2 == N:
            R[r] = r*2 +1
    ans = []
    def get_it(v):
        if v == 0:
            return
        get_it(L[v])
        ans.append(v)
        get_it(R[v])
        
    get_it(V)
    root = ans.index(1) + 1
    val = ans.index(N//2) +1
    print('#{} {} {}'.format(t, root, val))