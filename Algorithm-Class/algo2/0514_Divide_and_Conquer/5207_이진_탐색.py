def binary_search(direction, start, end, num, arr):
    global result
    middle = (start+end)//2
    if num == arr[middle]:
        result += 1
    else:
        if num > arr[middle] and direction != 1:
            binary_search(1, middle+1, end, num, arr)
        elif num < arr[middle] and direction != -1:
            binary_search(-1, start, middle-1, num, arr)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    result = 0
    for b in B:
        binary_search(0, 0, N-1, b, A)
    print('#{} {}'.format(t, result))