import sys

sys.stdin = open('input.txt')


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))

    arr = []
    
    for i in range(N-M+1):
        arr.append(sum(d[i: i+M]))

    print('#{} {}'.format(t, max(arr) - min(arr)))