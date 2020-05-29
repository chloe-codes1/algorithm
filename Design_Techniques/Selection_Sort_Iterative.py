# Iterative Selection Sort

def SelectionSort(arr):
    N = len(arr)
    for i in range(N-1):
        MIN = i
        for j in range(i+1, N):
            if arr[j] < arr[MIN]:
                MIN = j
        arr[MIN], arr[i] = arr[i], arr[MIN]

data = [3,4,1,2,5,7]
SelectionSort(data)

print(data)