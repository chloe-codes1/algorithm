def backtrack(selected, idx, data):
    # selected : 각 node의 선택 여부를 판단하는 배열
    # idx : 깊이
    # input : 목표 개수
    candidates = [0] *2  #선택할 수 있는 선택지는 선택 O/X
    if idx ==data:
        for i in range(data):
            if selected[i]:
                # print(i, end= ' ')
                print(arr[i], end=' ')
        print()
        return
    else:
        n_candidate = make_candidate(candidates)
        for i in range(n_candidate): # 후보군의 개수만큼 반복
            selected[idx] = candidates[i]
            backtrack(selected, idx+1, data)
def make_candidate(candidates):
    candidates[0] = 1
    candidates[1] = 0

    return 2

arr = [ 'A', 'B', 'C', 'D', 'E']
N = 5
backtrack([0]*N, 0, N)