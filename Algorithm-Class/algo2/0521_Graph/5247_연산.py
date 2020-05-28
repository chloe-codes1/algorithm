from collections import deque


def calculator(num, calc):
    if calc == 0:
        return num + 1
    elif calc == 1:
        return num - 1
    elif calc == 2:
        return num * 2
    else:
        return num - 10


def bfs(N, M):
    global t
    Q = deque()
    Q.append((N, 0))
    results[N] = t
    while Q:
        num, count = Q.popleft()
        for i in range(4):
            next_num = calculator(num, i)
            if next_num == M:
                return count + 1
            elif 1 <= next_num <= 1000000 and results[next_num] != t:
                Q.append((next_num, count + 1))
                results[next_num] = t 


T = int(input())

for t in range(1, T + 1):
    results = [0] * 1000001 
    N, M = map(int, input().split())
    print('#{} {}'.format(t, bfs(N, M)))