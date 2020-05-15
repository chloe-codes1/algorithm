# {1,2,3,4,5,6,7,8,9,10} 의 powerset 중 원소ㅡ이 값이 10인 부분집합을 모두 출력하시오.

def backtrack(arr, idx, N, selected, sum_num):
    if sum_num > 10:
        return
    if idx == N: 
        # 총합이 10이면 출력
        if sum_num == 10:
            for i in range(N):
                if selected[i]:
                    print(arr[i], end=' ')
            print()
        return

    #현재 index를 선택 했을 경우
    selected[idx] =1
    backtrack(arr, idx+1, N, selected, sum_num + arr[idx])

    #현재 index 를 선택하지 않았을 경우
    selected[idx] = 0
    backtrack(arr, idx+1, N, selected, sum_num )


arr = [1,2,3,4,5,6,7,8,9,10]

backtrack(arr, 0, 10, [0]*10, 0)