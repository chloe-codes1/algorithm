def backtrack(result, selected, idx, N):
    if idx == N:
        print(result)
        return
    # 사용 가능한 선택지 후보군에 대하여 다음 단계로 진행
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result[idx] = i
            backtrack(result, selected, idx+1, N)
            selected[i] = 0

N = 5
backtrack([0]*N, [0]*N, 0, N)