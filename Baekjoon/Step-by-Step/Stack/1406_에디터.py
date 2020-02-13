
from collections import deque


data = deque(input())
stack = deque()

N = int(input())


for n in range(N):
    orders = input().split()

    if len(orders) > 1:
        data.append(orders[1])
    else:
        order = orders[0]
        if order == 'L' and data:
            stack.append(data.pop())
        elif order == 'D' and stack:
            data.append(stack.pop())
        elif order == 'B' and data:
            data.pop()

print(''.join(data), end='')

stack = list((reversed(stack)))
for s in stack:
    print(s, end='')


