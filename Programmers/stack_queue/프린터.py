from collections import deque


def solution(priorities, location):
    answer = 0

    # 데이터 정제
    d = deque([(val, idx) for idx, val in enumerate(priorities)])

    # 계산
    while d:
        paper = d.popleft()
        if d and max(d)[0] > paper[0]:
            d.append(paper)
        else:
            answer += 1

            # 내가 요청한 문서 인지 확인
            if paper[1] == location:
                break

    return answer


ret = solution([2, 1, 3, 2], 2)  # 1
print(ret)
