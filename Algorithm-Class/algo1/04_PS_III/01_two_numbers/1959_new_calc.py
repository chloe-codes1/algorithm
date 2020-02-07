T = int(input())
for t in range(1,T+1):
    N, M =  list(map(int,input().split()))


    Aj = list(map(int,input().split()))
    Bj = list(map(int,input().split()))

    count = 0
    size = 0
    smaller = ''
    biggest = 0

    if N > M:
        smaller = 'Bj'
        count = N-M +1
        size = M
    else:
        smaller = 'Aj'
        count = M - N +1
        size = N

    for s in range(count):
        total = 0
        for c in range(size):
            if smaller == 'Aj':
                total += Aj[c] * Bj[c+s]
            else:
                total += Aj[c+s] * Bj[c]
        if total > biggest:
            biggest = total
    
    print('#{0} {1}'.format(t, biggest))