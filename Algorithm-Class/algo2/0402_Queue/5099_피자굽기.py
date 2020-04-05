from collections import deque
T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    c = list(map(int, input().split()))
    o = deque([i, c[i]] for i in range(N))
    i = 0
    while len(o) !=1:
        o[0][1] //= 2
        if o[0][1] == 0:
            if N + i < M:
                o.popleft()
                o.append([N+i, c[N+i]])
                i+=1
            else:
                o.popleft()
        else:
            o.append(o.popleft())
    print('#{} {}'.format(t, o[0][0] +1))


