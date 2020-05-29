
import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    d = [list(map(int, input().split())) for _ in range(N)]


    gotcha = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(M):
                s += sum(d[i+k][j:j+M])
            
            gotcha.append(s)

    print('#{} {}'.format(t, max(gotcha)))