# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
 



# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
 


# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.


# [제약 사항]

# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.

# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# 다음 줄부터 각 테스트 케이스가 주어진다.

# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# [출력]

# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


def check_sudoku(array):
    for i in range(9):
        if set(array[i]) != set(numbers):
            return 0
    
        row = set()
        for j in range(9):
            row.add(array[j][i])
        if row != set(numbers):
            return 0
    
    square_array = [set(), set(), set()]
    index = 0

    for k in range (0,81):
        r = k//9
        c = k%9

        if k !=0 and k %3 == 0:
            if index == 2:
                index = -1
            index += 1

        square_array[index].add(array[r][c])

        if k !=0 and k %27 == 0:
            if square_array[0] != set(numbers) and square_array[1] != set(numbers) and square_array[2] != set(numbers):
                return 0
    return 1


T = int(input())
numbers = [1,2,3,4,5,6,7,8,9]
for t in range(1, T+1):
    array = [[0]*9 for n in range(9)]

    for n in range(9):
        array[n] = list(map(int, input().split()))    

    print('#{0} {1}'.format(t, check_sudoku(array)))



        
        