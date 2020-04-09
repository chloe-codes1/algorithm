from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    
    base = deque(map(int, input().split()))

    for _ in range(M-1):
        merge = deque(map(int, input().split()))
        head = merge[0]
        for idx, val in enumerate(base):
            if val > head:
                base.insert(idx-1, merge)
                break
        else:
            base.append(merge)

    print(base)                