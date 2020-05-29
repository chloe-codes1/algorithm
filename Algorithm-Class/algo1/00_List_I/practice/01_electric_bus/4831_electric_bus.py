# input & output 은 통과하는데 Test case는 일부 통과 못함.... 고쳐야해...


T = int(input())

for t in range(1,T+1):

    K, N, M = map(int,input().split())

    chargable = list(map(int, input().split()))

    count = 0
    position = 0
    fuel = K
    while True:
        
        fuel -= 1
        position +=1
    
        if position in chargable:
            if fuel < K and N > position + fuel:
                fuel = K
                count += 1
        
        if position == N:
            break


        if fuel ==0 and position < N:
            count = 0
            break
    
    print('#{} {}'.format(t, count))