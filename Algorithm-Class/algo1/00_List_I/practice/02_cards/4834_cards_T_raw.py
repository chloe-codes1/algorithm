from collections import Counter


import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(input())

    # initialize 를 0으로 하기
    c = [0] *10

    for i in range(n):
        c[ int(d[i]) ] += 1

    max_index = 0
    max_value = c[0]

    for i in range(1,10):
        if max_value < c[i]:
            max_value = c[i]
            max_index = i

    print('#{} {} {}'.format(t, max_index, max_value))