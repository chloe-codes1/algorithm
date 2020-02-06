
T = int(input())
for t in range(1, T+1):
    print('#{}'.format(t))
    N = int(input())
    result = [[1]* (n+1) for n in range(N)]
    for n in range(2,N):
        for m in range (1, n):
            result[n][m] = result[n-1][m-1] + result[n-1][m]
        
    for x in range(N):
        for y in range(x+1):
            print(result[x][y], end=' ')
        print()