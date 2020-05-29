
T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list( map(int, input().split()))

    biggest = 0
    smallest = 1000000

    for n in numbers:
        if n < smallest:
            smallest = n
        if n> biggest:
            biggest = n
    
    print('#{} {}'.format(t, biggest-smallest))