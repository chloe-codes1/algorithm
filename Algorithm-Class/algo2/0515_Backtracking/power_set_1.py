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
        # 어짜피 0,1 두 가지 이므로 power_set.py 처럼 make_candidate() 없애고 막바로 0 과 1을 넣어줌
        selected[idx] = 1
        backtrack(selected, idx+1, data)

        selected[idx] = 0
        backtrack(selected, idx+1, data)

arr = [ 'A', 'B', 'C', 'D', 'E']
N = 5
backtrack([0]*N, 0, N)