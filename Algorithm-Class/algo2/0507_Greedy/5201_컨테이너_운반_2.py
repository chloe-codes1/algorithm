T = int(input())
 
for t in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    result = 0
    for i in range(M):
        temp = 0
        for w in W:
            if T[i] >= w and temp <= w:
                temp = w
        if temp:
            W.remove(temp)
        result += temp
    print('#{} {}'.format(t, result))
