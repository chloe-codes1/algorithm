import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))

    # max() min() 사용하지 않기

    max_num = d[0]
    min_num = d[0]

    for i in range(1, n):
        if max_num < d[i]:
            max_num = d[i]
        if min_num > d[i]:
            min_num = d[i]

    print('#{} {}'.format(t,max_num - min_num))