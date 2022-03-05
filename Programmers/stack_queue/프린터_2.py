from collections import deque


def solution(priorities, location):
    answer = 0

    # 데이터 정제 - (priority, idx) 형태의 tuple 만들기
    d = deque([(val, idx) for idx, val in enumerate(priorities)])

    # 계산
    while d:
        paper = d.popleft()

        # max 가 아닌 any 를 사용 하니 속도가 더 빠르다
        if d and any(paper[0] < q[0] for q in d):
            d.append(paper)
        else:
            answer += 1

            # 내가 요청한 문서 인지 확인
            if paper[1] == location:
                break

    return answer


ret = solution([2, 1, 3, 2], 2)  # 1
print(ret)
