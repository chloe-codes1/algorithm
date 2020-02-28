T = int(input())
def min_diff(n,k,h):
    global result
    if h >= height:
        result = min(h, result)
        return
    else:
        for i in range(n, k):
            if not used[i]:
                used[i]=1
                min_diff(i,k,h +tall[i])
                used[i]=0
for t in range(1, T+1):
    clerks, height = map(int, input().split())
    tall = list(map(int, input().split()))
    used = [0]*clerks
    result = 10000000
    min_diff(0,clerks,0)
    print('#{} {}'.format(t,result-height))