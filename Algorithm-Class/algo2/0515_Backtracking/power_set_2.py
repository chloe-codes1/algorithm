def f(n, k):
    if n==k: # 모든 원소에 대해 결정된 경우
        s = 0
        for i in range(k):
            if a[i]:
                # print(arr[i], end=' ')
        # print()
                s+= arr[i]
        print(s)
    else:
        # a[n] = 0
        # f(n+1, k) #다음칸으로 이동
        # a[n] = 1
        # f(n+1, k)

        for i in range(2):
            a[n] = i
            f(n+1, k)

arr = [4,6,7]
K = 3 # 주어진 집합의 원소 개수
a = [0]*3 # 원소의 포함여부를 나타내기 위한 배열

f(0,K)