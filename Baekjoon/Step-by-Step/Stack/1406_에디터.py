
<<<<<<< HEAD
import sys
input = sys.stdin.readline

from collections import deque


data = deque(input().strip())
stack = deque()

N = int(input().strip())


for n in range(N):
    orders = input().strip().split()
=======
from collections import deque


data = deque(input())
stack = deque()

N = int(input())


for n in range(N):
    orders = input().split()
>>>>>>> d193c42f3c50f72ca23f79db75dadc8fbefedb0e

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
<<<<<<< HEAD

for s in stack:
    print(s, end='')
=======
for s in stack:
    print(s, end='')


>>>>>>> d193c42f3c50f72ca23f79db75dadc8fbefedb0e
