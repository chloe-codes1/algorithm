import sys

sys.stdin = open('input.txt')


T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    d =list(map(int, input().split()))

    d.insert(0,0) # 출발 지점
    d.append(N)   # 도착 지점

    last =0
    cnt = 0

    for i in range(1, M +2):
        if d[i] - d[i-1] > K:
            cnt = 0
            break

        if d[i] > last + K:
            last = d[i-1]
            cnt += 1

    print('#{} {}'.format(t, cnt))