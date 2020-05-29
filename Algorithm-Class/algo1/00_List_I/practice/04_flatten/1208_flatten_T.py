import sys

sys.stdin = open('input.txt')
#.stdin 
# :standard input output

T = 10

for tc in range(1, T+1):
    n = int(input())
    d = list(map(int, input().split()))

    for c in range(n):
        d.sort()
        d[0] += 1
        d[-1] -=1
    
    print('#{} {}'.format(tc, max(d) - min(d)))