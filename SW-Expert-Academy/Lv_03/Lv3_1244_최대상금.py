def prize(c):
    global MAX
    if N == c:
        MAX = max(MAX, int(''.join(nums)))
        return
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            temp = int(''.join(nums))
            if temp not in  used[c+1]:
                used[c+1].add(temp)
                prize(c+1)
            nums[i], nums[j] = nums[j], nums[i]

T = int(input())

for t in range(1,T +1):
    nums, N = input().split()
    nums = list(str(nums))
    N = int(N)
    used = [set() for _ in range(N+1)]
    MAX = float('-inf')
    prize(0)
    print('#{} {}'.format(t, MAX))

