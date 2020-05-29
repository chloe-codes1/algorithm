import sys

sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1):
    c = 100
    n = int(input())

    d = [list(map(int, input().split() )) for _ in range(c)]


    max_sum = 0

    for i in range(c):
        s = 0
        for j in range(c):
            s+= d[i][j]
        if max_sum < s:
            max_sum = s
        
    for j in range(c):
        s = 0
        for i in range(c):
            s += d[i][j]
        if max_sum < s:
            max_sum = s


    s = 0
    for i in range(c):
        s += d[i][i]

    if max_sum < s:
        max_sum = s

    s = 0
    for i in range(c):
        s += d[i][-(i+1)] #음수 index 사용하긔

    if max_sum <s :
        max_sum = s

    print('#{} {}'.format(n, max_sum))