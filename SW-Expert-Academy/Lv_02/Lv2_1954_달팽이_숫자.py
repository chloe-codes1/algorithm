# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


# [예제]

# N이 3일 경우,
 



# N이 4일 경우,
 


# [제약사항]

# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어진다.


# [출력]

# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())

for i in range(1,T+1):
    N = int(input())
    print('#{}'.format(i))

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    num = 0
    index = 0

    current_x, current_y = 0, -1

    array = [[-1]*N for n in range(N)]

    while num < N*N:
        direction = directions[index]
        temp_x = current_x + direction[0]
        temp_y = current_y + direction[1]
    
        if temp_x < 0 or temp_y <0 or temp_x >= N or temp_y >= N or array[temp_x][temp_y] != -1:
            index += 1
            if index == 4:
                index = 0
        else:
            num +=1
            current_x, current_y = temp_x, temp_y
            array[current_x][current_y] = num

    for data in array:
        print(' '.join(map(str,data))) 
