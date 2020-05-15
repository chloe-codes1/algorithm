def f(n, k, s, M, rs):
    global cnt
    global fcnt # 호출 횟수 세려고
    fcnt += 1
    if n==k:
        if s==M: # 합이 M인 경우
            cnt += 1
    elif s > M: # 가지치기 - 호출 횟수 확 줄여줌
        return
    
    elif s+rs < M: # 가지치기 2 - 부분집합에 포함된 원소와 남은 원소의 합이 M에 못 미치면 return
        return
    else:
        f(n+1, k, s, M, rs-arr[n])
        f(n+1, k, s+arr[n], M, rs-arr[n])


arr = [1,2,3,4,5,6,7,8,9,10]
M=40
K = len(arr)
cnt = 0
fcnt = 0
f(0,K,0, M, sum(arr))
print(cnt, fcnt)