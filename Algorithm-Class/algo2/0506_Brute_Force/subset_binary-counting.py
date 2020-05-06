# Binary-counting을 통한 부분집합 생성하긔

arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(0, (1<<n)): # 2^n
    for j in range(n):
        if i % (1 << j):
            print(f'{arr[j]}', end='')
    print()