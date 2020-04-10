def merge(left, right):
    result = [] # 두 개의 분할된 list를 병합하여 result를 만듦

    while len(left) > 0 and len(right) > 0: # 양쪽 list에 원소가 남아있는 경우

        # 두 sub list의 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0: # 왼쪽 list에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0: # 오른쪽 list에 원소가 남아있는 경우
        result.extend(right)
    return result




def merge_sort(m):
    if len(m) <= 1: # 배열 크기가 0 이거나 1인 경우 바로 return
        return m

    # 1. Divide 부분
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # list의 크기가 1이 될 때까지 merge_sort() 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # 2. Conquer 부분 : 분할된 리스트들 병함
    return merge(left, right)