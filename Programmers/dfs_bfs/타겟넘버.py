def solution(numbers, target):
    answer = 0

    def dfs(index=0):

        if index < len(numbers):
            numbers[index] *= 1
            dfs(index+1)

            numbers[index] *= -1
            dfs(index+1)

        elif sum(numbers) == target:
            nonlocal answer
            answer +=1

    dfs()

    return answer


params = [([1, 1, 1, 1, 1], 3), ([4, 1, 2, 1], 4)]
for param in params:
    ret = solution(*param) 
    print(ret)  # 5, 2
