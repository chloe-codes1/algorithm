def solution(array, commands):
    answer = []

    for command in commands:
        start, end, position = command
        answer.append(sorted(array[start-1:end])[position-1])

    return answer


ret = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(ret)  # [5, 6, 3]
