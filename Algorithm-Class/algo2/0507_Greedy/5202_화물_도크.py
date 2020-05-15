T = int(input())

def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0][0]
        GREATER = [ element[0] for element in ARRAY[1:] if element[0] > PIVOT ]
        LESSER = [ element[0] for element in ARRAY[1:] if element[0] <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


for t  in range(1, T+1):
    N = int(input())
    forms = [ list(map(int, input().split())) for _ in range(N) ]
    data = quick_sort(forms)
    visited = [1] + [0]*(N-1)
    result = [data[0]]
    while 1:
        if sum(visited) == N:
            break
        for i in range(N):
            if result[-1][1] > data[i][0]:
                visited[i] = 1
        idx = 0
        val =  float('inf')
        for i in range(N):
            if not visited[i] and result[-1][1] <= data[i][0] and data[i][1] < val:
                idx = i
                val = data[i][0]
        result.append(data[idx])
    print('#{} {}'.format(t, len(result)))