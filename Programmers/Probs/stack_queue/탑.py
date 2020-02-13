

from collections import deque


def solution(heights):
    stack = deque()

    for h in range(len(heights) -1, -1, -1):
        temp = 0

        index = -1
        while h + index >= 0:
            if heights[h] < heights[h+index]:
                temp = h+index +1
                break
            
            index -= 1

        stack.appendleft(temp)
            
    return list(stack)

print(solution([6,9,5,7,4]))