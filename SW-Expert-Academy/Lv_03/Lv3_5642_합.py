# N개의 정수가 입력으로 주어진다.

# 이때 연속하여 몇 개의 정수를 골라 합을 구할 수 있다.

# 예를 들어, 1 3 -8 18 -8 이 있다고 하자.

# 그럼 2번부터 4번까지의 수를 골라 합을 구하면, 3+(-8)+18 = 13이다. 

# 이렇게 연속해서 정수를 골라 합을 구할 때, 그 합의 최대가 몇인지 구하는 프로그램을 작성하세요.

# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)

# 각 테스트 케이스 첫째 줄에 숫자 N이 주어진다. (3 ≤ N ≤ 100,000)

# 둘째 줄에는 절대값이 1000이하의 정수 N개가 공백을 사이에 두고 입력된다.

# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 연속된 정수의 합의 최대값을 출력하시오.



T = int(input())

for t in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    max_sum = numbers[0]
    temp = numbers[0]
    for i in range(1, len(numbers)):
        temp = max(temp + numbers[i], numbers[i])
        max_sum = max(temp, max_sum)


    print('#{} {}'.format(t,max_sum))