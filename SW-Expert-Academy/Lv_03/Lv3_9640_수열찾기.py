# MxM 크기의 숫자판이 있습니다. N개의 양의 정수로 구성된 수열이 주어질 때, 숫자판의 숫자를 따라 상하좌우로 이동해 주어진 수열을 찾을 수 있으면 1, 없으면 0을 출력하는 프로그램을 작성하세요. 
# 각 칸의 숫자는 1번만 사용할 수 있습니다.

# 예를 들어 1234563이란 수열을 아래의 숫자판에서는 완성할 수 없습니다.

# 0 0 0 0 0
# 0 1 2 0 0
# 0 6 3 0 0
# 0 5 4 0 0 
# 0 0 0 0 0

# 다음의 경우는 완성할 수 있습니다.
# 0 0 0 0 0
# 0 1 2 0 0
# 0 6 3 0 0
# 0 5 4 0 0 
# 0 0 3 2 1

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스 별로 수열의 길이 N과 N개의 수, 숫자판의 크기 M, 다음 부터 M개의 줄에 걸쳐 M개씩의 숫자가 주어집니다. (5 <= N, M <=10)

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 0 또는 1을 출력합니다.


T = int(input())

for t in range(1, T+1):
    