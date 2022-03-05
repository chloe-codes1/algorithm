def solution(progresses, speeds):
    # 데이터 정제
    workdays = []
    target = 100
    for idx, progress in enumerate(progresses):
        task = target - progress
        todos, extra = divmod(task, speeds[idx])
        if extra:
            todos += 1
        workdays.append(todos)

    # 계산
    answer = []
    count = 1
    for i in range(1, len(workdays)):
        if workdays[i - count] >= workdays[i]:
            count += 1
        else:
            answer.append(count)
            count = 1

    answer.append(count)
    return answer


# ret = solution([93, 30, 55], [1, 30, 5])  # [2, 1]
ret = solution([99, 1, 99, 1], [1, 1, 1, 1])  # [1, 3]
print(ret)
