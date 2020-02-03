
T = int(input())

for t in range(1, T+1):
    N = int(input())
    cards = list( map(int, input()))

    max_count =0
    result = 0

    for c in cards:
        count = 0
        for i in range(N):
            if cards[i] == c:
                count+=1

        if max_count < count:
            max_count = count
            result = c

        elif max_count == count:
            if result < c:
                max_count =count
                result = c
    
    print('#{} {} {}'.format(t, result, max_count))