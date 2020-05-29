from collections import deque


def solution(prices):
    answer = deque()

    for i in range(len(prices)):
        temp = len(prices) -i -1
        count =0
        for j in range(i+1, len(prices)):
            count +=1
            if prices[i] > prices[j]:
                temp = count
                break
        
        answer.append(temp)


    return list(answer)


print(solution([1, 2, 3, 2, 3]))