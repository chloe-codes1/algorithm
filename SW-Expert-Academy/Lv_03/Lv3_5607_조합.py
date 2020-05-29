# 자연수 N와 R가 주어진다. 이 때의 N combination R의 값을 1234567891로 나눈 나머지를  출력하세요.

# 예를들면 N이 4, R이 2라면 4 combination 2는 (4 * 3) / (2 * 1) = 6이 된다.

# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)

# 각 케이스의 첫 줄에 정수 N, R이 주어진다. (1 ≤ N ≤ 1000000, 0 ≤ R ≤ N)
 
# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, N combination R을 1234567891로 나눈 나머지를 출력하시오.


import itertools


combination = '1234567891'



T = int(input())

for t in range(1,T+1):
    N, R = map(int, input().split())

    result = (N * (N-1))/ (R * (R-1)) 
    print(result)