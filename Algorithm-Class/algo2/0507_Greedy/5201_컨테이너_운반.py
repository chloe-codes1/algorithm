T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    result = 0
    for i in range(M):
        temp = 0
        index = 0
        for idx, val in enumerate(W):
            if T[i] >= val and temp <= val:
                temp = val
                index = idx
        if temp:
            W[index] = 0
        result += temp
    print('#{} {}'.format(t, result))
                
        