T = int(input())
for t in range(1, T+1):
    E, N = map(int,input().split())
    infos = list(map(int,input().split()))
    V = E+1
    L = [0] *(V+1)
    R = [0] *(V+1)

    for i in range(0, E*2, 2):
        parent, child = infos[i], infos[i+1]
        if L[parent]:
            R[parent] = child
        else:
            L[parent] = child

    count = 0

    def count_it(v):
        global count
        if v == 0:
            return
        count_it(L[v])
        count_it(R[v])
        count +=1

    count_it(N)

    print('#{} {}'.format(t,count))
        
