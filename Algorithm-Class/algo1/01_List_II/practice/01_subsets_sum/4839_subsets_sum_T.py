
import sys

sys.stdin = open('input.txt')

# 조합 generate 해주는 combination 짱짱맨
from itertools import combinations

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    # 12까지의 원소 중 N개가 포함된 부분집합
    subsets =combinations(range(1,13), N )

    # ver1) for문으로 세기
    # count = 0
    # for subset in subsets:
    #     if sum(subset) == K:
    #         count +=1

    # ver2) comprehension 사용하기
    count = sum(1 for subset in subsets if sum(subset) == K)

    print('#{} {}'.format(t, count))