# k길이의 순열 만들기

# 순열의 n번 원소 결정, 순열의 길이 k, 사용할 숫자 m개
def f(n, k, m):
    if n == k:
        print(result)
    else:
        for i in range(m):
            # if used[i] == 0:
                # used[i] = 1
            result[n] = array[i]
            f(n+1,k,m)
                # used[i] = 0

array = [1,2,3,4,5]
length = len(array)
result = [0] * 3
used = [0] * length
f(0, 3, length)