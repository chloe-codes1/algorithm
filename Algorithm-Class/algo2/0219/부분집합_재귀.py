def f(n,k):
    if n==k: #부분집합 한 개 완성

        for i in range(k):
            if L[i] ==1:
                print(A[i], end= ' ')
        print(L)
    else:
        L[n] = 0
        f(n+1, k)
        L[n] = 1
        f(n+1, k)

A = [1,2,3]
L = [0]*len(A)
f(0, len(A))