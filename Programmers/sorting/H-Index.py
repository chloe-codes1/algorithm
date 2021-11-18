def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            break
        answer += 1
    return answer


ret = solution([3, 0, 6, 1, 5])
print(ret)  # 3
