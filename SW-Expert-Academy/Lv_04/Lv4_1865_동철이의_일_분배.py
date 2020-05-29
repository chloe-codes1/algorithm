T = int(input())

def dongcheol(n,k,total):
    global MAX

    if total <= MAX:
        return 

    if n == k:
        if MAX < total:
            MAX = total
            return
    else:
        for i in range(k):
            if visited[i] == 0:
                if chances[n][i] == 0:
                    continue
                else:
                    total *= chances[n][i]*0.01
                    visited[i] = 1
                    dongcheol(n+1,k, total)
                    total /= chances[n][i]*0.01     
                    visited[i] = 0
    



for t in range(1,T+1):
    N = int(input())
    chances = [ list( map(int, input().split())) for _ in range(N)]

    visited = [0]*N
    MAX = float('-inf')

    dongcheol(0,N,1)

    print('#%s %.6f'%(t,MAX*100))
