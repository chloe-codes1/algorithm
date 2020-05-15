def quick_sort (arr, left, right):
    # pivot 위치 결정 (pivot을 기준으로 큰 값은 오른쪽, 작은 값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left > right:
        return
    # 피봇 구하기
    pivot = lomuto_partition(arr, left, right)
    pivot = hoare_partition(arr, left, right)
    # 왼쪽 부분집합 정렬 실행
    quick_sort(arr, left, pivot-1)
    # 오르쪽 부분집합 정렬 실행
    quick_sort(arr,pivot+1, right)

def lomuto_partition(arr, left, right):
    # 맨 오른쪽 요소를 pivot으로 설정하고,
    # i = left -1
    # j = left
    pivot = arr[right]
    i = left -1

    for j in range(left, right):
        # arr[i] 가 pivot보다 작으면,
        if arr[j] < pivot:
            # i를 1 증가
            # arr[j], arr[i] 위치 교환
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # i가 가리키는 위치가 pivot보다 작은 값의 마지막 인덱스
    # i + 1 의 위치에 pivot을 두고 i+1 반환
    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    return i+1

def hoare_partition(arr, left, right):
    # i, j 설정하고, 큰값 & 작은 값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left]

    # i가 j보다 작을 때 까지 게속해서 반복
    while i <= j:
        # pivot 보다 큰 값이 나올 때 까지 i 증가
        while i<=j and arr[i] <= pivot:
            i += 1
        # pivot 보다 작은 값이 나올 때 까지 j 감소
        while i <=j and arr[j] >= pivot:
            j -= 1
        
        # i가 j보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[left], arr[j] = arr[j], arr[left]
    return j # pivot 위치인 j 반환

arr = [4,6,3,6,8,0,3,8,10]
quick_sort(arr, 0, len(arr)-1)
print(arr)