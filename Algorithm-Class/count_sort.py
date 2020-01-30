
def counting_sort (A, B, k):

    # A = 입력 배열
    # B = 정렬된 배열
    # C = 카운트 배열

    C = [0] *k

    for i in range(len(B)):
        C[A[i]] += 1
    
    for i in range(1, len(C)):
        C
