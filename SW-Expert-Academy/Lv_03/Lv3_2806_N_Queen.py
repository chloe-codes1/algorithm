# 8*8 체스보드에 8개의 퀸을 서로 공격하지 못하게 놓는 문제는 잘 알려져 있는 문제이다.

# 퀸은 같은 행, 열, 또는 대각선 위에 있는 말을 공격할 수 있다. 이 문제의 한가지 정답은 아래 그림과 같다.
 



# 이 문제의 조금 더 일반화된 문제는 Franz Nauck이 1850년에 제기했다.

# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.


# [출력]

# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

def foundQueen(position):
    for i in range(position):
        if row[i] == row[position]:
            return False
        if abs(row[position] -row[i]) == position - i:
            return False
    return True

def DFS(position):
    global count
    # global 문
    # : global 문을 사용하면 함수 안에서도 전역변수의 값을 수정할 수 있다!
    if position == size:
        count +=1
    else:
        for i in range(size):
            row[position] = i
            if foundQueen(position):
                DFS(position + 1)

T = int(input())
for t in range(1, T+1):
    size = int(input())
    row = [0] *size

    count = 0
    DFS(0)
    print('#{} {}'.format(t,count))