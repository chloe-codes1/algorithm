# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# 다음과 같은 5X5 배열에서 최댓값은 29이다.



# [제약 사항]

# 총 10개의 테스트 케이스가 주어진다.

# 배열의 크기는 100X100으로 동일하다.

# 각 행의 합은 integer 범위를 넘어가지 않는다.

# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
# [입력]

# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

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