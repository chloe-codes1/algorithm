
T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    array = [[0]* n for n in range(N)]
    for n in range(N):
        array[n] = list(map(int, input().split()))
    result = 0
    for i in range(N - M+1):
        for j in range(N -M+1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += array[i+x][j+y]
            if result < total:
                result = total
    print('#{} {}'.format(t, result))
