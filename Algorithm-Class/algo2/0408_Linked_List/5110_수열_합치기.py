
# 시간초과 ㅎ_ㅎ Linked List로 풀어야겠당

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    base = []
    for _ in range(M):
        merge = list(map(int, input().split()))
        for i in range(len(base)):
            if base[i] > merge[0]:
                base = base[:i] + merge + base[i:]
                break
        else:
            base += merge

    # print('#{}'.format(t) ,*list( base[i] for i in range(-1,-11,-1) ))                
    print('#{}'.format(t) ,*base[-1:-11:-1])                