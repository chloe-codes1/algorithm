# 캐신기 초간단 ver.

def f(n,k):
    if n == k:
        print(array)

    for i in range(n, k):
        array[n], array[i] = array[i], array[n]
        f(n+1, k)
        array[i], array[n] = array[n], array[i]

array = [1,2,3,4,5]
f(0, len(array))