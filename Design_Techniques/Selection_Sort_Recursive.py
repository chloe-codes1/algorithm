# Recursive Selection Sort

def SelectionSort(arr, s):
    N = len(arr)
    if s == N-1:
        return
    MIN = s
    for i in range(s, N):
        if arr[MIN] > arr[i]:
            MIN = i
    arr[s], arr[MIN] = arr[MIN], arr[s]
    SelectionSort(arr, s+1)

data = [3,4,1,2,5,7]
SelectionSort(data,0)

print(data)