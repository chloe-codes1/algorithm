# raw version

import sys

sys.stdin = open('input.txt')


T = 10

for tc in range (1, T+1):
    n = int(input())
    data = list(map(int, input().split()))

    for c in range(n):
        max_idx = 0
        min_idx = 0

        for i in range(1, 100):
            if data[max_idx] < data[i]:
                max_idx = i
            if data[min_idx] > data[i]:
                min_idx = i

        data[min_idx] +=1
        data[max_idx] -=1

    # [ Dumping 이 끝난 시점 ]
    max_value = data[0]      # ->아무거나로 initialize
    min_value = data[0]

    for j in range(1, 100):
        if max_value <data[j]:
            max_value = data[j]
        if min_value > data[j]:
            min_value = data[j]
    
    print('#{} {}'.format(tc, max_value - min_value))