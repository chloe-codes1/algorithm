def solution(clothes):
    answer = dict()
    for cloth in clothes:
        if cloth[1] not in answer:
            answer.update({cloth[1]:1})
        else:
            answer[cloth[1]] += 1
    result = 1
    for key, value in answer.items():
        result*=(value+1)
    return result-1