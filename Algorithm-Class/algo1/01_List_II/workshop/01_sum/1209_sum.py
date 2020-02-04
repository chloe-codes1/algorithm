
size = 100

for t in range(1, 11):
    case = int(input())
    array = [[]*n for n in range(size)]
    total = 0
    maximum = 0

    for i in range(100):
        array[i] = list(map(int, input().split()))
    
    #가로
    for i in range(size):
        total = sum(array[i])
        if total > maximum:
            maximum = total
    
    #세로
    for i in range(size):
        total = 0
        for j in range(size):
            total += array[j][i]
        if total > maximum:
            maximum = total
            
    total = 0
    #왼쪽 대각선
    for i in range (size):
        total += array[i][i]
        if total > maximum:
            maximum = total
    total = 0
    #오른쪽 대각선
    for i in range (size-1, -1,-1):
        total += array[i][i]
        if total > maximum:
            maximum = total

    print('#{0} {1}'.format(t,maximum))