import itertools

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    
    array = [i for i in range(1,13) ]

    count = 0
    arrays = list(itertools.combinations(array[:K - (N-1)*N//2 ], N))

    print(arrays)

    for j in arrays:
        if sum(j) == K:
                count+=1                   
    print('#{} {}'.format(t,count))
