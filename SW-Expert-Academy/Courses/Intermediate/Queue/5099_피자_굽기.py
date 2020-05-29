from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = deque( [i, cheese[i]] for i in range(N) )

    i = 0
    while len(oven) != 1:
        oven[0][1] //= 2

        if oven[0][1] == 0:
            if N + i < M:
                oven.popleft()
                oven.append([N + i, cheese[N+i]])
                i+=1
            else:
                oven.popleft()
        else:
            oven.append(oven.popleft())

    print('#{} {}'.format(t, oven[0][0] +1))    
