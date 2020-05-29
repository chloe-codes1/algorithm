from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))

    for _ in range(M):
        nums.append(nums.popleft())
    
    print('#{} {}'.format(t,nums[0]))