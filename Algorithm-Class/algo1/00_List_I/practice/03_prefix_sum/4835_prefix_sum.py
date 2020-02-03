T = int(input())

for t in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = int(M)

    numbers =list( map(int, input().split()))
    
    max_sum = 0
    min_sum = 1000000

    for i in range(N-M+1):
        count = 0
        for j in range(M):
            count += numbers[i+j]

        if count < min_sum:
            min_sum = count
        if count > max_sum:
            max_sum = count
    
    print('#{} {}'.format(t, max_sum - min_sum))
            